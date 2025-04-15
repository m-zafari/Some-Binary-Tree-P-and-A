
# mohammad zafari

class newNode:  
    def __init__(self, data):  
        self.data = data  
        self.left =  None
        self.right = None

def heighAndSize(node, size):  
    if (node == None) : 
        return 0
    L = heighAndSize(node.left, size)  
    R = heighAndSize(node.right, size)  
    size[0] += 1
    return L + 1 if(L > R) else R + 1

def density(root): 
    if (root == None) : 
        return 0
    size = [0] 
    height = heighAndSize(root, size)  
    return size[0] / height 

# Driver program 
if __name__ == '__main__': 
    root = newNode(5)  
    root.left = newNode(6)  
    root.right = newNode(7)  
    root.right.right = newNode(10)
    root.right.right.right = newNode(20)
    print("Density is ", density(root)) 
