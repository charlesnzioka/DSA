class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print('Found it!')
            return self
        if self.left and self.data > target:
            return self.left.search(target)
        if self.right and self.data < target:
            return self.right.search(target)
        print(f"Not found {target}!")

    def traversepreorder(self):
        print(self.data)

        if self.left:
            self.left.traversepreorder()
        if self.right:
            self.right.traversepreorder()

    def traverseinorder(self):
        if self.left:
            self.left.traverseinorder()
        print(self.data)
        if self.right:
            self.right.traverseinorder()

    def traversepostorder(self):
        if self.left:
            self.left.traversepostorder()
        if self.right:
            self.right.traversepostorder()
        print(self.data)


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def traversepreorder(self):
        self.root.traversepreorder()

    def traverseinorder(self):
        self.root.traverseinorder()

    def traversepostorder(self):
        self.root.traversepostorder()


node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

print(node.right.data)
print(node.right.right.data)

myTree = Tree(node)
myTree.search(6)
print('-'*10)
print("Pre Order Traversal")
myTree.traversepreorder()
print('-'*10)
print("In Order Traversal")
myTree.traverseinorder()
print('-'*10)
print("Post Order Traversal")
myTree.traversepostorder()
print('-'*10)
