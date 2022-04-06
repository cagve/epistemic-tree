import parser 
import tree

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

def check_nodes():
    label = parser.Label("1.a.2")
    formula = parser.Formula("Kap")

    labelled_formula = parser.LabelledFormula(label,formula)

    node1 = tree.Node(labelled_formula)
    print(node1.get_formula())
    print(node1.get_label())

def main():
    # check_formula_methods()
    check_label_methods()
    # check_nodes()

if __name__ == '__main__':
    main()
