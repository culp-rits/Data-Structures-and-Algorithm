class bitree:
    def __init__(self,key):
        self.key = key
        self.children = []
        self.order = 0
    
    def add_bitree(self,tree):
        self.children.append(tree)
        self.order += 1

    def show(self,x):
        print(x.key, end=" ")
        for i in x.children:
            self.show(i)

class binomialheap:
    def __init__(self):
        self.trees = []

    def insert(self,key):
        heap = binomialheap()
        tree = bitree(key)
        heap.trees.append(tree)
        self.merge(heap)

    def merge(self,heap):
        self.trees.extend(heap.trees)
        self.trees.sort(key = lambda tree:tree.order)
        if(self.trees == []):
            return
        i = 0
        while(i < len(self.trees)-1):
            temp = self.trees[i]
            temp_next = self.trees[i+1]
            if(temp.order == temp_next.order):
                if(i < len(self.trees)-2 and self.trees[i+2].order == temp_next.order):
                    temp_next_next =  self.trees[i+2]
                    if(temp_next.key < temp_next_next.key):
                        temp_next.add_bitree(temp_next_next)
                        del self.trees[i+2]
                    else:
                        temp_next_next.add_bitree(temp_next)
                        del self.trees[i+1]
                else:
                    if(temp.key < temp_next.key):
                        temp.add_bitree(temp_next)
                        del self.trees[i+1]
                    else:
                        temp_next.add_bitree(temp)
                        del self.trees[i]
            i += 1

    def get_min(self):
        min = self.trees[0].key
        for tree in self.trees:
            if(tree.key < min):
                min = tree.key
        print("Min =",min)

    def extract_min(self):
        min_tree = self.trees[0]
        for tree in self.trees:
            if(tree.key < min_tree.key):
                min_tree = tree
        self.trees.remove(min_tree)
        heap = binomialheap()
        heap.trees = min_tree.children
        self.merge(heap)
        print("Extracted Min =",min_tree.key)
    
    def print_tree(self):
        for i in self.trees:
            i.show(i)
            print("\n")
