import parser

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

    def __init__(self, labelled_formula: parser.LabelledFormula, left = None, right = None):
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
        return self.labelled_formula.get_labelled_formula()

    def add_one_child(self, data: parser.LabelledFormula):
        """ Add one child to the node. Is the node has only one child, it will be always the left one."""
        #HACK: Sobra comprobar si tiene hijo o no.
        if self.left is None:
            self.left = Node(data)
        else:
            self.left.add_one_child(data)

    def add_two_childs(self,data1,data2):
        """ Add two children to the node."""
        self.left = Node(data1)
        self.right = Node(data2)

    def get_childs(self) -> list:
        """Return a list wich contains the children of the node."""
        return [self.left,self.right]

class Tree:
    def __init__(self, root, left = None, right = None):
        self.root = Node(root)
        self.left = left
        self.right = right

    def simple_extension(self, data):
        """
        Insert function will insert a node on every leafs
        """
        for node in self.get_leafs(self.root):
            node.add_one_child(data)

    def double_extension(self,data1,data2):
        """
        Insert function will insert two childs on left child of the given node.
        """
        for node in self.get_leafs(self.root):
            node.add_two_childs(data1,data2)

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
            print(node.get_labelled_formula())
            self.preorder(node.left)
            self.preorder(node.right)



    # # QUEDA RARO QUE TE PIDA LA BRANCH. Problema de recursividad
    # def get_branch(self,root, target, branch): 
    #     """
    #     Return function will return the parent of the given node. 
    #     """
    #     if root == None: 
    #         return False
    #     if root == target: 
    #         branch.append(root)
    #         return True
    #     if (self.get_branch(root.left, target,branch) or self.get_branch(root.right, target, branch)): 
    #         branch.append(root) 
    #     return branch

    # # QUEDA RARO QUE TE PIDA LA BRANCH. Problema de recursividad
    # def get_node(self, node, key, list):
    #     """
    #     Return function will return the node that match with the key(str)
    #     """
    #     if node!=None:
    #         if node.data == key:
    #             list.append(node)
    #         else:
    #             self.get_node(node.left, key, list),
    #             if node==None:
    #                 self.get_node(node.right,key, list)
    #     return list

