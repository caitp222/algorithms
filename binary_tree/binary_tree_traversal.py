# http://interactivepython.org/runestone/static/pythonds/Trees/NodesandReferences.html
# http://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/

class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def insert_left(self, data):
    if self.left == None:
      self.left = BinaryTreeNode(data)
    else:
      self.left.insert_left(data)

  def insert_right(self, data):
    if self.right == None:
      self.right = BinaryTreeNode(data)
    else:
      self.right.insert_right(data)

  def inorder_traversal_iterative(self):
      current_node = self
      nodes = []
      while len(nodes) >= 1 or current_node != None:
          if current_node != None:
              nodes.append(current_node)
              current_node = current_node.left
          else:
              current_node = nodes[-1]
              del(nodes[-1])
              print current_node.data
              current_node = current_node.right

  def inorder_traversal_recursive(self):
      if self == None:
          return
      if self.left != None:
          self.left.inorder_traversal_recursive()
      print self.data
      if self.right != None:
          self.right.inorder_traversal_recursive()

  def preorder_traversal_iterative(self):
      pass

  def preorder_traversal_recursive(self):
      print self.data
      if self.left:
          self.left.preorder_traversal()
      if self.right:
          self.right.preorder_traversal()

  def postorder_traversal_iterative(self):
      pass

  def postorder_traversal_recursive(self):
      pass


# build tree
tree = BinaryTreeNode(1)
tree.insert_left(2)
tree.insert_left(4)
tree.insert_right(3)
tree.insert_right(6)
tree.right.insert_left(5)
tree.right.insert_left(7)
tree.right.left.insert_right(8)
tree.inorder_traversal_iterative()
# print(tree.inorder_traversal_recursive())
