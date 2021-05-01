'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST
import copy


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        if self.root is None:
            return True
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        ret &= BST._is_bst_satisfied(node)
        ret &= AVLTree._balance_factor(node) in [-1, 0, 1]
        if node.right:
            ret &= AVLTree._balance_factor(node.right) in [-1, 0, 1]
        if node.left:
            ret &= AVLTree._balance_factor(node.left) in [-1, 0, 1]
        return ret

    @staticmethod
    def _left_rotate(node):
        '''
        returns a Node() type

        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        temp = copy.deepcopy(node)
        new_root = copy.deepcopy(temp.right)
        temp_node = temp.right.left
        new_root.right = temp.right.right
        temp.right = temp_node
        new_root.left = temp
        return new_root

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        temp = copy.deepcopy(node)
        new_root = copy.deepcopy(temp.left)
        temp_node = temp.left.right
        new_root.left = temp.left.left
        temp.left = temp_node
        new_root.right = temp
        return new_root

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        # Not working yet
        return
        if self.root:
            AVLTree._insert(self.root, value.root)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value, parent):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                AVLTree._rebalance(parent)
            else:
                AVLTree._insert(node.left, value, node)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                AVLTree._rebalance(parent)
            else:
                AVLTree._insert(node.right, value, node)
        else:
            pass

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            else:
                AVLTree._right_rotate(node)
