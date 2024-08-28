class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#function to perform inorder traversal
def inorderTraversal(root):

    #Base case:if null
    if root is None:
        return
    
    #recur on the left subtree
    inorderTraversal(root.left)

    #visit the current node
    print(root.data,end=" ")

    #recur on the right subtree
    inorderTraversal(root.right)


root =  Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
inorderTraversal(root)