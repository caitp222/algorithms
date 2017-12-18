# http://interactivepython.org/runestone/static/pythonds/Trees/NodesandReferences.html
# http://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/

class BinaryTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def insert_left(self, data):
    if self.left == None:
      self.left = BinaryTree(data)
    else:
      self.left.insert_left(data)

  def insert_right(self,data):
    if self.right == None:
      self.right = BinaryTree(data)
    else:
      self.right.insert_right(data)

  def preorder_traversal(self):
      if self.left:
          self.left.preorder_traversal()
      if self.right:
          self.right.preorder_traversal()


# build tree
tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_left(4)
tree.insert_right(3)
tree.insert_right(6)
tree.right.insert_left(5)
tree.right.insert_left(7)
tree.right.left.insert_right(8)
tree.preorder_traversal()
