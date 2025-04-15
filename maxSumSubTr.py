
# mohammad zafari

class Tree:

    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None
        
    def tree_elm_sum(self):
        
        if self.lChild and self.rChild:
            return float(self.data) + float(self.lChild.tree_elm_sum()) + float(self.rChild.tree_elm_sum())
        
        elif self.rChild:
            return float(self.data) + float(self.rChild.tree_elm_sum())
        
        elif self.lChild:
            return float(self.data) + float(self.lChild.tree_elm_sum())
        
        else:
            return float(self.data)
    
    
    def preorder(self):
        if self is not None:
            print(self.data, end =' ')
            if self.lChild is not  None:
                self.lChild.preorder()
            if self.rChild:
                self.rChild.preorder()


    def ListOfSubTrees(self,is_root ,subtrees: dict):
        subtrees['SubTrees'].append(self)
        subtrees['Sum'].append(self.tree_elm_sum())
        if self.lChild and self.rChild:
            self.lChild.ListOfSubTrees(False, subtrees)
            self.rChild.ListOfSubTrees(False,subtrees)
        elif self.lChild:
            self.lChild.ListOfSubTrees(False, subtrees)
        elif self.rChild:
            self.rChild.ListOfSubTrees(False, subtrees)
        if is_root:
            return subtrees
        
dic = {
    "SubTrees": [],
    "Sum":[],
    }

t1 = Tree(1)
t1.lChild = Tree(-2)
t1.rChild = Tree(3)
t1.lChild.lChild = Tree(4)
t1.lChild.rChild = Tree(5)
t1.rChild.lChild = Tree(-6)
t1.rChild.rChild = Tree(2)

t1.ListOfSubTrees(True, dic)

maxSubtree = None

max = None
    
for (subtree, summ) in zip(dic['SubTrees'], dic['Sum']):

    if max :

        if max <= summ:

            maxSubtree = subtree
            max = summ

    else:

        max = summ
        maxSubtree = subtree


print('subtree with largest sum(preorder):')

maxSubtree.preorder()

print('\nlargest subtree sum:', max)
    