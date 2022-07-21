from epistemictree import parser
from epistemictree import eptree 
import os

type_rules = {
        'conjunction_rule':'alpha', 
        'disjunction_rule':'beta', 
        'implication_rule':'beta',
        'know_rule':'nu',
        'not_conjunction_rule':'beta',
        'not_disjunction_rule':'alpha',
        'not_implication_rule':'alpha',
        'not_know_rule':'pi',
        'literal': 'literal'

    }

formula_rules = {
        'and':'conjunction_rule',
        'or':'disjunction_rule', 
        'iff':'implication_rule',
        'know':'know_rule',
        'not_and':'not_conjunction_rule',
        'not_or':'not_disjunction_rule',
        'not_iff':'not_implication_rule',
        'not_know':'not_know_rule',
        'atom':'literal',
        'not_atom':'literal'
    }

def get_rule(node: eptree.Node):
    """Return the node formula of the gi"""
    type = node.get_formula().get_formula_type()
    return formula_rules[type]

def get_rule_type(node: eptree.Node):
    rule = get_rule(node)
    return type_rules.get(rule)

def apply_rule(node: eptree.Node, tree):
    tree.add_knows_to_group(tree.root,tree)
    type = node.get_formula().get_formula_type()
    formula_functions[type](node, tree)

def get_formula_rule(formula: parser.LabelledFormula):
    type = formula.formula.get_formula_type()
    return formula_rules.get(type)

def alpha_rule(node: eptree.Node, tree: eptree.Tree, term1: parser.LabelledFormula, term2: parser.LabelledFormula):
    leafs = tree.get_available_leafs(node)
    tree.remove_node_from_group(node)
    for leaf in leafs:
        id1 = int(str(leaf.id)+str(1))
        id2 = int(str(leaf.id)+str(11))
        leaf.add_one_child(term1,id1)
        tree.add_node_to_group(leaf.left)
        if not tree.get_branch(leaf.left).is_close():
            leaf.left.add_one_child(term2,id2)
            tree.add_node_to_group(leaf.left.left)


def beta_rule(node: eptree.Node, tree: eptree.Tree, term1: parser.LabelledFormula, term2: parser.LabelledFormula):
    leafs = tree.get_available_leafs(node)
    tree.remove_node_from_group(node)
    for leaf in leafs:
        id1 = int(str(leaf.id)+str(1))
        id2 = int(str(leaf.id)+str(2))
        leaf.add_two_childs(term1, term2,id1,id2)
        tree.add_node_to_group(leaf.left)
        tree.add_node_to_group(leaf.right)

# ALPHA RULES
def conjunction_rule(node: eptree.Node, tree: eptree.Tree):
    formula = node.get_formula()
    if formula.get_formula_type() != "and":
        #TODO: Error handling
        print("ERROR CON ")
    labelled_formula1 = parser.LabelledFormula(node.get_label(), formula.get_terms()[0].delete_negation())
    labelled_formula2 = parser.LabelledFormula(node.get_label(), formula.get_terms()[1].delete_negation())
    alpha_rule(node, tree, labelled_formula1, labelled_formula2)

def not_conjunction_rule(node: eptree.Node, tree: eptree.Tree):    
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

def not_disjunction_rule(node: eptree.Node, tree: eptree.Tree):
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

def not_implication_rule(node: eptree.Node, tree: eptree.Tree):
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

def not_know_rule(node: eptree.Node, tree: eptree.Tree):
    neg_formula = node.get_formula() #~Ka(A)
    component = node.get_formula().get_terms()[0] #Ka(A)
    result_formula = component.get_terms()[0].deny_formula().delete_negation()#~A
    agent = component.get_agent() #a
    tree.remove_node_from_group(node)

    if ((neg_formula.get_formula_type() != "not_know")):
        #TODO: Error handling
        print("ERROR neg K")
        return

    if not tree.get_available_leafs(node):
        print("not ava leafs")
        return

    for leaf in tree.get_available_leafs(node):
        id = int(str(leaf.id)+str(1))
        branch = tree.get_branch(leaf)
        lbranch = branch.get_label_branch() # Conjunto de etiquetas de la rama, en este caso node = leaf CUIDADO

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
        tree.add_node_to_group(leaf.left)

