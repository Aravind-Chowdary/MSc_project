from Crypto.Cipher import AES
from Popa_cli import enc

# Getting the value from the client needs to be done!!

# Doubt- where does the dec method goes!!


def dec(key,encd, adec, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    decd = adec.decrypt(encd)
    return decd


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A utility function to insert a new node with the given key


def insert(root, node):  # Doubts in tree construction like how to use keys
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)