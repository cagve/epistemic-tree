import parser 
import rules as rl
import tree as eptree

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

def test_tree():
    label = parser.Label("1.a.2")
    formula1= parser.Formula("p&&Kaq")
    formula2= parser.Formula("p")
    formula3 = parser.Formula("Kap")
    formula4 = parser.Formula("q")

    labelled_formula1 = parser.LabelledFormula(label,formula1)
    labelled_formula2 = parser.LabelledFormula(label,formula2)
    labelled_formula3 = parser.LabelledFormula(label,formula3)
    labelled_formula4 = parser.LabelledFormula(label,formula4)

    node1 = eptree.Node(labelled_formula1)
    node2 = eptree.Node(labelled_formula2)
    node3 = eptree.Node(labelled_formula3)
    node4 = eptree.Node(labelled_formula4)

    tree = eptree.Tree(labelled_formula1)
    return tree


    
def test_rules():
    tree = test_tree()
    rl.conjuntion_rule(tree.root,tree)

    print(tree.root)
    print("--")
    print(tree.root.left)
    print(tree.root.right)
    print("--")
    print(tree.root.left.left)
    print(tree.root.left.right)



def main():
    test_rules()

if __name__ == '__main__':
    main()
