# This problem was asked by Microsoft.

# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:

#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def isFull(self):
        return self.left is not None and self.right is not None

    def insert(self, value):
        if self.left is None:
            self.left = TreeNode(value)
        elif self.right is None:
            self.right = TreeNode(value)
        elif not self.left.isFull():
            self.left.insert(value)
        elif not self.right.isFull():
            self.right.insert(value)
        else:
            raise Exception('No valid branches left to build')
            

    def PrintTree(self):
        print(self.value)
        if self.left or self.right:
            print('\n')
            self.left.PrintTree()
            self.right.PrintTree()


def doTreeMath(node):
    if type(node.value) is str:
        if node.value == '+':
            return doTreeMath(node.left) + doTreeMath(node.right)
        elif node.value == '-':
            return doTreeMath(node.left) - doTreeMath(node.right)
        elif node.value == '*':
            return doTreeMath(node.left) * doTreeMath(node.right)
        elif node.value == '/':
            return doTreeMath(node.left) / doTreeMath(node.right)
        else:
            raise Exception('Invalid math operator')
    elif type(node.value) is int or type(node.value) is float:
        # We hit a leaf
        return node.value
    else:
        raise Exception('Invalid node value type %s' % type(node.value))
    
root = TreeNode('*')
root.insert('+')
root.insert('+')
root.insert(3)
root.insert(2)
root.insert(4)
root.insert(5)
root.PrintTree()
print(doTreeMath(root))