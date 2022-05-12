# Conjunto de funciones para trababajar con tree-sitter. 
from types import new_class
from tree_sitter import Parser as TSParser 
from tree_sitter import Language as TSLanguage

LP_LANGUAGE = TSLanguage('lib/tree-sitter/build/my-languages.so', 'ep')
LABEL_LANGUAGE = TSLanguage('lib/tree-sitter/build/my-languages.so', 'label')

class Parser():
    """Class to handle treesitter lib"""
    def __init__(self,cadena,language):
        self.cadena=cadena
        self.language = language

    def get_parser(self):
        parser = TSParser()
        parser.set_language(self.language)
        return parser

    def get_tree(self):
        cadena=self.cadena.replace(" ","")
        cadena_bytes=bytes(cadena,'utf-8')
        tree = self.get_parser().parse(cadena_bytes)
        return tree

    def get_root_node(self):
        tree = self.get_tree()
        root = tree.root_node
        return root

    def get_node_text(self,node):
        source_code_bytes=bytes(self.cadena,'utf-8')
        byte_text = source_code_bytes[node.start_byte:node.end_byte]
        node_text = byte_text.decode('utf-8')
        return node_text


class Formula:
    # ?? ESTA ESTO BIEN PUESTO AQUÍ???????
    """Class for formula managment"""
    def __init__(self, formula):
        if(formula[0]=='(' and formula[-1]==')'): # ESTE IF ELIMINA LOS PARÉNTESIS EXTERIORES
            self.formula=formula[1:-1].replace(" ","")
        else:
            self.formula=formula.replace(" ","")
        self.ts = Parser(self.formula,LP_LANGUAGE)
        self.tree = self.ts.get_tree()
        self.node = self.ts.get_root_node()

    def get_subformulas(self):
        fbf_query = LP_LANGUAGE.query("""
                (formula
                    operator:(or))@or_formula
                (formula
                    operator:(and))@and_formula
                (formula
                    operator:(iff))@iff_formula
                (formula
                    operator:(know))@eq_formula
                (formula
                    operator:(eq))@eq_formula
                (formula
                    operator:(not))@not_formula
                (atom) @atom_formula
                """)
        fbf = fbf_query.captures(self.node)
        formula_stack = []
        subformulas = []
        for i in fbf:
            current_formula = i[0]
            node_text=self.ts.get_node_text(current_formula)
            formula_stack.append(node_text) # Añado las fórmulas a una pila
            formula_stack=list(dict.fromkeys(formula_stack))
        for i in formula_stack:
            formula=Formula(i)
            subformulas.append(formula)

        j=0
        size=len(subformulas)

        # Bubble sort: algoritmo para ordenar de mayor a menor las fórmulas
        for i in range(size-1):
            for j in range(0, size-i-1):
                if subformulas[j].get_len() < subformulas[j + 1].get_len():
                    subformulas[j], subformulas[j + 1] = subformulas[j + 1], subformulas[j]
        return subformulas

    def get_formula_type(self):
        node = self.node
        operator=node.child_by_field_name('operator')
        if(operator == None):
            return "atom"
        else:
            return operator.type

    def get_terms(self) -> list:
        node=self.node
        type=self.get_formula_type()
        term_list = []
        if(type=="atom"):
            term_list.append(self)
        elif(type=="not" or type=="know"):
            term=node.child_by_field_name('term')
            formula=Formula(self.ts.get_node_text(term))
            term_list.append(formula)
        else:
            first_term=node.child_by_field_name('left_term')
            second_term=node.child_by_field_name('right_term')
            first_formula=Formula(self.ts.get_node_text(first_term))
            second_formula=Formula(self.ts.get_node_text(second_term))
            term_list.append(first_formula)
            term_list.append(second_formula)
        return term_list
    
    # Elimina los paréntesis exteriores. Pensar
    def simplify_par(self):
        if(self.formula[0]=='('):
                self.formula=self.formula[1:-1]

    def get_len(self): # FALLO para los operadores negadores
        type=self.get_formula_type()
        len=0
        if(type=="atom"):
            len=1
        else:
            len=1
            for i in self.get_terms():
                len=len+i.get_len()
        return len

    def parse(self):
        fbf_query = LP_LANGUAGE.query("""
                (ERROR)@error
                """)
        # Captura los errores
        fbf = fbf_query.captures(self.node)
        # Bucle que comprueba que hay el mismo numero de parentesis abiuertos y cerrados
        # En caso de que j<0 ocurre cuando ocurre un ) antes que un (. Esto es porque en el caso de los paréntesis Treesitter no lo capta como error
        flag=True
        j = 0
        for char in self.formula:
            if char == ')':
                j -= 1
                if j < 0:
                    flag=False
            elif char == '(':
                j += 1
            flag=j == 0
        return flag and len(fbf)==0

    def get_agent(self):
        cursor = self.tree.walk()
        if(self.get_formula_type()=="know"): # Por el árbol que te genera para acceder al agente tenemos que ir a hijo e hijo y hermano
            assert cursor.goto_first_child()
            assert cursor.goto_first_child()
            assert cursor.goto_next_sibling()
            agent = cursor.node
            return self.ts.get_node_text(agent)
        else: 
            # Crear un tipo de error para esto
            print("No es una fórmula de conocimiento")
            return ""

    def deny_formula(self):
        return Formula("-("+self.formula+")")

    def delete_negation(self):
        if self.get_formula_type() != 'not':
            return self
        elif self.get_terms()[0].get_formula_type() == 'not': 
            return self.get_terms()[0].get_terms()[0].delete_negation()
        else:
            return self


    def simplify_formula(self):
        if self.get_formula_type() == 'not':
            # Simplifica las negaciones:  ---p => -p
            if self.get_terms()[0].get_formula_type() == 'not':
                return self.delete_negation()
            # Simplifica los parentesis de la negación -(p) --> -p
            elif self.get_terms()[0].get_formula_type() == 'atom' or self.get_terms()[0].get_formula_type() == 'know':
                return Formula("-"+self.get_terms()[0].formula) 
            else: 
                return self
        else:
            return self



