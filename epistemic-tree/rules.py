from os import wait
import tree as eptree
import parser

type_rules = {
        'and':'alpha', 
        'disjunction_rule':'beta', 
        'implication_rule':'beta',
        'know_rule':'nu',
        'neg_conjunction_rule':'beta',
        'neg_disjunction_rule':'alpha',
        'neg_implication_rule':'alpha',
        'neg_know_rule':'pi'
    }

def alpha_rule(node: eptree.Node, tree: eptree.Tree, term1: parser.LabelledFormula, term2: parser.LabelledFormula):
    leafs = tree.get_available_leafs(node)
    for leaf in leafs:
        id1 = int(str(leaf.id)+str(1))
        id2 = int(str(leaf.id)+str(11))
        leaf.add_one_child(term1,id1)
        leaf.left.add_one_child(term2,id2)

def beta_rule(node: eptree.Node, tree: eptree.Tree, term1: parser.LabelledFormula, term2: parser.LabelledFormula):
    leafs = tree.get_available_leafs(node)
    for leaf in leafs:
        id1 = int(str(leaf.id)+str(1))
        id2 = int(str(leaf.id)+str(2))
        leaf.add_two_childs(term1, term2,id1,id2)

# ALPHA RULES
def conjuntion_rule(node: eptree.Node, tree: eptree.Tree):
    formula = node.get_formula()
    if formula.get_formula_type() != "and":
        #TODO: Error handling
        print("ERROR CON ")
    labelled_formula1 = parser.LabelledFormula(node.get_label(), formula.get_terms()[0].delete_negation())
    labelled_formula2 = parser.LabelledFormula(node.get_label(), formula.get_terms()[1].delete_negation())
    alpha_rule(node, tree, labelled_formula1, labelled_formula2)

def neg_conjunction_rule(node: eptree.Node, tree: eptree.Tree):    
    neg_formula = node.get_formula()
    if neg_formula.get_formula_type() != "not_and":
        #TODO: Error handling
        print("ERROR NEG CON")

    formula = neg_formula.get_terms()[0]

    denied_formula1 = formula.get_terms()[0].deny_formula().delete_negation()
    denied_formula2 = formula.get_terms()[1].deny_formula().delete_negation()

    labelled_formula1 = parser.LabelledFormula(node.get_label(), denied_formula1)
    labelled_formula2 = parser.LabelledFormula(node.get_label(), denied_formula2)
    beta_rule(node, tree, labelled_formula1, labelled_formula2)

def disjunction_rule(node: eptree.Node, tree: eptree.Tree):
    formula = node.get_formula()
    if formula.get_formula_type() != "or":
        print("ERROR DIS")
    labelled_formula1 = parser.LabelledFormula(node.get_label(), formula.get_terms()[0].delete_negation())
    labelled_formula2 = parser.LabelledFormula(node.get_label(), formula.get_terms()[1].delete_negation())
    beta_rule(node, tree, labelled_formula1, labelled_formula2)

def neg_disjunction_rule(node: eptree.Node, tree: eptree.Tree):
    neg_formula = node.get_formula()
    if neg_formula.get_formula_type() != "not_or":
        #TODO: Error handling
        print("ERROR NEG DIS")
    formula = neg_formula.get_terms()[0]

    denied_formula1 = formula.get_terms()[0].deny_formula().delete_negation()
    denied_formula2 = formula.get_terms()[1].deny_formula().delete_negation()
    labelled_formula1 = parser.LabelledFormula(node.get_label(), denied_formula1)
    labelled_formula2 = parser.LabelledFormula(node.get_label(), denied_formula2)
    alpha_rule(node, tree, labelled_formula1, labelled_formula2)

