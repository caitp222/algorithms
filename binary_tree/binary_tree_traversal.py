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
      current = self
      nodes = []
      while current != None or len(nodes) > 0:
          if current == None:
              current = nodes[-1]
              del(nodes[-1])
              while current.right == None and len(nodes) > 0:
                  current = nodes[-1]
                  del(nodes[-1])
              current = current.right
          else:
              print current.data
              nodes.append(current)
              current = current.left

  def preorder_traversal_recursive(self):
      print self.data
      if self.left:
          self.left.preorder_traversal()
      if self.right:
          self.right.preorder_traversal()

  def postorder_traversal_iterative(self):
      current = self
      nodes = []
      output = []
      while current.left != None or len(nodes) >= 1:
          print "current is %i" %(current.data)
          if len(nodes) > 0:
              print "nodes[-1] is %i" %(nodes[-1].data)
          if current.left == None and current.right == None:
              while current.right == None:
                  output.append(current.data)
                  current = nodes[-1]
                  del(nodes[-1])
              print current.data
              current = current.right
              # break
          else:
              nodes.append(current)
              current = current.left
      print nodes
      print output


  def postorder_traversal_recursive(self):
      if self.left == None:
          return
      self.left.postorder_traversal_recursive()
      print self.left.data
      if self.right == None:
          return
      self.right.postorder_traversal_recursive()
      print self.right.data
      # need to figure out the root node issue
      # print self.data


# build tree
tree = BinaryTreeNode(1)
tree.insert_left(2)
tree.insert_left(4)
tree.insert_right(3)
tree.insert_right(6)
tree.right.insert_left(5)
tree.right.insert_left(7)
tree.right.left.insert_right(8)

# tree.postorder_traversal_recursive()
tree.postorder_traversal_iterative()
