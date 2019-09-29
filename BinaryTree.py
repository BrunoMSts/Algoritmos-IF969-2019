class No:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self, otherNo):
        if self.value < otherNo.value:
            return True
        return False

    def __gt__(self, otherNo):
        if self.value > otherNo.value:
            return True
        return False
    
    def __le__(self, otherNo):
        if self.value <= otherNo.value:
            return True
        return False
    
    def __ge__(self, otherNo):
        if self.value >= otherNo.value:
            return True
        return False
    
    def __eq__(self, otherNo):
        if self.value == otherNo.value:
            return True
        return False
    
    def __ne__(self, otherNo):
        if self.value != otherNo.value:
            return True
        return False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()
    
class Tree:
    def __init__(self, tree = None):
        if tree:
            node = No(tree)            
            self.root = node
        else:
            self.root = None
        self.height = 0

    def insert(self, elem = None, tree = None):
        if tree is None:
            tree = self.root
            self.insert(elem, tree)
        else:
            if elem < tree.value:
                if tree.left is None:
                    tree.left = No(elem)
                self.insert(elem, tree.left)
            elif elem > tree.value:
                if tree.right is None:
                    tree.right = No(elem)
                self.insert(elem, tree.right)

    def inOrdem(self, tree = None): #<-- Árvore...
        if not tree:
            tree = self.root
        if tree.left:
            self.inOrdem(tree.left)
        print(tree)
        if tree.right:
            self.inOrdem(tree.right)


    def preOrdem(self, tree = None):
        if not tree:
            tree = self.root
        print(tree)
        if tree.left:
            self.preOrdem(tree.left)
        if tree.right:
            self.preOrdem(tree.right)

    def reiniciar(self, elem = None, tree = None): 
        if tree is None:
            tree = self.root
        else:
            pass

    def posOrdem(self, tree = None):
        pass

    def __bool__(self):
        if self.height == 0:
            return False
        return True

    def __str__(self):
        return self.inOrdem()
    def __repr__(self):
        return self.preOrdem()

    def __getitem__(self):
        pass

    def __setitem__(self):
        pass

    def __iter__(self):
        return self
    
    def __next__(self, tree = None):
        if not tree:
            tree = self.root
        print(tree)
        if tree.left:
            self.preOrdem(tree.left)
        if tree.right:
            self.preOrdem(tree.right)
        raise StopIteration()
    
    def __dict__(self):
        pass
if __name__ == "__main__":
    t = Tree(5)
    print(t.root)