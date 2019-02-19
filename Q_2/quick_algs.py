class QuickFind(object):
	def __init__(self, n):
			n = 8192
			self.list = range(n)

	def find(self, a, b):
		return self.list[a] == self.list[b]

	def union(self, a, b):
		old = self.list[a]
		new = self.list[b]
		for ind, x in enumerate(self.list):
			if x == old:
				self.list[ind] = new


class QuickUnion(object):
	def __init__(self, N):
		self.list = range(N)

	def get_root(self, index):
		while index != self.list[index]:
			index = self.list[index]
		return index

	def find(self, a, b):
		return self.get_root(a) == self.get_root(b)

	def union(self, a, b):
		root_a = self.get_root(a)
		self.list[root_a] = self.get_root(b)


class WeightedQuickUnion(object):
	def __init__(self, N):
		self.lst = range(N)
		self.sizes = [1] * N

	def get_root(self, index):
		while ind != self.lst[index]:
			index = self.lst[index]
		return index

	def find(self, a, b):
		return self.get_root(a) == self.get_root(b)

	def union(self, a, b):
		if self.sizes[self.get_root(a)] < self.sizes[self.get_root(b)]:
			self.lst[self.get_root(a)] = self.get_root(b)
			self.sizes[self.get_root(b)] += self.sizes[self.get_root(a)]
		else:
			self.lst[self.get_root(b)] = self.get_root(a)
			self.sizes[self.get_root(a)] += self.sizes[self.get_root(b)]