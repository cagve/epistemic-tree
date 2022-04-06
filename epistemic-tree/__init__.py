import parser 

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

def main():
    l = parser.Label("1.a.2.3")
    if l.parse():
        print("Es válida")
    else:
        print("No es válida")

if __name__ == '__main__':
    main()
