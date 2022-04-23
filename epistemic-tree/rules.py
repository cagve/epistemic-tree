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

def neg_know_rule(node: eptree.Node, tree: eptree.Tree):
    neg_formula = node.get_formula() #~Ka(A)
    component = node.get_formula().get_terms()[0] #Ka(A)
    result_formula = component.get_terms()[0].deny_formula()#~A
    agent = component.get_agent() #a

    if ((neg_formula.get_formula_type() != "not") or (neg_formula.get_terms()[0].get_formula_type() != "know")):
        #TODO: Error handling
        print("ERROR")
        return

    for leaf in tree.get_leafs(node):
        id = leaf.id.copy()
        id.append(1) # EL ARBOL BINARIO LO CREO AÑADIENDO 1 PORQUE NO EXTIENDE

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
        node.add_one_child(formula, id)

def get_label_branch(branch: list) -> list:
    labelbranchlist = []
    for i in branch:
        if (i.get_label().label not in labelbranchlist):
            labelbranchlist.append(i.get_label())
    return labelbranchlist




