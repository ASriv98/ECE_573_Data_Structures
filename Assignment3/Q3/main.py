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


Tree = LeftRB

# def fill_tree(items):
# 	tree = Tree()
# 	map(tree.insert, items)
# 	return tree


# class TestLeftRB(Base):

# 	items = [5, 1, 3, 6]

# 	def test_search(self):
# 		t = fill_tree(self.items)
# 		needle = max(self.items)
# 		assert t.search(needle) == needle

# 	def test_in(self):
# 		t = fill_tree(self.items)
# 		needle = max(self.items)
# 		assert needle in t

# 	def test_len(self):
# 		t = fill_tree(self.items)
# 		assert len(t) == len(self.items)

# 	def test_height(self):
# 		for n in range(1, 16):
# 			items = random.sample(range(n), n)
# 			t = fill_tree(items)
# 			print("Items: {0}".format(items))
# 			assert t.height() <= int(2 * math.ceil(math.log(n, 2) + 1))

# 	def test_min(self):
# 		t = fill_tree(self.items)
# 		assert t.min() == min(self.items)

# 	def test_max(self):
# 		t = fill_tree(self.items)
# 		assert t.max() == max(self.items)

# 	def test_delete(self):
# 		t = fill_tree(random.sample(range(100), 90))

# 		key = random.randint(0, 999)
# 		value = str(key)
# 		t.insert(key, value)
# 		assert value == t.search(key)
# 		t.delete(key)
# 		assert None == t.search(key)

count = 0
count2 = 0

def getNumberNodes(root):

	global count2

	if (root == None):
		return root


	if is_red(root) or is_black(root):
		count2+=1


	getNumberNodes(root.left)
	getNumberNodes(root.right)

	return count2


def getNumberRedNodes(root):

	global count
	
	if (root == None):
		return root
	
	if is_red(root):
		count+=1

	getNumberRedNodes(root.left)
	getNumberRedNodes(root.right)

	return count

llrb_tree = LeftRB()
llrb_tree2= LeftRB()
llrb_tree3= LeftRB()

final1 = []
final2 = []
final3 = []


#change the trial size values
for i in range(0,1):

	for i in range(0,10000):
		randomNumber = random.randint(0,10000)
		llrb_tree.insert(randomNumber)

	for i in range(0,100000):
		randomNumber = random.randint(0,100000)
		llrb_tree.insert(randomNumber)

	for i in range(0,1000000):
		randomNumber = random.randint(0,1000000)
		llrb_tree.insert(randomNumber)


	numberRedNodes = getNumberRedNodes(llrb_tree.root)
	numberNodes = getNumberNodes(llrb_tree.root)

	numberRedNodes2 = getNumberRedNodes(llrb_tree.root)
	numberNodes2 = getNumberNodes(llrb_tree.root)

	numberRedNodes3 = getNumberRedNodes(llrb_tree.root)
	numberNodes3 = getNumberNodes(llrb_tree.root)

	percentage_red  = numberRedNodes/10000
	percentage_red2 = numberRedNodes/100000
	percentage_red3 = numberRedNodes/1000000

	final1.append(percentage_red)
	final2.append(percentage_red2)
	final3.append(percentage_red3)


print(np.mean(final1))
print(np.mean(final2))
print(np.mean(final3))



