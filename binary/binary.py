class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"

def reverseBinaryTree(theTree):
    if theTree:
        print(theTree.data)
        print(theTree.left)
        print(theTree.right)
        left = theTree.left
        right = theTree.right
        theTree.left = right
        theTree.right = left
        reverseBinaryTree(theTree.left)
        reverseBinaryTree(theTree.right)
# print(tree.find(3).v)
# print(tree.find(10))
# tree.deleteTree()
# tree.printTree()



reverseBinaryTree(root)