"""
You could do a DFS using recursion or iteration (stack)

The time would be O(n) since you have to validate every single one

https://leetcode.com/problems/validate-binary-search-tree/description/

"""

#Recursion Method
def recurValidateBst(node, upperLim, lowerLim):
    
	#Reached End
    if node is None:
        return True
    
	#Reached Error
    if (node.value > upperLim) or (node.value < lowerLim):
        return False

	#Traverse Down
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

