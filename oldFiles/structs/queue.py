class DEQUE():
	def __init__(self):
		self.list = []

	def push_back(self, item):
		self.list.append(item)

	def push_front(self, item):
		self.list.insert(0, item)

	def pop_front(self):
		self.list.pop(0)

	def pop_back(self):
		self.list.pop(-1)

	def front(self):
		return self.list[0]		

	def back(self):
		return self.list[-1]

	def size(self):
		return len(self.list)

	def find(self, elem):
		return self.list.find(elem)

	def __getitem__(self, index):
		return self.list[index]


class STACK():
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.append(item)

	def pop(self):
		self.list.pop(-1)

	def front(self):
		return self.list[-1]

	def find(self, elem):
		return self.list.find(elem)

	def size(self):
		return len(self.list)