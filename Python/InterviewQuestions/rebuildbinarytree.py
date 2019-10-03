#-------------------------------------------------------------------------------
# Purpose/Question: rebuild binary tree
#
'''
Enter the result of the preorder traversal and the in-order traversal of a binary tree,
and reconstruct the binary tree. It is assumed that the results of the pre-order traversal
and the in-order traversal of the input do not contain duplicate numbers.
For example, if the pre-order traversal sequence {1, 2, 4, 7, 3, 5, 6, 8} and the
mid-order traversal sequence {4, 7, 2, 1, 5, 3, 8, 6} are input, the binary tree is
reconstructed. return.
'''
# Author:      Olivier Laflamme
#
# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

# -*- coding:utf-8 -*-
class  TreeNode :
    def  __init__ ( self , x ):
        self .val = x
        self .left =  None
        self .right =  None

class  Solution :
    #TreeNode root node
    def  reConstructBinaryTree ( self , pre , tin ):
        # write code here
        if  not pre or  not tin:
            return  None
        root = TreeNode(pre[ 0 ])
        val = tin.index(pre[ 0 ])

        # the first parameter
        root.left =  self .reConstructBinaryTree(pre[ 1 :val +  1 ], tin[:val])
        root.right =  self .reConstructBinaryTree(pre[val +  1 :], tin[val +  1 :])
        return root