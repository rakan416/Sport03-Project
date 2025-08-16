import pickle
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = " "*self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + str(self.data))
        if self.child:
            for chi in self.child:
                chi.print_tree()

    def add_child(self, chil):
        chil.parent = self
        self.child.append(chil)

# trn = TreeNode('Root')
# fl = open('Data/treeDatabase.pickle','wb')
# pickle.dump(trn, fl)
# fl.close()

