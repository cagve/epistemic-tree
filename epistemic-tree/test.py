import sys
import rules as rl
import tree as t
import parser

help = """
Comando no encontrado, comandos disponibles:

rules 1  -> Ejemplo de árbol 1
rules 2  -> Ejemplo de árbol 2
tree     -> Creación de árbol binario con índices
formulas -> Test de métodos de fórmulas
labels   -> Test de métodos de etiquetas
"""

def test_tree():
    label = parser.Label("1")
    formula1 = parser.Formula("-Kap&&-Kaq")
    labelled_formula1 = parser.LabelledFormula(label, formula1 )
    tree = t.Tree(labelled_formula1)
    print("----------------")
    tree.print_label_tree(tree.root, 2)
    print("----------------")
    
    msg = "¿Qué hacer? > "
    val = input(msg)
    while val != 'q':
        if val == 's':
            tree.simple_extension(labelled_formula1)
        elif val == 'd':
            tree.double_extension(labelled_formula1,labelled_formula1)

        print("----------------")
        tree.print_label_tree(tree.root, 2)
        print("----------------")
        val = input(msg)



def test_rules(case:int):
    ########CASO 1#########
    #     1 -Kap&&-Kaq    #
    #     1 -Kap          #
    #     1 -Kaq          #
    #     1.a.1 -p        #
    #     1.a.2 -q        #
    #######################
    if case == 1:
        label = parser.Label("1")
        formula1 = parser.Formula("-Kap&&-Kaq")

        labelled_formula1 = parser.LabelledFormula(label, formula1 )
        tree = t.Tree(labelled_formula1)

        print("################### INITIAL TREE ######################")
        tree.print_tree(tree.root,2)
        print()

        rl.conjuntion_rule(tree.root,tree)
        rl.neg_know_rule(tree.root.left,tree)
        rl.neg_know_rule(tree.root.left.left,tree)
        print("################### FINAL TREE ######################")
        tree.print_tree(tree.root,2)

    ########CASO 2##########
    #     1 -(Kap&&Kaq)    #
    #           |          #
    #          / \         #
    #         /   \        #
    #    1 -Kap   1 -Kaq   #
    #   1.a.1 -p  1.a.1 -q #
    ########################
    elif case == 2: 
        label = parser.Label("1")
        formula1 = parser.Formula("-(Kap&&Kaq)")
        labelled_formula1 = parser.LabelledFormula(label, formula1 )

        tree = t.Tree(labelled_formula1)
        print("################### INITIAL TREE ######################")
        tree.print_tree(tree.root,2)
        print()

        rl.neg_conjuntion_rule(tree.root,tree)
        rl.neg_know_rule(tree.root.left,tree)
        rl.neg_know_rule(tree.root.right,tree)
        print("################### FINAL TREE ######################")
        tree.print_tree(tree.root,2)

def check_formula_methods():
    form = input("Introduce una fórmula: ")
    f1 = parser.Formula(form)

    if f1.parse():
        print("\n* Esta es una fórmula válida\n")
        print("* Tipo de fórmula =>" + f1.get_formula_type()+"\n")
        print("* Agente de la fórmula " + f1.get_agent()+"\n")
        print("* Longitud de la fórmula " + f1.get_len().__str__()+"\n")
        print("* Los términos de la fórmula son ")
        for i in f1.get_terms():
            print(i.formula)
        print("* Las subfórmulas son ")
        for i in f1.get_subformulas():
            print(i.formula)
    else:
        print("Fórmula no válida")

def check_label_methods():
    form = input("Introduce una etiqueta: ")
    l = parser.Label(form)
    if l.parse():
        print("Es válida")
    else:
        print("No es válida")

def main():
    if sys.argv[1] == 'rules':
        test_rules(int(sys.argv[2]))
    elif sys.argv[1] == 'tree':
            test_tree()
    elif sys.argv[1] == 'formulas':
        check_formula_methods()
    elif sys.argv[1] == 'labels':
        check_label_methods()
    else:
        print(help)
        
    
if __name__ == '__main__':
    main()

