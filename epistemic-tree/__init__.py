import parser 
import os
import rules as rl
import tree as t

def arbol1():
    f1 = parser.Formula("Kap&&Kbr")
    f3 = parser.Formula("Kbq")
    premises = [f3]
    tree = t.Tree()
    tree.create_tree(f1,premises)
    rl.rule_algorithm(tree)
    tree.print_dot(tree.root)
    print(tree.is_theorem())

def arbol2():
    f1 = parser.Formula("Ka(p=>q)=>(Kap=>Kaq)")
    tree = t.Tree()
    tree.create_tree(f1)
    rl.rule_algorithm(tree)
    tree.print_dot(tree.root)
    print(tree.is_theorem())

def arbol3():
    f1 = parser.Formula("Ka(p||q) => Kap")
    tree = t.Tree()
    tree.create_tree(f1)
    rl.rule_algorithm(tree)
    tree.print_dot(tree.root)
    print(tree.get_open_branchs())

def arbol4():
    f1 = parser.Formula("Kap&&q")
    tree = t.Tree()
    tree.create_tree(f1)
    rl.rule_algorithm(tree)
    tree.print_dot(tree.root)
    print(tree.is_theorem())

def cli():
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
    tree.create_tree(conclusion,premisas)
    rl.rule_algorithm(tree)
    tree.print_dot(tree.root)
    os.system('dot -Tpng ~/epistemic-tree/lib/dots/graph_test.dot > ~/test.png')
    os.system('notify-send "'+str(tree.is_theorem())+'"')
    os.system('feh ~/test.png')


def test_theorem(conclusion, premisas):
    tree = t.Tree()
    lista_premisas = []
    if premisas:
        for premisa in premisas:
            formula = parser.Formula(premisa)
            lista_premisas.append(formula)

    formula = parser.Formula(conclusion)
    tree.create_tree(formula,lista_premisas)
    rl.rule_algorithm(tree)
    return tree.is_theorem()

def main():
    arbol4()


if __name__ == '__main__':
    main()
