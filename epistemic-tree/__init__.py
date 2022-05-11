import parser 
import rules as rl
import tree as t
def deny():
    label = parser.Label("1")
    formula1 = parser.Formula("-(-(-p&&p)&&-(-p&&p))")
    # formula1 = parser.Formula("-(Kap&&Kaq))")

    labelled_formula1 = parser.LabelledFormula(label, formula1 )
    tree = t.Tree(labelled_formula1)

    rl.neg_conjuntion_rule(tree.root,tree)
    rl.conjuntion_rule(tree.root.left,tree)

    tree.print_tree(tree.root,2)


def main():
    deny()

if __name__ == '__main__':
    main()
