class BSTNode(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root=None):
        self.root = root
        self.count = 0

    def lookup(self, value):
        checker = self.root

        while checker:
            if value == checker.value:
                return True
            elif value < checker.value:
                checker = checker.left
            else:
                checker = checker.right

        return False

    def insert(self, value):
        node = BSTNode(value)
        if not self.count:
            # BST is empty add the first node
            self.root = node
            self.count += 1
        else:
            checker = self.root
            while True:
                if value < checker.value:
                    if not checker.left:
                        checker.left = node
                        self.count += 1
                        break
                    checker = checker.left
                else:
                    if not checker.right:
                        checker.right = node
                        self.count += 1
                        break
                    checker = checker.right

bst = BST()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)

print(bst.lookup(1))
print(bst.lookup(1000))
print(bst.lookup(6))
print(bst.lookup('xxx'))
print(bst.lookup(170))