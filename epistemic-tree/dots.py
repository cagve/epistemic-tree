import tree as t
import rules as rl
import parser

label = parser.Label("1")
formula1 = parser.Formula("-(Kap&&Kaq)")
labelled_formula1 = parser.LabelledFormula(label, formula1 )

tree = t.Tree(labelled_formula1)
rl.neg_conjuntion_rule(tree.root,tree)
rl.neg_know_rule(tree.root.left,tree)
rl.neg_know_rule(tree.root.right,tree)


tree.print_dot(tree.root)

