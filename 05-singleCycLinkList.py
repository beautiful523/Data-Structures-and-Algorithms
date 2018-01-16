# 节点实现
class SingleNode(object):
	def __init__(self,item):
		# 元素
		self.item = item
		# 下一节点
		self.next = None

# 单链表的实现
class SingleCycLinkList(object):
	def __init__(self):
		self.__head = None

	def is_empty(self):
		return self.__head == None

	def length(self):
		if self.is_empty():
			return 0
		current = self.__head
		count = 1
		while current.next != self.__head:
			count += 1
			current = current.next
		return count

	def travel(self):
		# 遍历
		current = self.__head
		print(current.item,end=' ')
		while current.next != self.__head:
			current = current.next
			print(current.item,end=' ')
		print()

	def add(self, item):
		# 头部添加元素
		node = SingleNode(item)
		if self.is_empty():
			self.__head = node
			node.next = self.__head
		else:
			# 先把头元素与新元素连接
			node.next = self.__head
			current = self.__head
			while current.next != self.__head:
				current = current.next
			# 再把尾元素与新元素连接
			current.next = node
			# 再把新元素设置为头元素
			self.__head = node

	def append(self,item):
		# 尾部添加元素
		node = SingleNode(item)
		if self.is_empty():
			self.__head = node
			node.next = self.__head
		else:
			current = self.__head
			while current.next != self.__head:
				current = current.next
			current.next = node
			node.next = self.__head

	def insert(self,pos,item):
		# 在指定位置添加元素
		node = SingleNode(item)
		if pos == 0:
			self.add(item)
		else:
			count = 0
			# pre指定位置的前一个位置
			pre = self.__head
			while count < (pos-1):
				pre = pre.next
				count += 1
			node.next = pre.next
			pre.next = node

	def remove(self, item):
		# 删除节点
		current = self.__head
		pre = None
		# 如果头节点就是item
		if current.item == item:
			if current.next != self.__head:
				# 如果不止一个节点
				while current.next != self.__head:
					current = current.next
				current.next = self.__head.next
				self.__head = self.__head.next
			else:
				self.__head = None
		else:
			pre = self.__head
			while current.next != self.__head:
				if current.item == item:
					pre.next = current.next
					return
				else:
					pre = current
					current = current.next
			# 判断最后一个元素
			if current.item == item:
				pre.next = current.next


	def search(self,item):
		# 查看元素是否存在
		current = self.__head
		if current.item == item:
			return True
		while current.next != self.__head:
			current = current.next
			if current.item == item:
				return True
		return False

if __name__ == '__main__':
	ll = SingleCycLinkList()
	ll.add(1)
	ll.add(2)
	ll.append(3)
	ll.insert(2,4)
	ll.insert(4, 5)
	ll.insert(0, 6)
	print(ll.length())
	ll.travel()
	print(ll.search(3))
	print(ll.search(7))
	ll.remove(1)
	print(ll.length())
	ll.travel()