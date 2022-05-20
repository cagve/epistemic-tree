import parser 
import os
import rules as rl
import eptree as t
import test 

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
    return(tree.open_branch())

def cli():
    premisas=[]
    try:
        while True:
            entrada = input("Introduzca premisa: ")  
            formula = parser.Formula(entrada)
            if not formula.parse():
                print("Formula not valid")
            else:
                premisas.append(formula)
    except KeyboardInterrupt:
        pass
    print()
    conclusion = parser.Formula(input('Introduzca conclusión: '))
    tree = t.Tree()
    tree.create_tree(conclusion,premisas)
    rl.rule_algorithm(tree)
    print(tree.open_branch())
    tree.print_open_close_branchs()
    tree.print_dot(tree.root)
    os.system('dot -Tpng ~/epistemic-tree/lib/dots/graph_test.dot > ~/test.png')
    os.system('feh ~/test.png')



def main():
    cli()

if __name__ == '__main__':
    main()
