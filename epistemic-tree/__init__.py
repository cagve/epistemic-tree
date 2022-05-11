import parser 
import rules as rl
import tree as t
def deny():
    label = parser.Label("1")
    label1 = parser.Label("1.a.3")
    formula1 = parser.Formula("Ka(p => Kbr)")
    formula2 = parser.Formula("---Ka(p => Kbr)")
    formula3 = parser.Formula("------p")
    labelled_formula1 = parser.LabelledFormula(label, formula1 )
    labelled_formula2 = parser.LabelledFormula(label1, formula2 )

    print(labelled_formula2.get_contradiction(labelled_formula1))
    # print(formula3.delete_negation().formula)


def main():
    deny()

if __name__ == '__main__':
    main()
