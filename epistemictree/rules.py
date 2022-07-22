from epistemictree import parser
from time import sleep
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

def get_formula_rule(formula: parser.LabelledFormula):
    type = formula.formula.get_formula_type()
    return formula_rules.get(type)

def alpha_rule(node: eptree.Node, tree: eptree.Tree, term1: parser.LabelledFormula, term2: parser.LabelledFormula):
    leafs = tree.get_available_leafs(node)
    tree.remove_node_from_group(node)
    if leafs:
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
    if leafs: 
        for leaf in leafs:
            id1 = int(str(leaf.id)+str(1))
            id2 = int(str(leaf.id)+str(2))
            leaf.add_two_childs(term1, term2,id1,id2)
            tree.add_node_to_group(leaf.left)
            tree.add_node_to_group(leaf.right)

# ALPHA RULES
def conjunction_rule(node: eptree.Node, tree: eptree.Tree, system):
    print("Aplicando regla de conjunción en nodo "+ str(node.id)+ " > formula "+ str(node.get_labelled_formula_string()))
    formula = node.get_formula()
    if formula.get_formula_type() != "and":
        #TODO: Error handling
        print("ERROR CON ")
    labelled_formula1 = parser.LabelledFormula(node.get_label(), formula.get_terms()[0].delete_negation())
    labelled_formula2 = parser.LabelledFormula(node.get_label(), formula.get_terms()[1].delete_negation())
    alpha_rule(node, tree, labelled_formula1, labelled_formula2)

def not_conjunction_rule(node: eptree.Node, tree: eptree.Tree, system):    
    print("Aplicando regla de not conjunción en nodo "+ str(node.id)+ " > formula "+ str(node.get_labelled_formula_string()))
    neg_formula = node.get_formula()
    if neg_formula.get_formula_type() != "not_and":
        print("ERROR NEG CON")

    formula = neg_formula.get_terms()[0]

    denied_formula1 = formula.get_terms()[0].deny_formula().delete_negation()
    denied_formula2 = formula.get_terms()[1].deny_formula().delete_negation()

    labelled_formula1 = parser.LabelledFormula(node.get_label(), denied_formula1)
    labelled_formula2 = parser.LabelledFormula(node.get_label(), denied_formula2)
    beta_rule(node, tree, labelled_formula1, labelled_formula2)

def disjunction_rule(node: eptree.Node, tree: eptree.Tree,system):
    formula = node.get_formula()
    if formula.get_formula_type() != "or":
        print("ERROR DIS")
    labelled_formula1 = parser.LabelledFormula(node.get_label(), formula.get_terms()[0].delete_negation())
    labelled_formula2 = parser.LabelledFormula(node.get_label(), formula.get_terms()[1].delete_negation())
    beta_rule(node, tree, labelled_formula1, labelled_formula2)

def not_disjunction_rule(node: eptree.Node, tree: eptree.Tree, system):
    neg_formula = node.get_formula()
    if neg_formula.get_formula_type() != "not_or":
        print("ERROR NEG DIS")
    formula = neg_formula.get_terms()[0]

    denied_formula1 = formula.get_terms()[0].deny_formula().delete_negation()
    denied_formula2 = formula.get_terms()[1].deny_formula().delete_negation()
    labelled_formula1 = parser.LabelledFormula(node.get_label(), denied_formula1)
    labelled_formula2 = parser.LabelledFormula(node.get_label(), denied_formula2)
    alpha_rule(node, tree, labelled_formula1, labelled_formula2)

def implication_rule(node: eptree.Node, tree: eptree.Tree, system):
    print("Aplicando regla de imp en nodo "+ str(node.id)+ " > formula "+ str(node.get_labelled_formula_string()))
    formula = node.get_formula()
    if formula.get_formula_type() != "iff":
        print("ERROR IMP")
    denied_formula1 = formula.get_terms()[0].deny_formula().delete_negation()
    formula2 = formula.get_terms()[1].delete_negation()
    labelled_formula1 = parser.LabelledFormula(node.get_label(), denied_formula1)
    labelled_formula2 = parser.LabelledFormula(node.get_label(), formula2)
    beta_rule(node,tree,labelled_formula1, labelled_formula2)

def not_implication_rule(node: eptree.Node, tree: eptree.Tree, system):
    print("Aplicando regla de not imp en nodo "+ str(node.id)+ " > formula "+ str(node.get_labelled_formula_string()))
    neg_formula = node.get_formula()
    if neg_formula.get_formula_type() != "not_iff":
        print("ERROR NEG IMP")
    formula = neg_formula.get_terms()[0]

    formula1 = formula.get_terms()[0].delete_negation()
    denied_formula2 = formula.get_terms()[1].deny_formula().delete_negation()
    labelled_formula1 = parser.LabelledFormula(node.get_label(), formula1)
    labelled_formula2 = parser.LabelledFormula(node.get_label(), denied_formula2)
    alpha_rule(node, tree, labelled_formula1, labelled_formula2)