def not_know_rule_4(node: eptree.Node, tree: eptree.Tree):
    neg_formula = node.get_formula() #~Ka(A)
    component = node.get_formula().get_terms()[0] #Ka(A)
    result_formula = component.get_terms()[0].deny_formula().delete_negation()#~A
    agent = component.get_agent() #a
    tree.remove_node_from_group(node)

    if ((neg_formula.get_formula_type() != "not_know")):
        #TODO: Error handling
        print("ERROR neg K")
        return

    if not tree.get_available_leafs(node):
        print("not ava leafs")
        return

    for leaf in tree.get_available_leafs(node):
        id = int(str(leaf.id)+str(1))
        branch = tree.get_branch(leaf)
        if (node.get_label().is_superfluo(branch)):
            print("Es superfluo")
            return 
        lbranch = branch.get_label_branch() # Conjunto de etiquetas de la rama, en este caso node = leaf CUIDADO

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
            if new_label.simplify_label() == num or new_label.is_superfluo(branch):
                count += 1
        formula = parser.LabelledFormula(new_label,result_formula)
        leaf.add_one_child(formula, id)
        tree.add_node_to_group(leaf.left)

def know_rule(node: eptree.Node, tree: eptree.Tree):
    formula = node.get_formula()
    term = formula.get_terms()[0]
    agent = node.get_formula().get_agent()
    label = node.get_label()
    extensions =[]
    tree.remove_node_from_group(node)
    if (formula.get_formula_type() != "know"):
        #TODO: Error handling
        print("ERROR K")
        return

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
                    tree.add_node_to_group(leaf.left)
        else:
            #TODO: Error handling
            print("ERROR K")
            return
    tree.add_knows_to_group(tree.root, tree)
    return extensions


def know_rule_4(node: eptree.Node, tree: eptree.Tree):
    formula = node.get_formula()
    agent = node.get_formula().get_agent()
    label = node.get_label()
    extensions =[]
    tree.remove_node_from_group(node)
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
                    lformula = parser.LabelledFormula(extlabel,formula)
                    leaf.add_one_child(lformula,id)
                    tree.add_node_to_group(leaf.left)
        else:
            #TODO: Error handling
            print("ERROR K")
            return
    tree.add_knows_to_group(tree.root, tree)
    return extensions

def rule_algorithm(tree: eptree.Tree):
    while True:
        if not tree.get_available_leafs(tree.root):
            return False
        if tree.alpha_group:
            apply_rule(tree.alpha_group[0],tree)
        elif tree.pi_group:
            apply_rule(tree.pi_group[0],tree)
        elif tree.nu_group:
            apply_rule(tree.nu_group[0],tree)
        elif tree.beta_group: 
            apply_rule(tree.beta_group[0],tree)
        else:
            return False
        return rule_algorithm(tree)
    
def run_system(tree):
    while True:
        if tree.alpha_group:
            apply_rule_c(tree.alpha_group[0],tree)
        elif tree.nu_group:
            apply_rule_c(tree.nu_group[0],tree)
        elif tree.pi_group:
            apply_rule_c(tree.pi_group[0],tree)
        elif tree.beta_group: 
            apply_rule_c(tree.beta_group[0],tree)
        else:
            return False
        return run_system(tree)
    
def apply_rule_c(node: eptree.Node, tree):
    print("Aplicando regla en nodo "+ str(node.id))
    print(node.get_labelled_formula_string())
    tree.add_knows_to_group(tree.root,tree)
    type = node.get_formula().get_formula_type()
    for i in formula_functions_k4[type]:
        i(node, tree)

def run_tableau(conclusion, premisas):
    tree = eptree.Tree()
    lista_premisas = []
    if premisas:
        for premisa in premisas:
            formula = parser.Formula(premisa)
            lista_premisas.append(formula)

    formula = parser.Formula(conclusion)
    tree.create_tree(formula,lista_premisas)
    rule_algorithm(tree)
    if tree.open_branch():
        model = tree.create_counter_model()
        model[0].print_dot()
        os.system('dot -Tpng ~/model.dot > ~/model.png')
    tree.print_open_close_branchs()
    tree.print_dot(tree.root)
    os.system('dot -Tpng ~/tree.dot > ~/tree.png')
    return(tree.open_branch())

def know4_rule(node, i):
    print("REGLA 4")


    
formula_functions_k4 = {
        'and':[conjunction_rule],
        'or':[disjunction_rule], 
        'iff':[implication_rule],
        'know':[know_rule, know_rule_4],
        'not_and':[not_conjunction_rule],
        'not_or':[not_disjunction_rule],
        'not_iff':[not_implication_rule],
        'not_know':[not_know_rule_4]
        }

formula_functions = {
        'and':conjunction_rule,
        'or':disjunction_rule, 
        'iff':implication_rule,
        'know':know_rule,
        'not_and':not_conjunction_rule,
        'not_or':not_disjunction_rule,
        'not_iff':not_implication_rule,
        'not_know':not_know_rule
    }


