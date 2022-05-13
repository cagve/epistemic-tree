from pickle import LONG1
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
    rl.conjuntion_rule(tree.root, tree)
    rl.neg_know_rule(tree.root.left,tree)
    rl.neg_know_rule(tree.root.left.left,tree)
    rl.know_rule(tree.root.left.left.left,tree)

    tree.print_dot(tree.root)
    tree.print_tree(tree.root,2)

def entrada():
    label1 = parser.Label("1")
    label2 = parser.Label("1.a.1")
    label3 = parser.Label("1.b.1")

    f1 = parser.Formula("Kap&&Kbr")
    f3 = parser.Formula("Kbq")
    premises = [f3]
    tree = t.Tree()
    tree.create_tree(premises,f1)
    rl.neg_conjunction_rule(tree.root,tree)
    rl.neg_know_rule(tree.root.left.left,tree)
    rl.neg_know_rule(tree.root.left.right,tree)
    rl.know_rule(tree.root.left,tree)
    tree.print_tree(tree.root,2)

def deny():
    label = parser.Label("1")
    f1 = parser.Formula("Kap&&Kbq")
    f2 = parser.Formula("Kbr")

    lf1 = parser.LabelledFormula(label, f1 )
    lf2 = parser.LabelledFormula(label, f2 )
    tree = t.Tree()
    premises = [f2]
    conclusion = f1
    tree.create_tree(premises,conclusion)
    rl.neg_conjunction_rule(tree.root,tree)
    rl.neg_know_rule(tree.root.left.left,tree)
    rl.neg_know_rule(tree.root.left.right,tree)
    rl.know_rule(tree.root.left,tree)
    tree.print_tree(tree.root,2)


def test():
    label = parser.Label('1')
    formula1 = parser.Formula('Kap')
    formula2 = parser.Formula('Kap||r')
    formula3 = parser.Formula('-Kap')
    formula4 = parser.Formula('--(Kap=>r)')
    formula5 = parser.Formula('---(Kap=>r)')

    l1 = parser.LabelledFormula(label,formula1)
    l2 = parser.LabelledFormula(label,formula2)
    l3 = parser.LabelledFormula(label,formula3)
    l4 = parser.LabelledFormula(label,formula4)
    l5 = parser.LabelledFormula(label,formula5)

    print(formula1.get_formula_type())
    print(formula2.get_formula_type())
    print(formula3.get_formula_type())
    print(formula4.get_formula_type())
    print(formula5.get_formula_type())


def main():
    deny()

if __name__ == '__main__':
    main()
