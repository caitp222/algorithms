# implement arbitrary binary tree and then write a method to determine if it is sorted
# if sorted:
# all nodes to the left of current node will be smaller than current node
# all nodes to the right of current node will be greater than current node

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node


def binary_tree_sorted(top_node):
    if top_node.left == None and top_node.right == None:
        return True
    elif top_node.left != None and top_node.left.data >= top_node.data:
        return False
    elif top_node.right != None and top_node.right.data < top_node.data:
        return False
    else:
        left = True
        right = True
        if top_node.left != None:
            left = binary_tree_sorted(top_node.left)
        if top_node.right != None:
            right = binary_tree_sorted(top_node.right)
        return left and right

# create binary tree
top_node = BinaryTreeNode(5)
top_node.insert_left(BinaryTreeNode(3))
top_node.left.insert_left(BinaryTreeNode(1))
top_node.left.insert_right(BinaryTreeNode(4))
top_node.insert_right(BinaryTreeNode(7))
top_node.right.insert_left(BinaryTreeNode(6))
top_node.right.insert_right(BinaryTreeNode(7))
print binary_tree_sorted(top_node) == True

top_node.right.right.insert_left(BinaryTreeNode(8))
print binary_tree_sorted(top_node) == False
