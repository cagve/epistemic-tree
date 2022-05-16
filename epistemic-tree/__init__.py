import parser 
import rules as rl
import tree as t

def know():
    label = parser.Label("1")
    f1 = parser.Formula("Kap&&Kbq")
    f2 = parser.Formula("Kbr")

    lf1 = parser.LabelledFormula(label, f1 )
    lf2 = parser.LabelledFormula(label, f2 )
    tree = t.Tree(lf1)
    tree.simple_extension(lf2)
    rl.conjunction_rule(tree.root, tree)
    rl.not_know_rule(tree.root.left,tree)
    rl.not_know_rule(tree.root.left.left,tree)
    rl.know_rule(tree.root.left.left.left,tree)

    tree.print_dot(tree.root)
    tree.print_tree(tree.root,2)

def arbol1():
    f1 = parser.Formula("Kap&&Kbr")
    f3 = parser.Formula("Kbq")
    premises = [f3]
    tree = t.Tree()
    tree.create_tree(premises,f1)
    rl.rule_algorithm(tree)
    tree.print_tree(tree.root,2)
    tree.print_dot(tree.root)

def arbol2():
    f1 = parser.Formula("Ka(p=>q)=>(Kap&&Kaq)")
    tree = t.Tree()
    tree.create_tree(f1)
    rl.rule_algorithm(tree)
    tree.print_dot(tree.root)

def deny():
    label = parser.Label("1")
    f1 = parser.Formula("-(Ka(p => Kbr))")
    f2 = parser.Formula("Ka(p => Kbr)")
    lf1 = parser.LabelledFormula(label, f1 )
    lf2 = parser.LabelledFormula(label, f2 )
    print(f1.deny_formula().formula)

def test():
    label = parser.Label('1')
    formula1 = parser.Formula('Kap')
    formula2 = parser.Formula('Kap||r')
    formula3 = parser.Formula('-Kap')
    formula4 = parser.Formula('(Kap=>r)')
    formula5 = parser.Formula('-(Kap=>r)')

    l1 = parser.LabelledFormula(label,formula1)
    l2 = parser.LabelledFormula(label,formula2)
    l3 = parser.LabelledFormula(label,formula3)
    l4 = parser.LabelledFormula(label,formula4)
    l5 = parser.LabelledFormula(label,formula5)
    
    print(t.Node(l1,1).get_rule())
    print(t.Node(l2,11).get_rule())
    print(t.Node(l3,111).get_rule())
    print(t.Node(l4,1111).get_rule())
    print(t.Node(l5,11111).get_rule())
    



def main():
    arbol2()

if __name__ == '__main__':
    main()
