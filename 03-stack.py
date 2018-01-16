class Stack(object):
	"""栈"""
	def __init__(self):
		self._list = []

	def push(self,item):
		self._list.append(item)

	def pop(self):
		return self._list.pop()

	def peek(self):
		'''返回栈顶元素，但是不取出'''
		if self._list:
			return self._list[-1]
		else:
			return None

	def is_empty(self):
		return self._list == []

	def size(self):
		return len(self._list)

if __name__ == "__main__":
	s = Stack( )
	s.push(1)
	s.push(2)
	s.push(3)
	print("pop:",s.pop())
	print("peek:",s.peek())
	print("empty:",s.is_empty())
	print("size:",s.size())
	print("pop:",s.pop())
