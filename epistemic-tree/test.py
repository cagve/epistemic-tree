import sys
import rules as rl
import tree as t
import parser
import __init__ as init
import unittest

# Arbol = [conclusion, premisas, solución]
trees = {
    'tree1':['Kap&&q', None , False],
    'tree2':['Kap&&q', ['-q']  , False],
        }

class TestUnit(unittest.TestCase):
    def test_rules(self):
        label1 = parser.Label("1")

        formula1 = parser.Formula("p&&q")
        formula2 = parser.Formula("-Kap")
        formula3 = parser.Formula("-(Ka(p => Kbr))")
        formula4 = parser.Formula("(Kap&&(r=>r))=>-p")

        lab_formula1 = parser.LabelledFormula(label1,formula1)
        lab_formula2 = parser.LabelledFormula(label1,formula2)
        lab_formula3 = parser.LabelledFormula(label1,formula3)
        lab_formula4 = parser.LabelledFormula(label1,formula4)
        self.assertEqual(rl.get_formula_rule(lab_formula1),'conjunction_rule')
        self.assertEqual(rl.get_formula_rule(lab_formula2),'not_know_rule')

    def test_paser(self):
        self.assertEqual(parser.Formula("p").parse(),True)
        self.assertEqual(parser.Formula("p&&q").parse(),True)
        self.assertEqual(parser.Formula("p=>p").parse(),True)
        self.assertEqual(parser.Formula("(Kap&&(r=>r))=>-p").parse(),True)
        self.assertEqual(parser.Formula("p(&&q)").parse(),False)

    def test_type(self):
        self.assertEqual(parser.Formula("p").get_formula_type(),'atom')
        self.assertEqual(parser.Formula("-(p&&q)").get_formula_type(),'not_and')
        self.assertEqual(parser.Formula("-(p=>p)").get_formula_type(),'not_iff')
        self.assertEqual(parser.Formula("-(Kap&&(r=>r))=>-p").get_formula_type(),'iff')
        self.assertEqual(parser.Formula("-Kap)").get_formula_type(),'not_know')

    def test_neg(self):
        label1 = parser.Label("1")
        label2 = parser.Label("2")

        formula1 = parser.Formula("p")
        formula2 = parser.Formula("-Kap")
        formula3 = parser.Formula("-(Ka(p => Kbr))")
        formula4 = parser.Formula("(Kap&&(r=>r))=>-p")
        lab_formula1 = parser.LabelledFormula(label1,formula1)
        lab_formula2 = parser.LabelledFormula(label1,formula2)
        lab_formula3 = parser.LabelledFormula(label1,formula3)
        lab_formula4 = parser.LabelledFormula(label1,formula4)

        formulaa = parser.Formula("--------p")
        formulab = parser.Formula("Kap")
        formulac = parser.Formula("Ka(p => Kbr)")
        formulad = parser.Formula("-((Kap&&(r=>r))=>-p)")
        lab_formulaa = parser.LabelledFormula(label1,formulaa)
        lab_formulab = parser.LabelledFormula(label2,formulab)
        lab_formulac = parser.LabelledFormula(label1,formulac)
        lab_formulad = parser.LabelledFormula(label1,formulad)

        self.assertEqual(lab_formula1.get_contradiction(lab_formulaa),False)
        self.assertEqual(lab_formula2.get_contradiction(lab_formulab),False)
        self.assertEqual(lab_formula3.get_contradiction(lab_formulac),True)
        self.assertEqual(lab_formula4.get_contradiction(lab_formulad),True)

    def test_rule_type(self):
        label1 = parser.Label("1")
        label2 = parser.Label("2")

        formula1 = parser.Formula("p&&q")
        formula2 = parser.Formula("-(Kap&&Kbq)")
        formula3 = parser.Formula("-Kap")
        formula4 = parser.Formula("Ka(p => Kbr)")
        formula4 = parser.Formula("(Kap&&(r=>r))=>-p")
        lab_formula1 = parser.LabelledFormula(label1,formula1)
        lab_formula2 = parser.LabelledFormula(label1,formula2)
        lab_formula3 = parser.LabelledFormula(label1,formula3)
        lab_formula4 = parser.LabelledFormula(label1,formula4)

        n1 = t.Node(lab_formula1,1)
        n2 = t.Node(lab_formula2,1)
        n3 = t.Node(lab_formula3,1)
        n4 = t.Node(lab_formula4,1)

        self.assertEqual(n1.get_rule_type(),'alpha')
        self.assertEqual(n2.get_rule_type(),'beta')
        self.assertEqual(n3.get_rule_type(),'pi')
        self.assertEqual(n4.get_rule_type(),'beta')

    def test_trees(self):
        for key,value in trees.items():
            print("Test "+key)
            self.assertEqual(init.test_theorem(value[0],value[1]),value[2])
    
if __name__ == '__main__':
    unittest.main() 

