import itertools
from epistemictree import epmodel
from epistemictree import rules
from epistemictree import parser

COUNT = [10]
COUNT2 = [10]
class Node:
    """
    A class used to represent the nodes of the tree

    Attributes
    ----------
    labelled_formula: LabelledFormula
        The formula of the node 
    left: Node
        Left child 
    right: Node
        Right child

    Methods
    -------
    get_label()
    get_formula()
    get_labelled_formula()
    add_one_child(data: LabelledFormula) -> Node
    add_two_childs(data1,data2)
    def get_childs() -> list
    """

    def __init__(self, labelled_formula: parser.LabelledFormula, id: int, left = None, right = None):
        """
        Parameters
        ----------
        labelled_formula : LabelledFormula
            The formula of the node 
        left : Node
            Left child 
        right : Node
            Right child
        """
        self.id = id
        self.left = left
        self.right = right
        self.labelled_formula = labelled_formula

    def get_label(self) -> parser.Label:
        """ Return label of the labelled formula's node """
        return self.labelled_formula.label

    def get_formula(self) -> parser.Formula:
        """ Return formula of the labelled formula's node """
        return self.labelled_formula.formula

    def get_labelled_formula(self) -> parser.LabelledFormula:
        """ Return labelled formula"""
        return self.labelled_formula

    def get_labelled_formula_string(self) -> parser.LabelledFormula:
        """ Return labelled formula"""
        return self.labelled_formula.to_string()

    def get_id(self):
        return self.id

    def add_one_child(self, data: parser.LabelledFormula, id):
        """ Add one child to the node. Is the node has only one child, it will be always the left one."""
        #HACK: Sobra comprobar si tiene hijo o no.
        if self.left is None:
            self.left = Node(data, id)
        else:
            self.left.add_one_child(data, id)

    def add_two_childs(self,data1,data2,id1, id2):
        """ Add two children to the node."""
        self.left = Node(data1,id1)
        self.right = Node(data2,id2)

    def get_childs(self) -> list:
        """Return a list wich contains the children of the node."""
        return [self.left,self.right]

    def get_rule(self):
        type = self.get_formula().get_formula_type()
        return rules.formula_rules[type]

    def get_rule_type(self):
        rule = self.get_rule()
        return rules.type_rules.get(rule)

    def apply_rule(self, tree):
        tree.add_knows_to_group(tree.root,tree)
        type = self.get_formula().get_formula_type()
        rules.formula_functions[type](self, tree)

