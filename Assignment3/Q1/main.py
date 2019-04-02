from __future__ import absolute_import

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import math
import random
import numpy as np
import llrb

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
