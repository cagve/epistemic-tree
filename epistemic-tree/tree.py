class Node:
    def __init__(self, labelled_formula, left = None, right = None):
        self.left = left
        self.right = right
        self.labelled_formula = labelled_formula

    def get_label(self):
        return self.labelled_formula.label

    def get_formula(self):
        return self.labelled_formula.formula

    def get_labelled_formula(self):
        return self.labelled_formula.get_labelled_formula()

    def add_one_child(self, data):
        if self.left is None:
            self.left = Node(data)
            return self.left
        else:
            self.left.add_one_child(data)

    def add_two_childs(self,data1,data2):
        self.left = Node(data1)
        self.right = Node(data2)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.labelled_formula.get_labelled_formula()),
        if self.right:
            self.right.print_tree()
 
    def get_childs(self):
        return [self.left,self.right]

class Tree:
    def __init__(self, root, left = None, right = None):
        self.root = Node(root)
        self.left = left
        self.right = right

    def create_node(self,data):
        """
        Create node
        """
        return Node(data)

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

    def get_leafs(self, node, leafs=None):
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

    def count_leafs(self, node):
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

# tree = Tree("1")
# node1 = tree.root
# node2,node3 = tree.insert_two_childs(node1,"2","3")
# node4 = tree.insert_one_child(node2,"4")
# node5 = tree.insert_one_child(node4,"5")
# node6,node7 = tree.insert_two_childs(node5,"6","7")
# node10 = tree.insert_one_child(node8,"10")
# node8,node9 = tree.insert_two_childs(node3,"8","9")


