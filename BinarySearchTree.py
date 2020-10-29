

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _isValidBSTHelper(self, node, low, high):

        if not node:
            return True
        cur_val = node.val
        if (cur_val > low and cur_val < high) and \
        self._isValidBSTHelper(node.left, low, cur_val) and \
        self._isValidBSTHelper(node.right, cur_val, high):
            return True
        return False

    def isValidBST(self, node):
        return self._isValidBSTHelper(node, float('-inf'), float('inf'))
# BST 1
node = Node(5)

node.left = Node(4)
node.left.right = Node(8)

node.right = Node(7)
print (Solution().isValidBST(node))

# BST 2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print (Solution().isValidBST(node))

# BST 3
node = Node(5)
node.left = Node(3)
node.left.right = Node(4)
node.left.left = Node(2)

node.right = Node(7)
node.right.right = Node(10)
node.right.right.left = Node(9)
print (Solution().isValidBST(node))

# BST 5
node = Node(10)
node.left = Node(12)
node.right = Node(13)

print (Solution().isValidBST(node))