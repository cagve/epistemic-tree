import sys
import rules as rl
import tree as t
import parser
import unittest

help = """
Comando no encontrado, comandos disponibles:

rules 1  -> Ejemplo de árbol 1
rules 2  -> Ejemplo de árbol 2
tree     -> Creación de árbol binario con índices
formulas -> Test de métodos de fórmulas
labels   -> Test de métodos de etiquetas
"""

def test_tree():
    label = parser.Label("1")
    formula1 = parser.Formula("-Kap&&-Kaq")
    labelled_formula1 = parser.LabelledFormula(label, formula1 )
    tree = t.Tree(labelled_formula1)
    print("----------------")
    tree.print_label_tree(tree.root, 2)
    print("----------------")
    
    msg = "¿Qué hacer? > "
    val = input(msg)
    while val != 'q':
        if val == 's':
            tree.simple_extension(labelled_formula1)
        elif val == 'd':
            tree.double_extension(labelled_formula1,labelled_formula1)

        print("----------------")
        tree.print_label_tree(tree.root, 2)
        print("----------------")
        val = input(msg)



def test_rules(case:int):
    ########CASO 1#########
    #     1 -Kap&&-Kaq    #
    #     1 -Kap          #
    #     1 -Kaq          #
    #     1.a.1 -p        #
    #     1.a.2 -q        #
    #######################
    if case == 1:
        label = parser.Label("1")
        formula1 = parser.Formula("-Kap&&-Kaq")

        labelled_formula1 = parser.LabelledFormula(label, formula1 )
        tree = t.Tree(labelled_formula1)

        print("################### INITIAL TREE ######################")
        tree.print_tree(tree.root,2)
        print()

        rl.conjuntion_rule(tree.root,tree)
        rl.neg_know_rule(tree.root.left,tree)
        rl.neg_know_rule(tree.root.left.left,tree)
        print("################### FINAL TREE ######################")
        tree.print_tree(tree.root,2)

    ########CASO 2##########
    #     1 -(Kap&&Kaq)    #
    #           |          #
    #          / \         #
    #         /   \        #
    #    1 -Kap   1 -Kaq   #
    #   1.a.1 -p  1.a.1 -q #
    ########################
    elif case == 2: 
        label = parser.Label("1")
        formula1 = parser.Formula("-(Kap&&Kaq)")
        labelled_formula1 = parser.LabelledFormula(label, formula1 )

        tree = t.Tree(labelled_formula1)
        print("################### INITIAL TREE ######################")
        tree.print_tree(tree.root,2)
        print()

        rl.neg_conjuntion_rule(tree.root,tree)
        rl.neg_know_rule(tree.root.left,tree)
        rl.neg_know_rule(tree.root.right,tree)
        print("################### FINAL TREE ######################")
        tree.print_tree(tree.root,2)

def check_formula_methods():
    form = input("Introduce una fórmula: ")
    f1 = parser.Formula(form)

    if f1.parse():
        print("\n* Esta es una fórmula válida\n")
        print("* Tipo de fórmula =>" + f1.get_formula_type()+"\n")
        print("* Agente de la fórmula " + f1.get_agent()+"\n")
        print("* Longitud de la fórmula " + f1.get_len().__str__()+"\n")
        print("* Los términos de la fórmula son ")
        for i in f1.get_terms():
            print(i.formula)
        print("* Las subfórmulas son ")
        for i in f1.get_subformulas():
            print(i.formula)
    else:
        print("Fórmula no válida")

def check_label_methods():
    form = input("Introduce una etiqueta: ")
    l = parser.Label(form)
    if l.parse():
        print("Es válida")
    else:
        print("No es válida")

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

    def rule_type(self):
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

if __name__ == '__main__':
    unittest.main() 

