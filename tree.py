class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_one_child(self, data):
        if self.left is None:
            self.left = Node(data)
            return self.left
        else:
            self.left.insert_one_child(data)

    def insert_two_childs(self,data1,data2):
        self.left = Node(data1)
        self.right = Node(data2)

class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def create_node(self,data):
        """
        Create node
        """
        return Node(data)

    def insert_one_child(self, node, data):
        """
        Insert function will insert only one child on left child of the given node
        """
        if node.left is None:
            node.left = self.create_node(data)
            return node.left
        else:
            node.left.add_one_child(data)

    def insert_two_childs(self,node,data1,data2):
        """
        Insert function will insert two childs on left child of the given node.
        """
        node.left = self.create_node(data1)
        node.right = self.create_node(data2)
        return node.left, node.right


    # QUEDA RARO QUE TE PIDA LA BRANCH. Problema de recursividad
    def get_branch(self,root, target, branch): 
        """
        Return function will return the parent of the given node. 
        """
        if root == None: 
            return False
        if root == target: 
            branch.append(root)
            return True
        if (self.get_branch(root.left, target,branch) or self.get_branch(root.right, target, branch)): 
            branch.append(root) 
        return branch

    # QUEDA RARO QUE TE PIDA LA BRANCH. Problema de recursividad
    def get_node(self, node, key, list):
        """
        Return function will return the node that match with the key(str)
        """
        if node!=None:
            if node.data == key:
                list.append(node)
            else:
                self.get_node(node.left, key, list),
                if node==None:
                    self.get_node(node.right,key, list)
        return list

tree = Tree("1")
node1 = tree.root
node2,node3 = tree.insert_two_childs(node1,"2","3")
node4 = tree.insert_one_child(node2,"4")
node5 = tree.insert_one_child(node4,"5")
node6,node7 = tree.insert_two_childs(node5,"6","7")
node8,node9 = tree.insert_two_childs(node3,"8","9")
node10 = tree.insert_one_child(node8,"10")


list = []

