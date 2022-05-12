import tree as t
import rules as rl
import parser

label = parser.Label("1.a.2")
label2 = parser.Label("1.a.2.a.3")
label3 = parser.Label("1.a.2.b.3")
label4 = parser.Label("1.b.2.b.4")
formula1 = parser.Formula("-(Kap&&Kaq)")
labelled_formula1 = parser.LabelledFormula(label, formula1 )

tree = t.Tree(labelled_formula1)
rl.neg_conjuntion_rule(tree.root,tree)
rl.neg_know_rule(tree.root.left,tree)
rl.neg_know_rule(tree.root.right,tree)

# for i in tree.get_label_branch(branch):
#     print(i.label)