class Tree:
    def __init__(self, root = None, left = None, right = None):
        self.root = Node(root,1)
        self.left = left
        self.right = right
        self.label_group = []
        self.alpha_group = []
        self.beta_group = []
        self.nu_group = []
        self.pi_group = []


    def simple_extension(self, data):
        """
        Insert function will insert a node on every leafs
        """
        for node in self.get_leafs(self.root):
            newid = int(str(node.id)+str(1))
            node.add_one_child(data, newid)
            self.add_node_to_group(node.left)

    def double_extension(self,data1,data2):
        """
        Insert function will insert two childs on left child of the given node.
        """
        for node in self.get_leafs(self.root):
            id1 = int(str(node.id)+str(1))
            id2 = int(str(node.id)+str(2))
            node.add_two_childs(data1,data2,id1,id2)

    def create_tree(self,  conclusion:parser.Formula, premises=None):
        label = parser.Label('1')
        conclusion_node= Node(parser.LabelledFormula(label,conclusion.deny_formula().delete_negation()),1)
        self.root=conclusion_node
        self.add_node_to_group(self.root)
        if premises !=None:
            for formula in premises:
                lformula = parser.LabelledFormula(label,formula)
                self.simple_extension(lformula)


    def get_leafs(self, node: Node, leafs=None) -> list:
        """
        Return list of nodes. If node != root, return leafs of a branch.
        """
        if leafs == None:
            leafs = []

        if node is None:
            print("Empty tree")
        if(node.left is None and node.right is None):
            leafs.append(node)
        else:
            self.get_leafs(node.left,leafs) 
            if node.right is not None:
                self.get_leafs(node.right,leafs)
        return leafs

    def count_leafs(self, node) -> int:
        """
        Return the numbers of leafs. If node != root, return leafs of a branch.
        """
        # TODO: si una rama está cerrada que no devuelva el último término
        if node is None:
            return  0
        if(node.left is None and node.right is None):
            return  1
        else:
            if node.right is not None:
                return self.count_leafs(node.left) + self.count_leafs(node.right)
            else: 
                return self.count_leafs(node.left) 

    def preorder(self,node):
        if node:
            if(node != None):
                print(node.get_labelled_formula_string())
                self.preorder(node.left)
                self.preorder(node.right)

    def dot_id(self,node,file):
        if node:
            if(node != None):
                if(node.left != None):
                    file.write(str(node.id)+' -> '+str(node.left.id)+';\n')
                if(node.right != None):
                    file.write(str(node.id)+' -> '+str(node.right.id)+';\n')
                self.dot_id(node.left,file)
                self.dot_id(node.right,file)

    def dot_formula(self,node,file):
        if node:
            if(node != None):
                formula = node.get_labelled_formula_string().replace('=>','→').replace('&&','∧').replace('||','∨')
                # file.write(str(node.id)+'[label=< <FONT POINT-SIZE="10">'+str(node.id)+'<BR/></FONT><FONT POINT-SIZE="20">'+formula+'</FONT> >];\n')
                file.write(str(node.id)+'[label="'+formula+'"];\n')
                self.dot_formula(node.left,file)
                self.dot_formula(node.right,file)

    def print_dot(self,node):
        file = open("/home/karu/tree.dot", 'w')
        file.write("digraph G {\n")
        file.write('node[shape = none]\n')
        self.dot_formula(node,file)
        self.dot_id(node, file)
        file.write("}")
        file.close

    def get_node_from_id(self, node:Node, id:int):
        if(node != None):
            if id == node.id:
                return node 
            return self.get_node_from_id(node.left, id) or self.get_node_from_id(node.right, id)

    def get_full_branch(self,node) -> list:
        ''' Obtiene todas las ramas de un nodo'''
        leafs = self.get_leafs(node)
        extension = []
        for leaf in leafs:
            branch = self.get_branch(leaf)
            extension.append(branch)
        return extension

    def get_branch(self,node):
        branch = Branch()
        id = node.id
        branch.append(node)
        while id!=1:
            id = int(str(id)[:-1])
            branch.append(self.get_node_from_id(self.root,id))
        return branch

    def get_available_leafs(self, node):
        ava_branchs = []
        ava_leafs = []
        leafs = self.get_leafs(node)
        for leaf in leafs:
            branch = self.get_branch(leaf)
            if branch.is_close():
                print("Branch of " + leaf.get_labelled_formula_string() + " is close")
            else: 
                ava_branchs.append(branch)
                ava_leafs.append(leaf)
        return ava_leafs

    def print_open_close_branchs(self):
        branchs = self.get_full_branch(self.root)
        close_branchs = list(filter(lambda branch: branch.is_close(), branchs))
        open_branchs = list(filter(lambda branch: not branch.is_close(), branchs))
        for branch in close_branchs:
            formula = parser.Formula('')
            label = parser.Label('')
            lf = parser.LabelledFormula(label,formula)
            leaf = branch[0]
            id = int(str(leaf.id)+str(1))
            leaf.add_one_child(lf,id)

        for branch in open_branchs:
            formula = parser.Formula('')
            label = parser.Label('')
            lf = parser.LabelledFormula(label,formula)
            leaf = branch[0]
            id = int(str(leaf.id)+str(1))
            leaf.add_one_child(lf,id)

    def print_tree(self, root, space):
        if (root == None):
            return False

        space += COUNT[0]
        self.print_tree(root.right, space)
        print()
        for i in range(COUNT[0], space):
            print(end = " ")
        # print(root.id, end = " ")
        print(root.get_labelled_formula_string())
        self.print_tree(root.left, space)

    def print_label_tree(self, node, space):
        if (node == None):
            return False

        space += COUNT2[0]
        self.print_label_tree(node.right, space)
        print()
        for i in range(COUNT[0], space):
            print(end = " ")
        print(node.id)
        self.print_label_tree(node.left, space)

    def check_node_know_alive(self,node, tree):
        available = []
        if node.get_rule_type() == 'nu':
            agent = node.get_formula().get_agent()
            branchs = self.get_full_branch(node)
            # AÑADE LAS EXTENSIONES SIMPLES
            for branch in branchs: 
                agent_extensions = branch.get_extensions_agent(agent,node.get_label()) 
                if agent_extensions is not None:
                    for extension in agent_extensions:
                        formula = parser.LabelledFormula(extension,node.get_formula().get_terms()[0])
                        if not branch.formula_in_branch(formula):
                            available.append(extension)
            if available:
                return True
            else:
                return False

    def add_knows_to_group(self,node, tree, nu_group=None):
        if nu_group == None:
            nu_group = []

        if node:
            if(node != None):
                if self.check_node_know_alive(node, tree):
                    nu_group.append(node)
                self.add_knows_to_group(node.left,tree,nu_group)
                self.add_knows_to_group(node.right,tree,nu_group)
        self.nu_group = nu_group


    def add_node_to_group(self,node: Node):
        self.add_knows_to_group(self.root, self)
        if node.get_rule_type() == 'alpha':
            self.alpha_group.append(node)
        elif node.get_rule_type() == 'beta':
            self.beta_group.append(node)
        elif node.get_rule_type() == 'pi':
            self.pi_group.append(node)
        # elif node.get_rule_type() =='literal':
        #     print("Es un literal")
        # else:
            # print("error add_node_from_group")

    def remove_node_from_group(self, node:Node):
        if node.get_rule_type() == 'alpha':
            self.alpha_group.remove(node)
        elif node.get_rule_type() == 'beta':
            self.beta_group.remove(node)
        # elif node.get_rule_type() == 'nu':
        #     self.nu_group.remove(node)
        elif node.get_rule_type() == 'pi':
            self.pi_group.remove(node)
        elif node.get_rule_type() =='literal':
            return 
        else:
            return 

    def get_open_branchs(self) -> list:
        branchs = self.get_full_branch(self.root)
        open_branchs = list(filter(lambda branch: not branch.is_close(), branchs))
        return open_branchs
    
    def open_branch(self):
        return len(self.get_open_branchs()) != 0

    def create_counter_model(self):
        counter_models = []
        if not self.open_branch():
            print("Closed tree")
            return

        open_branchs = self.get_open_branchs()

        branch = open_branchs[0]
        labelbranch = branch.get_label_branch()
        modelo = epmodel.Model()
        for label in labelbranch:
            modelo.add_world(epmodel.World(str(label.simplify_label())))
            # ADD EVALUATION ONLY LITERAL
            world = epmodel.World(str(label.simplify_label()))
            world.add_true_formula_list(filter(lambda x: x.is_literal(), branch.get_formulas_label(label)))
            modelo.add_world(world)
            if branch.get_simple_extensions(label) !=None:
                for ext in branch.get_simple_extensions(label):
                    agent=ext.get_agent()
                    world1 = epmodel.World(str(label.simplify_label()))
                    world2 = epmodel.World(str(ext.simplify_label()))
                    relation = epmodel.Relation(world1,world2,agent) 
                    modelo.add_relation(relation)
        counter_models.append(modelo)
        # for branch in open_branchs:
        #     branch = open_branchs[0]
        #     labelbranch = branch.get_label_branch()
        #     modelo = epmodel.Model()
        #     for label in labelbranch:
        #         modelo.add_world(epmodel.World(str(label.simplify_label())))
        #         # ADD EVALUATION ONLY LITERAL
        #         world = epmodel.World(str(label.simplify_label()))
        #         world.add_true_formula_list(filter(lambda x: x.is_literal(), label.get_formulas(self.root)))
        #         modelo.add_world(world)
        #         if branch.get_simple_extensions(label) !=None:
        #             for ext in branch.get_simple_extensions(label):
        #                 agent=ext.get_agent()
        #                 world1 = epmodel.World(str(label.simplify_label()))
        #                 world2 = epmodel.World(str(ext.simplify_label()))
        #                 relation = epmodel.Relation(world1,world2,agent) 
        #                 modelo.add_relation(relation)
        #     counter_models.append(modelo)
        return counter_models



