class Tree:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key 

def insert(root,key):
    #if the tree is empty - return the root node as this becomes the root node
    if root is None:
        return Tree(key)
    
    #otherwise go down the tree
    if key<root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

#deleting a node
def deletenode(root, key):
    #base case : if root is empty
    if root is None:
        return root
    
    #going down the tree to find the node
    if key < root.value:
        root.left = deletenode ( root.left, key)

    elif key > root.value:
        root.right= deletenode(root.right, key)

    else:
        #case 1 : if the node is a leaf node (no children) 
        if root.left is None and root.right is None:
            return None
        #case 2: if the node only 1 child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        #case 3: if the node has 2 children 
        # inorder successor : (lowest in the right subtree)
        #inorder predessor : (highest in left subtree)
        temp = findmin(root.right)

        #replace roots value with the successor's value
        root.value = temp.value

        #delete the inorder sucessor
        root.right = deletenode(root.right, temp.value)

    return root

# Function to find the minimum value in right subtree (INorder sucessor)
def findmin(node):
    current = node
    while current.left is not None:
        current = current.left
    return current 

def inordertraversal(root):
    if root:
        inordertraversal(root.left)
        print(root.value, end = "-")
        inordertraversal(root.right)

#Examples
root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)

print("the inordertraversal of tree before deleting the node:")
print(inordertraversal(root))

#deleting the leaf node - 40
root = deletenode(root, 40)
print( "\n The Inordertravseral of tree after deleting the node: ")
print(inordertraversal(root))

root = deletenode(root,30)
print( "\n The Inordertravseral of tree after deleting the node: ")
print(inordertraversal(root))

root = deletenode( root, 70)
print( "\n The Inordertravseral of tree after deleting the node: ")
print(inordertraversal(root))







    




