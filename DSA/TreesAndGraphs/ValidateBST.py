import unittest

"""
Validate BST using recursion

"""

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

"""
You could do a DFS using recursion or iteration (stack)

The time would be O(n) since you have to validate every single one

"""

#Recursion Method
def recurValidateBst(node, upperLim, lowerLim):
    
    if node is None:
        return True
    
    if (node.value > upperLim) or (node.value < lowerLim):
        return False

    return recurValidateBst(node.left, node.value, lowerLim ) and recurValidateBst(node.right, upperLim, node.value)


#Iterative Method
def iterValidateBst(node):
    
    if node is None:
        return False
    
    stack = [(node, float('inf'), -float('inf'))]
    
    while (len(stack)):
        
        node, upperLim, lowerLim = stack.pop()
        
        if (node.value < lowerLim) or (node.value > upperLim):
            return False
        
        if node.right is not None:
            stack.append((node.right, upperLim, node.value))
        
        if node.left is not None:
            stack.append((node.left, node.value, lowerLim))
    
    return True
    

def is_binary_search_tree(root):
    
    if root is None:
        return False
    
    return recurValidateBst(root, float('inf'), -float('inf')) and iterValidateBst(root)

#########################################################
# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)