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

    def height(self,h=0):
        left_height = self.left.height(h + 1) if self.left else h
        right_height = self.right.height(h + 1) if self.right else h
        return max(left_height, right_height)

    def getnodesatdepth(self, depth, nodes=[]):
        if depth > self.height():
            print("depth is greater than tree height!")
            return None
        if depth == 0:
            nodes.append(self.data)
            return nodes
        if self.left:
            self.left.getnodesatdepth(depth - 1, nodes)
        else:
            nodes.extend([None]*2**(depth - 1))

        if self.right:
            self.right.getnodesatdepth(depth - 1, nodes)
        else:
            nodes.extend([None]*2**(depth - 1))

        return nodes


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

    def height(self):
        return self.root.height()

    def getnodesatdepth(self, depth):
        return self.root.getnodesatdepth(depth)


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
print(f'Tree height = {myTree.height()}')
node1 = Node(50)
node1.left = Node(25)
node1.right = Node(75)
node1.left.left = Node(13)
node1.left.right = Node(35)
node1.left.right.right = Node(37)
node1.left.left.left = Node(2)
node1.left.left.right = Node(20)
node1.right.left = Node(55)
node1.right.right = Node(103)
node1.right.right.right = Node(256)

myTree2 = Tree(node1, "Second Tree")
print(myTree2.getnodesatdepth(3))
