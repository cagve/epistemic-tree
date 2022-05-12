import parser 
import rules as rl
import tree as t

def know():
    label = parser.Label("1")
    f1 = parser.Formula("-Kap&&Kaq")
    f2 = parser.Formula("-Kar")

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

    f1 = parser.Formula("Ka(p=>r)")
    f2 = parser.Formula("Ka(p=>q)&&Ka(q=>r)")
    premises = [f2]
    tree = t.Tree()
    tree.create_tree(premises,f1)
    rl.conjuntion_rule(tree.root.left,tree)
    rl.neg_know_rule(tree.root,tree)
    rl.know_rule(tree.root.left.left,tree)
    tree.print_tree(tree.root,2)
    tree.print_label_tree(tree.root,2)
    

def deny():

    label = parser.Label("1")
    f1 = parser.Formula("p=>q")
    f2 = parser.Formula("r=>-q")
    f3 = parser.Formula("-(r=>-p)")

    lf1 = parser.LabelledFormula(label, f1 )
    lf2 = parser.LabelledFormula(label, f2 )
    lf3 = parser.LabelledFormula(label, f3 )
    tree = t.Tree(lf1)
    tree.simple_extension(lf2)
    tree.simple_extension(lf3)

    rl.neg_implication_rule(tree.root.left.left, tree)
    rl.implication_rule(tree.root, tree)
    rl.implication_rule(tree.root.left, tree)

    tree.print_dot(tree.root)


def main():
    entrada()

if __name__ == '__main__':
    main()
