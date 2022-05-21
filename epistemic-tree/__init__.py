import parser 
import epmodel
import os
import rules as rl
import eptree as t
import test 


def arbol1():
    f1 = parser.Formula("Kap&&Kbr")
    f3 = parser.Formula("Kbq")
    premises = [f3]
    tree = t.Tree()
    tree.create_tree(f1,premises)
    rl.rule_algorithm(tree)
    print(tree.open_branch())
    model = tree.create_counter_model()
    print(model)
    model[0].print_model()
    tree.print_tree(tree.root,2)

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
    tree.print_dot(tree.root)
    os.system('dot -Tpng ~/epistemic-tree/lib/dots/graph_test.dot > ~/test.png')
    os.system('feh ~/test.png')


def create_model():
    f1 = parser.Formula("Kap")
    f3 = parser.Formula("-Ka-q")
    premises = [f3]
    tree = t.Tree()
    tree.create_tree(f1,premises)
    rl.rule_algorithm(tree)
    tree.print_tree(tree.root,2)
    branch = tree.get_branch(tree.root.left.left.left)
    labelbranch = branch.get_label_branch()

    modelo = epmodel.Model()
    for label in  labelbranch:
        world = epmodel.World(str(label.simplify_label()))
        world.add_true_formula_list(filter(lambda x: x.is_literal(), label.get_formulas(tree.root)))
        modelo.add_world(world)
        if branch.get_simple_extensions(label) !=None:
            for ext in branch.get_simple_extensions(label):
                agent=ext.get_agent()
                world1 = epmodel.World(str(label.simplify_label()))
                world2 = epmodel.World(str(ext.simplify_label()))
                relation = epmodel.Relation(world1,world2,agent) 
                modelo.add_relation(relation)
    modelo.print_model()
    modelo.print_dot()
def main():
    create_model()

if __name__ == '__main__':
    main()
