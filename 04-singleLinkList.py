# 节点实现
class SingleNode(object):
	def __init__(self,item):
		# 元素
		self.item = item
		# 下一节点
		self.next = None

# 单链表的实现
class SingleLinkList(object):
	def __init__(self):
		self.__head = None

	def is_empty(self):
		return self.__head == None

	def length(self):
		current = self.__head
		count = 0
		while current != None:
			count += 1
			current = current.next
		return count

	def travel(self):
		# 遍历
		current = self.__head
		while current != None:
			print(current.item,end=' ')
			current = current.next
		print()

	def add(self, item):
		# 头部添加元素
		node = SingleNode(item)
		node.next = self.__head
		self.__head = node

	def append(self,item):
		# 尾部添加元素
		node = SingleNode(item)
		if self.is_empty():
			self.__head = node
		else:
			current = self.__head
			while current.next != None:
				current = current.next
			current.next = node

	def insert(self,pos,item):
		# 在指定位置添加元素
		node = SingleNode(item)
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
		while current != None:
			if current.item == item:
				# 如果这是第一个节点
				if not pre:
					self.__head = current.next
				else:
					pre.next = current.next
				break
			else:
				pre = current
				current = current.next
	def search(self,item):
		# 查看元素是否存在
		current = self.__head
		while current != None:
			if current.item == item:
				return True
			current = current.next
		return False

if __name__ == '__main__':
	ll = SingleLinkList()
	ll.add(1)
	ll.add(2)
	ll.append(3)
	ll.insert(2,4)
	print(ll.length)
	ll.travel()
	print(ll.search(3))
	print(ll.search(5))
	ll.remove(1)
	print(ll.length())
	ll.travel()