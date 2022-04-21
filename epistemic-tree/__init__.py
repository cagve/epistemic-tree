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
    label = parser.Label("1")
    formula1= parser.Formula("p&&Kaq")
    formula2= parser.Formula("p")
    formula3 = parser.Formula("Kaq")
    formula4 = parser.Formula("q")
    formula5 = parser.Formula("r")

    labelled_formula1 = parser.LabelledFormula(label,formula1)
    labelled_formula2 = parser.LabelledFormula(label,formula2)
    labelled_formula3 = parser.LabelledFormula(label,formula3)
    labelled_formula4 = parser.LabelledFormula(label,formula4)
    labelled_formula5 = parser.LabelledFormula(label,formula5)

    tree = eptree.Tree(labelled_formula1)
    tree.simple_extension(labelled_formula2)
    tree.simple_extension(labelled_formula3)
    tree.double_extension(labelled_formula4,labelled_formula5)
    tree.print_tree(tree.root,2)
    print(tree.get_labelled_formula_from_id(tree.root, [1, 1, 1, 2]).get_labelled_formula())

    for n in tree.get_branch(tree.root.left.left.right):
        print(n.get_labelled_formula(), end=" > ")


    
def test_rules():
    tree = test_tree() 
    # rl.conjuntion_rule(tree.root,tree) #
    # rl.neg_conjuntion_rule(tree.root.left,tree)

    # tree.print_tree(tree.root, 2)
    # print(tree.root.get_labelled_formula())
    # print("--")
    # print(tree.root.left.get_labelled_formula())
    # print(tree.root.right)
    # print("--")
    # print(tree.root.left.left.get_labelled_formula())
    # print(tree.root.left.right)
    # print("--")
    # print(tree.root.left.left.left.get_labelled_formula())
    # print(tree.root.left.left.right.get_labelled_formula())

def test_labels():
    label1 = parser.Label('1.a.1.a.1')
    label2 = parser.Label('1.b.1')
    label3 = parser.Label('1.a.1')
    label4 = parser.Label('1.a.2')

    print(label1.is_subset(label2))
    print(label2.is_subset(label1))

def main():
    test_tree()

if __name__ == '__main__':
    main()