class Label(): 
    # TODO: [improve] Mirar que herede los métodos de lista
    def __init__(self,label):
        self.label = label
        self.ts = Parser(self.label,LABEL_LANGUAGE)
        self.tree = self.ts.get_tree()
        self.node = self.ts.get_root_node()

    def parse(self):
        fbf_query = LP_LANGUAGE.query("""
                (ERROR)@error
                """)
        fbf = fbf_query.captures(self.node)
        return len(fbf)==0

    def len(self):
       return len(self.label.replace('.',''))

    def is_sublabel(self,label)-> bool:
        """label1.is_subset(label2) => """
        # label2 = parser.Label(label)
        if self.len() > label.len():
            return False
        else:
            label1_list = []
            label2_list = []
            for member in self.label:
                label1_list.append(member)

            for member in label.label:
                label2_list.append(member)

            i = 0
            for digit in label1_list:
                if digit != label2_list[i]:
                    return False
                i +=1
            return True

    def is_simple_extension(self,label)-> bool:
        len1 = self.len()
        len2 = label.len()+2
        return label.is_sublabel(self) and len1==len2


    def append(self, agent, world):
        new_label = self.label +"."+agent+"."+world
        return Label(new_label)

    def simplify_label(self) -> int:
        """ Devuelve el núímero de la etiqueta 1.a.2.b.3 -> 123"""
        label_num  = ""
        for number in self.label:
            if number.isdigit():
                label_num = label_num+number
        return int(label_num)



    # TODO: [fun] label.to_list() -> list: label en forma de lista
    # TODO: [fun] label.len() -> int:  longitud de la etiqueta
    # TODO: [fun] label1.relation(label2) -> string: non-proper extension o proper extension.
    # TODO: [fun] label.append(agent,world) -> Incluye en la etiqueta la extensión "agent.world"

class LabelledFormula:
    def __init__(self, label, formula) -> None:
        self.label = label
        self.formula = formula

    def get_contradiction(self, lab_formula) -> bool:
        deny_formula = self.formula.deny_formula().simplify_formula()
        formula = lab_formula.formula.simplify_formula()
        if deny_formula.formula == formula.formula:
            return True
        return False
        
    def to_string(self):
        return self.label.label+" "+self.formula.formula

    # TODO: [fun] label.from(str) -> LabelledFormula: Devuelve una fórmula creada a partir de una string completa 1.a.2.3-Kap (estudiar como separarlo)
