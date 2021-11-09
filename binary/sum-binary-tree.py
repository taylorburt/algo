class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = Tree()
root.data = 5
root.left = Tree()
root.left.data = 3
root.left.left = Tree()
root.left.left.data = 2
root.left.right = Tree()
root.left.right.data = 4
root.right = Tree()
root.right.data = 8
root.right.left = Tree()
root.right.left.data = 6
root.right.right = Tree()
root.right.right.data = 10

xsum = 0

def findRange(values):
    min_val = min(values)
    max_val = max(values)
    return min_val, max_val

def sumBinaryTree(tree, targets):
    global xsum
    min_val, max_val = findRange(targets)
    if tree:
        if ((int(tree.data) >= min_val) and
            (int(tree.data) <= max_val)):
            print(tree.data)
            xsum = tree.data + xsum
        sumBinaryTree(tree.left, targets)
        sumBinaryTree(tree.right, targets)


targets = [4, 9]
sumBinaryTree(root, targets)
print(xsum)
