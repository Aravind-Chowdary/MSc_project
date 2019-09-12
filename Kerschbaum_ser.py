class RedBlackTree:

    class Node():
        def __init__(self, key=None,color='red'):
            self.right = None
            self.left = None
            self.p = None
            self.key = key
            self.color = color

    def __init__(self):
        self.NIL = self.Node(key = None, color='black')
        self.root = self.NIL
        self.size = 0
        self.ordered = []
        pass

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def insert(self, z):
        new_node = self.Node(key=z)
        self._insert(new_node)
        self.size += 1

    def _insert(self, z):
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.color = "red"
        self.rb_insert_fixup(z)


    def rb_insert_fixup(self, z):
        i = 0
        while z.p.color == "red":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'red':
                    z.p.color = "black"
                    y.color = "black"
                    z.p.p.color = "red"
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 'red':
                    z.p.color = "black"
                    y.color = "black"
                    z.p.p.color = "red"
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self.left_rotate(z.p.p)
            i += 1
        self.root.color = 'black'