# No Queue Implemented. To be updated.

# class Node:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.top = value
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def getRoot(self):
#         return self.root
#
#     def add(self, val):
#         if self.root is None:
#             self.root = Node(val)
#         else:
#             self.addChild(val, self.root)
#
#     def addChild(self, val, node):
#         if node.left is None:
#             node.left = Node(val)
#         elif node.right is None:
#             node.right = Node(val)
#         else:
#             self.addChild(val, node.left)
#
#     def printTree(self):
#         if self.root is not None:
#             self._printTree(self.root)
#
#     def _printTree(self, node):
#         if(node != None):
#             self._printTree(node.left)
#             print str(node.top) + ' '
#             self._printTree(node.right)
#
# tree = Tree()
# n = map(int,raw_input("Elements\n").split())
# for x in n:
#     tree.add(x)
# tree.printTree()