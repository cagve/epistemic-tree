import itertools
import parser

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

class Tree:
    def __init__(self, root, left = None, right = None):
        self.root = Node(root,1)
        self.left = left
        self.right = right

    def simple_extension(self, data):
        """
        Insert function will insert a node on every leafs
        """
        for node in self.get_leafs(self.root):
            newid = int(str(node.id)+str(1))
            node.add_one_child(data, newid)

    def double_extension(self,data1,data2):
        """
        Insert function will insert two childs on left child of the given node.
        """
        for node in self.get_leafs(self.root):
            id1 = int(str(node.id)+str(1))
            id2 = int(str(node.id)+str(2))
            node.add_two_childs(data1,data2,id1,id2)

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

    def get_node_from_id(self, node, id):
        if(node != None):
            if id == node.id:
                return node 
            return self.get_node_from_id(node.left, id) or self.get_node_from_id(node.right, id)

    def get_branch(self,node):
        branch = Branch()
        id = node.id
        branch.append(node)
        while id!=1:
            id = int(str(id)[:-1])
            branch.append(self.get_node_from_id(self.root,id))
        return branch

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

class Branch(list):
    def is_close(self):
        flag = False
        for a,b in itertools.combinations(self,2): 
            if a.get_labelled_formula().get_contradiction(b.get_labelled_formula()):
                return True
        return False
    def print_branch(self):
        for i in self:
            print(i.get_labelled_formula())


