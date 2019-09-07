
from Popa_cli import dec
import sqlite3


class OPETree:
    # __ denotes private class member or method
    def __init__(self):
        pass

    __key = None
    __tree = None
    __table = None #dictionary/map data type

    def set_key(self, key):
        self.__key = key

    def insert_in_tree(self, enc_val, iv):
        val = dec(self.__key,enc_val,iv)
        if self.tree is None:
            self.__tree = Tree.new(val)
            path = ""
            self.__insert_path_in_table(enc_val, path)
        else:
            path = self.__tree.insert(val, "") #Note: we initially set path as empty
            self.__insert_path_in_table(enc_val, path)


    def __insert_path_in_table(self, enc_val, path): #Add encrypted value and path to table

        conn = sqlite3.connect('testdb2.sqlite')

        cursor = conn.cursor()

        query = '''
               	    CREATE TABLE IF NOT EXISTS pepe(
               	    	enc_val text, 
               	    	path text
               	    )
               	'''

        cursor.execute(query)

        query1 = '''
                INSERT INTO pepe (enc_val, path )
                VALUES ( ?,? )
                '''
        cursor.execute(query1)
        conn.commit()
        conn.close()

    def lookup_path(self, enc_val):
        conn = sqlite3.connect('testdb2.sqlite')

        cursor = conn.cursor()

        query = '''
                       	    SELECT path 
                       	    FROM pepe
                       	'''

        cursor.execute(query)
        conn.commit()
        conn.close()

    def compare(self, enc_val_1, enc_val_2):

        path1 = self.lookup_path(enc_val_1)
        path2 = self.lookup_path(enc_val_2)
        cnt = 0
        while path1[cnt] == path2[cnt]:
            cnt += 1
        if path1[cnt] == "" and path2[cnt] == "0":
            return 1
        if path1[cnt] == "" and path2[cnt] == "1":
            return -1
        if path1[cnt] == "0" and path2[cnt] == "":
            return -1
        if path1[cnt] == "1" and path2[cnt] == "":
            return 1
        if path1[cnt] == "0" and path2[cnt] == "1":
            return -1
        if path1[cnt] == "1" and path2[cnt] == "0":
            return 1
        return 0


class Node:
    __left=None
    __right=None
    __val=None

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A utility function to insert a new node with the given key


class Tree:
    __root = None

    def __init__(self, val):
        self.__root = Node.new(val)

    def insert(self, val, path):
        return self.__insert(self.__root, val, path)

    def __insert(self, node, val, path):
        if node.val < val:
            if node.right is None:
                node.right = Node.new(val)
                return path
            else:
                self.__insert(node.right, val, path+"1")
        else:
            if node.left is None:
                node.left = Node.new(val)
                return path
            else:
                self.__insert(node.left, val, path+"0")
