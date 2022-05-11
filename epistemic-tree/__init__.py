import parser 
import rules as rl
import tree as t
def deny():
    label = parser.Label("1")
    formula1 = parser.Formula("-Kaq&&Kap")
    formula2 = parser.Formula("--Kap")

    labelled_formula1 = parser.LabelledFormula(label, formula1 )
    labelled_formula2 = parser.LabelledFormula(label, formula2 )
    tree = t.Tree(labelled_formula1)

    rl.conjuntion_rule(tree.root,tree)
    rl.neg_know_rule(tree.root.left,tree)
    rl.neg_know_rule(tree.root.left.left,tree)
    tree.print_tree(tree.root,2)

    leaf_node = tree.get_leafs(tree.root)[0]
    branch = tree.get_branch(leaf_node)
    print(branch.is_close())


def main():
    deny()

if __name__ == '__main__':
    main()
