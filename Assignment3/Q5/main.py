from __future__ import absolute_import

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import math
import random
import numpy as np
from leftrb.llrb import LeftRB, is_red, is_black

from leftrb.bst import BinarySearchTree
import leftrb.llrb
key = 7

lines = [line.rstrip('\n') for line in open('data.txt')]

#print(lines)
count = 0

def get_rank(root,key):
	
	res = []
	
	if root:
		res = get_rank(root.left,key) 
		res.append(root.key)
		res = res + get_rank(root.right,key)
	
	return res

def get_select(root):

	res = []
	
	if root:
		res = get_rank(root.left,key) 
		res.append(root.key)
		res = res + get_rank(root.right,key)
	
	return res



tree = BinarySearchTree()


for value in lines:
	tree.insert(int(value))


print(tree.root)
print(tree.search(3))
rank = get_rank(tree.root, key)
select = get_select(tree.root)
print("Rank: "+rank[key-2])
print("Select: "+select[key])