class Branch(list):
    def is_close(self):
        for a,b in itertools.combinations(self,2): 
            if a.get_labelled_formula().get_contradiction(b.get_labelled_formula()) or b.get_labelled_formula().get_contradiction(a.get_labelled_formula()):
                return True
        return False

    def print_branch(self):
        for i in self:
            print(i.get_labelled_formula_string())

    def get_label_branch(self):
        labels = []
        for node in self:
            labels.append(node.get_label())
        return set(labels)

    def get_formulas_label(self, label):
        formulas = []
        for node in self:
            if node.get_label().label == label.label:
                formulas.append(node.get_formula())
        return formulas

    # TODO AÑADIR IR A HOJA
    def get_simple_extensions(self,  label_filter, label_branch=None,):
        extensions = []
        if label_branch==None:
            label_branch = self.get_label_branch()

        for label in label_branch:
            if label.is_simple_extension(label_filter):
                extensions.append(label)

        if len(extensions)==0:
            return None
        else:
            return extensions
            
    def get_extensions_agent(self, agent, label_filter, label_branch=None):
        extensions = self.get_simple_extensions(label_filter)
        if extensions != None:
            for extension in extensions:
                if extension.label[-3] != agent:
                    extensions.remove(extension)
        return extensions

    def formula_in_branch(self, formula: parser.LabelledFormula):
        for node in self:
            if node.get_labelled_formula_string() == formula.to_string():
                return True
        return False 

