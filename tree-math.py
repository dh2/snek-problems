# This problem was asked by Microsoft.

# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:

#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45.

#            *
#       /        \
#     +           +
#   /   \       /   \
#  +     +     +     -
# / \   / \   / \   / \
# 3  2  4  5 1   1 8   6
# You should return 56.

#             -
#       /           \
#     +              +
#   /   \        /       \
#    +     +       +           -
#   / \   / \     / \       /    \
#  *  +    -  +   +    +      -     +
# /\  /\  / \ /\  / \  / \    / \   / \   
# 3 2 0 5 4 5 5 4 1  1 8  6  10  5 5   1  
# You should return 4

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.rCount = 0
        self.lCount = 0
        self.value = value

    def isFull(self, count):
        # leftFull = False if self.left is None else self.left.isFull()
        # rightFull = False if self.right is None else self.right.isFull()
        # return leftFull and rightFull
        count = count + 1
 
        # Loop to check the count is in
        # the form of 2^(n-1)
        while (count % 2 == 0):
            count = count / 2
    
        if (count == 1):
            return True
        else:
            return False
    
    def branchCount(self):
        base = self.rCount + self.lCount
        left = 0 if self.left is None else self.left.branchCount()
        right = 0 if self.right is None else self.right.branchCount()
        return base + left + right

    def insert(self, value):
        if self.left is None:
            self.lCount += 1
            self.left = TreeNode(value)
        elif self.right is None:
            self.rCount += 1
            self.right = TreeNode(value)
        elif self.lCount == self.rCount:
            self.lCount += 1
            self.left.insert(value)
        elif self.rCount < self.lCount:
            if not self.isFull(self.lCount):
                self.left.insert(value)
                self.lCount += 1
            else:
                self.right.insert(value)
                self.rCount += 1
        else:
            print('\n*********************************\n')
            print("LB: {0}  RB: {1}\n".format(self.lCount, self.rCount))
            self.PrintTree()
            raise Exception('No valid branches left to build')
    
    def PrintBranch(self):
        l = self.left.value if self.left is not None else '#'
        r = self.right.value if self.right is not None else '#'

        if self.left or self.right:
            print("{0}:  {1} {2}".format(self.value,l,r))
        if self.left:
            self.left.PrintTree(True)
        if self.right:
            self.right.PrintTree(True)

    def PrintTree(self, branchOnly = False):
        if not branchOnly:
            print(self.value)
        self.PrintBranch()


def doTreeMath(node):
    if type(node.value) is int or type(node.value) is float:
        # We hit a leaf
        return node.value
    
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
    else:
        raise Exception('Invalid node value type %s' % type(node.value))

def processTree(nodeArray: list):
    root = nodeArray.pop(0)
    tree = TreeNode(root)
    count = len(nodeArray)
    for i in range(count):
        tree.insert(nodeArray[i])

    tree.PrintTree()
    print("Value: {0}".format(doTreeMath(tree)))

r1 = ['*', '+', '+',3,2,4,5]
processTree(r1)

print('\n***********************')
r2 = ['*','+','+','+','+','+','-',3,2,4,5,1,1,8,6]
processTree(r2)
print('\n***********************')

r3 = ['-','+','+','+','+','+','-','*','+','-','+','+','+','-','+',3,2,0,5,4,5,5,4,1,1,8,6,10,5,5,1]
processTree(r3)