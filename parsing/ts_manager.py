# Conjunto de funciones para trababajar con tree-sitter. 
from tree_sitter import Parser,Language

LP_LANGUAGE = Language('tree-sitter/build/my-languages.so', 'ep')

parser = Parser()
parser.set_language(LP_LANGUAGE)

# Obtiene el texto de un nodo
def get_text(node,formula):
    source_code_bytes=bytes(formula,'utf-8')
    byte_text = source_code_bytes[node.start_byte:node.end_byte]
    string = byte_text.decode('utf-8')
    return  string

# Obtiene el arbol de la fórmula
def get_tree(formula):
    # Convertimo la fórmula a bytes
    formula=formula.replace(" ","")
    formula_bytes=bytes(formula,'utf-8')

    # Creamos el parser
    tree = parser.parse(formula_bytes)
    return tree

# Obtiene el nodo raíz del árbol(el nodo equivalente a la fórmula)
def get_root_node(formula):
    tree = get_tree(formula)
    root = tree.root_node
    return root

# Devuelve la lista sub(A)
def get_subformulas(formula):
    root = get_root_node(formula)
    fbf_query = LP_LANGUAGE.query("""
            (si_formula)  @expression
            (and_formula) @expression
            (or_formula)  @expression
            (eq_formula)  @expression
            (negation_formula) @expression
            (atom) @expression
            """)

    fbf = fbf_query.captures(root)
    formula_stack = []
    for i in fbf:
        current_node = i[0]
        node_text=get_text(current_node,formula)
        formula_stack.append(node_text) # Añado las fórmulas a una pila
    return formula_stack

# Función que devuelve el operador principal de la fórmula. 
def get_formula_type(formula):
    tree = get_tree(formula)

    cursor = tree.walk()
    cursor.goto_first_child()
    return{
        'and_formula'      : "and",
        'or_formula'       : "or",
        'negation_formula' : "not"
        }.get(cursor.node.type)

def main():
    print(get_subformulas("p&&(q||r)"))



