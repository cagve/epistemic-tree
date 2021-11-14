# Conjunto de funciones para trababajar con tree-sitter. 
from tree_sitter import Parser,Language
LP_LANGUAGE = Language('tree-sitter/build/my-languages.so', 'ep')
parser = Parser()
parser.set_language(LP_LANGUAGE)

class TSManager():
    def __init__(self,formula):
        self.formula=formula

    def get_tree(self):
        formula=self.formula.replace(" ","")
        formula_bytes=bytes(formula,'utf-8')
        tree = parser.parse(formula_bytes)
        return tree

    def get_root_node(self):
        tree = self.get_tree()
        root = tree.root_node
        return root

    def get_node_text(self,node):
        source_code_bytes=bytes(self.formula,'utf-8')
        byte_text = source_code_bytes[node.start_byte:node.end_byte]
        node_text = byte_text.decode('utf-8')
        return node_text
        

class Formula:
    def __init__(self, formula):
        self.formula=formula
        self.ts = TSManager(self.formula)
        self.tree = self.ts.get_tree()
        self.node = self.ts.get_root_node()

    def get_subformulas(self):
        fbf_query = LP_LANGUAGE.query("""
                (si_formula)  @expression
                (and_formula) @expression
                (or_formula)  @expression
                (eq_formula)  @expression
                (negation_formula) @expression
                (atom) @expression
                """)
        fbf = fbf_query.captures(self.node)
        formula_stack = []
        for i in fbf:
            current_formula = i[0]
            node_text=parser.get_node_text(current_formula)
            formula=Formula(node_text)
            formula_stack.append(formula) # Añado las fórmulas a una pila
        return formula_stack

    def get_formula_type(self):
        cursor = self.tree.walk()
        cursor.goto_first_child()
        return{
            'si_formula'      : "si",
            'eq_formula'      : "eq",
            'and_formula'      : "and",
            'or_formula'       : "or",
            'negation_formula' : "not",
            'atom' : "atom"
            }.get(cursor.node.type)

    def get_term(self):
        cursor = self.tree.walk()
        type=self.get_formula_type()
        if(type=="atom"):
            return self.formula
        elif(type=="not"):
            cursor.goto_first_child()     
            cursor.goto_first_child()     
            cursor.goto_next_sibling()
            return self.ts.get_node_text(cursor.node)
        else:
            return "No implementado"


