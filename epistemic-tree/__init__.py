import parser 
import rules as rl
import tree as t
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

    tree.print_tree(tree.root,2)
    tree.tree_to_dot(tree.root)
    tree.get_pairs(tree.root)


def main():
    deny()

if __name__ == '__main__':
    main()