def implication_rule(node: eptree.Node, tree: eptree.Tree):
    formula = node.get_formula()
    if formula.get_formula_type() != "iff":
        print("ERROR IMP")
    denied_formula1 = formula.get_terms()[0].deny_formula().delete_negation()
    formula2 = formula.get_terms()[1].delete_negation()
    labelled_formula1 = parser.LabelledFormula(node.get_label(), denied_formula1)
    labelled_formula2 = parser.LabelledFormula(node.get_label(), formula2)
    beta_rule(node,tree,labelled_formula1, labelled_formula2)

def neg_implication_rule(node: eptree.Node, tree: eptree.Tree):
    neg_formula = node.get_formula()
    if neg_formula.get_formula_type() != "not_iff":
        #TODO: Error handling
        print("ERROR NEG IMP")
    formula = neg_formula.get_terms()[0]

    formula1 = formula.get_terms()[0].delete_negation()
    denied_formula2 = formula.get_terms()[1].deny_formula().delete_negation()
    labelled_formula1 = parser.LabelledFormula(node.get_label(), formula1)
    labelled_formula2 = parser.LabelledFormula(node.get_label(), denied_formula2)
    alpha_rule(node, tree, labelled_formula1, labelled_formula2)


def neg_know_rule(node: eptree.Node, tree: eptree.Tree):
    neg_formula = node.get_formula() #~Ka(A)
    component = node.get_formula().get_terms()[0] #Ka(A)
    result_formula = component.get_terms()[0].deny_formula().delete_negation()#~A
    agent = component.get_agent() #a

    if ((neg_formula.get_formula_type() != "not_know")):
        #TODO: Error handling
        print("ERROR neg K")
        return

    for leaf in tree.get_available_leafs(node):
        id = int(str(leaf.id)+str(1))
        lbranch = get_label_branch(tree.get_branch(leaf)) # Conjunto de etiquetas de la rama, en este caso node = leaf CUIDADO


        simple_branch = [] # Lista para despuéß simplificar la rama. 
        currentlabel = node.get_label() # Etiqueta del nodo al que vamos a aplicar la regla
        count = 1 # Contador para crear la nueva etiqueta
        new_label = None # INICIALIZAR VARIABLE PARA QUE NO SE PETE

        ## Bucle para construir el conjunto de etiquetas simplificado (IDEA > CREAR CLASE RAMA CON ESTOS DATOS)
        for label in lbranch:
            simple_branch.append(label.simplify_label())

        #Bucle para crear la extensión de la hoja del árbol
        for num in simple_branch:            
            new_label = currentlabel.append(agent,str(count))
            if new_label.simplify_label() == num:
                count += 1
        formula = parser.LabelledFormula(new_label,result_formula)
        leaf.add_one_child(formula, id)

def know_rule(node: eptree.Node, tree: eptree.Tree):
    formula = node.get_formula()
    term = formula.get_terms()[0]
    agent = node.get_formula().get_agent()
    label = node.get_label()
    extensions =[]
    if (formula.get_formula_type() != "know"):
        #TODO: Error handling
        print("ERROR K")
        return
    # VOY HASTA LA HOJA
    for leaf in tree.get_available_leafs(node):
        id = int(leaf.id)
        #COJO LA RAMA DESDE LA HOJA
        branch = tree.get_branch(leaf)
        labels = branch.get_label_branch()
        # COJO LOS LABELS Y LAS FILTRO
        extensions = branch.get_simple_extensions(label,labels)
        if extensions != None:
            for extlabel in extensions:
                # COMPRUEBO QU EL A EXTENSIÓN SEA LA DEL AGENTE DE LA FORMULA
                if extlabel.label[-3]==agent:
                    id = int(str(id)+str(1))
                    lformula = parser.LabelledFormula(extlabel,term)
                    leaf.add_one_child(lformula,id)
                else:
                    print("ERROR")
        else:
            #TODO: Error handling
            print("ERROR K")
            return
    return extensions




def get_label_branch(branch: list) -> list:
    labelbranchlist = []
    for i in branch:
        if (i.get_label().label not in labelbranchlist):
            labelbranchlist.append(i.get_label())
    return labelbranchlist




