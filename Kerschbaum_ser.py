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