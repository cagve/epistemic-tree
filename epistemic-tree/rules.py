import tree as eptree
import parser

#HACK: [Mejora] una única función y con casos
def conjuntion_rule(node: eptree.Node, tree: eptree.Tree):
    formula = node.get_formula()
    if formula.get_formula_type() != "and":
        #TODO: Error handling
        print("ERROR")

    labelled_formula1 = parser.LabelledFormula(node.get_label(), formula.get_terms()[0])
    labelled_formula2 = parser.LabelledFormula(node.get_label(), formula.get_terms()[1])
    tree.simple_extension(labelled_formula1)
    tree.simple_extension(labelled_formula2)

def neg_conjuntion_rule(node: eptree.Node, tree: eptree.Tree):    
    neg_formula = node.get_formula()
    if neg_formula.get_formula_type() != "not":
        #TODO: Error handling
        print("ERROR")

    formula = neg_formula.get_terms()[0]

    labelled_formula1 = parser.LabelledFormula(node.get_label(), formula.get_terms()[0])
    labelled_formula2 = parser.LabelledFormula(node.get_label(), formula.get_terms()[1])
    tree.double_extension(labelled_formula1,labelled_formula2)


def apply_rule(tree: eptree.Tree):
    print("test")


