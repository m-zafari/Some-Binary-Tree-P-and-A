
# mohammad zafari

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkUtil(root, level):
    if root is None:
        return True

    if root.left is None and root.right is None:
        if check.leafLevel == 0 :
            check.leafLevel = level 
            return True
        return level == check.leafLevel 
    return (checkUtil(root.left, level+1)and
            checkUtil(root.right, level+1))
 
def check(root):
    level = 0
    check.leafLevel = 0
    return (checkUtil(root, level))
 
# Driver program 
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.right.left = Node(8)
root.left.right.left.left  = Node(9)
root.left.right.left.right = Node(10)

if(check(root)):
    print("Leaves are at same level")
else:
    print("Leaves are not at same level")

