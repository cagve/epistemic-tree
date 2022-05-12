import os
import tree as t
import rules as rl
import parser
from simple_term_menu import TerminalMenu
	
def apply_rule(argument,node,tree):
    if argument == 'conjuntion_rule':
        rl.conjuntion_rule(node,tree)
    elif argument == 'disjunction_rule':
        rl.disjunction_rule(node,tree)
    elif argument == 'implication_rule':
        rl.implication_rule(node,tree)
    elif argument == 'know_rule':
        rl.know_rule(node,tree)
    elif argument == 'neg_conjunction_rule':
        rl.neg_conjunction_rule(node,tree)
    elif argument == 'neg_disjunction_rule':
        rl.neg_disjunction_rule(node,tree)
    elif argument == 'neg_implication_rule':
        rl.neg_implication_rule(node,tree)
    elif argument == 'neg_know_rule':
        rl.neg_know_rule(node,tree)


def menu(tree):
    options = [ 'conjuntion_rule', 'disjunction_rule', 'implication_rule', 'know_rule', 'neg_conjunction_rule', 'neg_disjunction_rule', 'neg_implication_rule', 'neg_know_rule']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    rule = options[menu_entry_index]
    id = input("Sobre que nodo aplicar la regla "+rule+"? ")
    node = tree.get_node_from_id(tree.root,int(id))
    apply_rule(rule,node,tree)
    print_tree(tree)
    os.system('clear')
    menu(tree)

    

def crear_arbol():
    premisas=[]
    try:
        while True:
            entrada = input("Introduzca premisa: ")  
            if entrada == 'exit':
                break
            formula = parser.Formula(entrada)
            if not formula.parse():
                print("Error")
            else:
                premisas.append(formula)
    except KeyboardInterrupt:
        pass
    print()
    conclusion = parser.Formula(input('Introduzca conclusión: '))
    tree = t.Tree()
    tree.create_tree(premisas,conclusion)
    print_tree(tree)
    os.system('clear')
    menu(tree)


def print_tree(tree):
    tree.print_dot(tree.root)
    os.system('dot -Tpng ~/epistemic-tree/lib/dots/graph_test.dot > ~/test.png')



if __name__ == "__main__":
    crear_arbol()

