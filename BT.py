class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.level = None

class BinaryTree:
    

    import turtle
    turtle.speed(10)
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(0,300)

    radius = 15



    def __init__(self):
        self.root = None
        
    def getRoot(self):
        return self.root

    def add(self,value):
        if self.root == None:
            self.root = Node(value)
            self.root.level = 1
            self.turtle.pendown()
            self.turtle.circle(self.radius)
            self.turtle.write(self.root.data)
            self.turtle.penup()
        else:
            self._add(value,self.root)

    def _add(self,val, node,level=2,x=0):
        if val<node.data:
            if node.left is not None:
                self._add(val,node.left,level+1,x-50)
            else:
                node.left = Node(val)
                node.left.level = level
                self.turtle.goto(x-50,300-level*50)
                self.turtle.pendown()
                self.turtle.circle(self.radius)
                self.turtle.write(node.left.data)
                self.turtle.penup()
        else:
            if node.right is not None:
                self._add(val,node.right,level+1,x+50)
            else:
                node.right = Node(val)
                node.right.level = level
                self.turtle.goto(x+50,300-50*level)
                self.turtle.pendown()
                self.turtle.circle(self.radius)
                self.turtle.write(node.right.data)
                self.turtle.penup()

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.data)+ " " +str(node.level) + ' ')
            self._printTree(node.right)

    def getLevel(self,node,level=1):
        if self.root == None:
            return 0
        
            
            
        









import random
l = [random.randint(0,100) for i in range(20)]
tree = BinaryTree()
for i in range(len(l)):
    c = l[i]
    if i!=len(l)-1:
        print(c,end=" ")
    else:
        print(c)
        
    tree.add(c)

tree.printTree()

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.level = None

class BinaryTree:
    
    global turtle
    def __init__(self):
        self.root = None
        
    def getRoot(self):
        return self.root

    def add(self,value):
        if self.root == None:
            self.root = Node(value)
            self.root.level = 1
            turtle.circle(2)
            turtle.write(self.root)
        else:
            self._add(value,self.root)

    def _add(self,val, node,level=2):
        if val<node.data:
            if node.left is not None:
                self._add(val,node.left,level+1)
            else:
                node.left = Node(val)
                node.left.level = level
                turle.goto(0,300)
                turtle.pendown()
                turtle.circle(2)
                turtle.write(node.write)
                turtle.penup()
        else:
            if node.right is not None:
                self._add(val,node.right,level+1)
            else:
                node.right = Node(val)
                node.right.level = level
                turtle.goto(0,300-100*level)
                turtle.pendown()
                turtle.circle(2)
                turtle.write(node.right)
                turtle.penup()

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.data)+ " " +str(node.level) + ' ')
            self._printTree(node.right)

    def getLevel(self,node,level=1):
        if self.root == None:
            return 0
        
            
            
        









import random
l = [random.randint(0,40) for i in range(20)]
tree = BinaryTree()
for i in range(len(l)):
    c = l[i]
    if i!=len(l)-1:
        print(c,end=" ")
    else:
        print(c)
        
    tree.add(c)

tree.printTree()


import turtle
turtle.speed(10)
turtle.shape('turtle')
turtle.penup()
turtle.goto(0,300)