def not_know_rule( node: eptree.Node, tree: eptree.Tree, system):
    print("Aplicando regla de not know en nodo "+ str(node.id)+ " > formula "+ str(node.get_labelled_formula_string()))
    neg_formula = node.get_formula() #~Ka(A)
    component = node.get_formula().get_terms()[0] #Ka(A)
    result_formula = component.get_terms()[0].deny_formula().delete_negation()#~A
    agent = component.get_agent() #a
    tree.remove_node_from_group(node)

    if ((neg_formula.get_formula_type() != "not_know")):
        print("ERROR neg K")
        return

    leafs = tree.get_available_leafs(node)
    if not leafs:
        print("not available leafs")
        return 
    else:
        for leaf in leafs:
            id = int(str(leaf.id)+str(1))
            branch = tree.get_branch(leaf)
            if ("4" in system and node.get_label().is_superfluo(branch)):
                print(system)
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
                # SYSTEM K4
                if system == "k4":
                    if new_label.simplify_label() == num or new_label.is_superfluo(branch):
                        count += 1
                else:
                    if new_label.simplify_label() == num:
                        count += 1
            if new_label:
                formula = parser.LabelledFormula(new_label,result_formula)
                leaf.add_one_child(formula, id)
                tree.add_node_to_group(leaf.left)
            else:
                print("Not new label")

def know_rule(node: eptree.Node, tree: eptree.Tree, system):
    print("Aplicando regla de know en nodo "+ str(node.id)+ " > formula "+ str(node.get_labelled_formula_string()))
    formula = node.get_formula()
    term = formula.get_terms()[0].delete_negation()
    agent = node.get_formula().get_agent()
    label = node.get_label()
    extensions =[]
    tree.remove_node_from_group(node)
    if (formula.get_formula_type() != "know"):
        #TODO: Error handling
        print("ERROR K")
        return
    # VOY HASTA LA HOJA
    leafs = tree.get_available_leafs(node)
    if leafs == None:
        print("No hojas libres")
        return
    for leaf in leafs:
        id = int(leaf.id)
        #COJO LA RAMA DESDE LA HOJA
        branch = tree.get_branch(leaf)
        labels = branch.get_label_branch()
        # S4
        if "t" in system:
            print("Aplicando s4")
            id = int(str(id)+str(1))
            labelled_formula = parser.LabelledFormula(label, term)
            if branch.formula_in_base_set(label ,term):
                print("La fórmula "+term.formula+" está en el conjunto base "+label.label)
            else:
                leaf.add_one_child(labelled_formula,id)
                print("[New Node] " + leaf.left.get_labelled_formula_string())
                tree.add_node_to_group(leaf.left)
                leaf = leaf.left

        extensions = branch.get_simple_extensions(label,labels)
        if extensions != None:
            for extlabel in extensions:
                if extlabel.label[-3]==agent:
                    id = int(str(id)+str(1))
                    lformula = parser.LabelledFormula(extlabel,term)
                    if branch.formula_in_base_set(extlabel,term):
                        print("ESTÁ DENTRO")
                        continue
                    leaf.add_one_child(lformula,id)
                    tree.add_node_to_group(leaf.left)
                    if "4" in system:
                        print("Aplicando 4")
                        print(leaf.get_labelled_formula_string())
                        id = int(str(id)+str(1))
                        kformula = parser.LabelledFormula(extlabel,formula)
                        if branch.formula_in_base_set(extlabel,term):
                            print("ESTÁ DENTRO")
                            continue
                        leaf.left.add_one_child(kformula,id)
                        tree.add_node_to_group(leaf.left.left)
        else:
            print("Not extensions")
            continue
    # tree.add_knows_to_group(tree.root)
    return extensions

# Ahora mismo satura primero las etiquetas y después divide ramas.
def rule_algorithm(system,tree):
    while True:
        # tree.add_knows_to_group(tree.root,tree)
        tree.add_knows_to_group(tree.root,tree)
        print("-----------------------Paso---------------------")
        if tree.alpha_group:
            apply_rule(system, tree.alpha_group[0],tree)
        elif tree.nu_group:
            apply_rule(system, tree.nu_group[0],tree)
        elif tree.pi_group:
            apply_rule(system, tree.pi_group[0],tree)
        elif tree.beta_group: 
            apply_rule(system, tree.beta_group[0],tree)
        else:
            return False
        return rule_algorithm(system, tree)
    
def apply_rule(system, node: eptree.Node, tree):
    type = node.get_formula().get_formula_type()
    formula_functions[type](node, tree, system)
    # print("Aplicando regla "+str(formula_functions[type])+ " en nodo "+ str(node.id)+ " > formula "+ str(node.get_labelled_formula_string()))
     


def run_tableau(system, conclusion, premisas):
    tree = eptree.Tree()
    lista_premisas = []
    model = None
    if premisas:
        for premisa in premisas:
            formula = parser.Formula(premisa)
            lista_premisas.append(formula)

    formula = parser.Formula(conclusion)
    tree.create_tree(formula,lista_premisas)
    rule_algorithm(system, tree)
    tree.print_dot(tree.root)
    os.system('dot -Tpng ~/tree.dot > ~/tree.png')
    if tree.open_branch():
        model = tree.create_counter_model()
        if "4" in system:
            print("Aplicando loop checking")
            tree.loop_checking(model[0])
            model[0].transitive_closure('a')
        else:
            print("No aplicar loop checking")
        model[0].print_dot()
        os.system('dot -Tpng ~/model.dot > ~/model.png')
        tree.print_open_close_branchs()
        return(True,tree, model[0])
    else: 
        print("No model")
        tree.print_open_close_branchs()
        return(False, tree, None)

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


