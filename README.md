# 数据结构与算法
### test1
如果a+b+c = 1000，
且a^2+b^2=c^2，
如何求出所有a,b,c可能的组合？

```
# my best code
start_time = time.time()
for a in range(0,1001):
	for b in range(0,1001-a):
		c = 1000-a-b
		if c<a or c<b: 
			break  # important sentence
		if a*a+b*b==c*c:
			print(a,b,c)
end_time = time.time()
print('Take time:',end_time-start_time)
```

### 算法的概念
算法是独立存在的一种解决问题的方法和思想
### 算法的五大特性
输入
输出
有穷
确定
可行
### 算法效率衡量
- 执行时间（与计算机状态有关）
- 执行基本运算数量（时间复杂度）

### 时间复杂度 
T(n) = 2*n^3+8

g(n) = n^3

**大“O”表示法**：一个计算步骤跟n相关的时候，系数全部忽略掉，之留下最特征的部分，记为T(n)=O(g(n))

**时间复杂度**：假设存在函数g，使得算法A处理规模为n的问题所用时间为T(n)=O(g(n))，则称O(g(n))为算法A的渐近时间复杂度，简称时间复杂度，记为T(n)
### 最坏时间复杂度
最多需要的步骤，在这个数目内一定能解决同类问题。
### 时间复杂度的几条基本计算规则
1. 基本操作，即只有常数项，认为其时间复杂度为O(1)
2. 顺序结构，时间复杂度按加法进行计算
3. 循环结构，时间复杂度按乘法进行计算
4. 条件结构，时间复杂度取最大值
5. 判断一个算法的效率时，往往只需要关注操作数量的最高次项，其它*次要项*和*常数项*可以忽略
6. 在没有特殊说明时，我们所分析的算法的时间复杂度都是指最坏时间复杂度

### 常见的时间复杂度
- O(1)
- O(n)
- O(n^2)
- O(logn)
- O(nlogn)
- O(n^3)
- O(2^n)

### python内置类型性能分析

**timeit模块**可以用来测试一小段Python代码的执行速度。

class timeit.Timer(stmt='pass',setup='pass', timer=<timer function>)

Timer是测量小段代码执行速度的类；

stmt参数是要测试的代码语句（statment）；

setup参数是运行代码时需要的设置，import之类的；

timer参数是一个定时器函数，与平台有关，默认有一个。

timeit.Timer.timeit(number=1000000) 1000000万次平均耗时


```
from timeit import Timer
def t1():
	li = []
	for i in range(1000):
		li = li + [i]
def t2():
	li = []
	for i in range(1000):
		li.extend([i])
def t3():
	li = []
	for i in range(1000):
		li.append(i)
def t4():
	li = [i for i in range(1000)]
def t5():
	li = list(range(1000))

timer1 = Timer("t1()","from __main__ import t1")
print(timer1.timeit(1000))
timer2 = Timer("t2()","from __main__ import t2")
print(timer2.timeit(1000))
timer3 = Timer("t3()","from __main__ import t3")
print(timer3.timeit(1000))
timer4 = Timer("t4()","from __main__ import t4")
print(timer4.timeit(1000))
timer5 = Timer("t5()","from __main__ import t5")
print(timer5.timeit(1000))
```
t1--->t5 耗时越来越少
### 顺序表
将元素顺序地存放在一块连续的存储区里，元素间的顺序关系由它们的存储顺序自然表示
### 顺序表的形式
- 基本形式：数据元素本身连续存储，每个元素所占的存储单元大小固定相同，元素的下标是其逻辑地址，而元素存储的物理地址（实际内存地址）可以通过存储区的起始地址Loc (e0)加上逻辑地址（第i个元素）与存储单元大小（c）的乘积计算而得
- 元素外置的形式：将实际数据元素另行存储，而顺序表中各单元位置保存对应元素的地址信息（即链接）。由于每个链接所需的存储量相同，通过上述公式，可以计算出元素链接的存储位置，而后顺着链接找到实际存储的数据元素。

### 顺序表的结构
- 元素集合
- 整体信息
    - 总容量
    - 已有元素

### 顺序表的扩充策略
- 每次扩充增加固定数目的存储位置，称为线性增长。
- 每次扩充容量加倍，如每次扩充增加一倍存储空间

### 顺序表的两种方式
- 一体式结构

    存储表信息的单元与元素存储区以连续的方式安排在一块存储区形成一个完整的顺序*表对象*。
- 分离式结构
    
    *表对象*里只保存容量和元素个数，实际数据元素存放在另一个独立的元素存储区里，通过链接与基本表对象关联

### python中的顺序表
- list

    - 基于下标的访问，时间复杂度为O(1),所以应该为顺序表
    - 表元素改变，表对象地址不变，采用分离式实现技术
    - 容量可以在使用中动态变化的叫动态顺序表
    - 总结：采用分离式技术实现的动态顺序表

- tupple

### 链表
线性表，在每一个节点（数据存储单元）里存放下一个节点的位置信息（即地址）
### 单向链表
每个节点包含两个域：一个信息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。
### 单链表的操作

- is_empty() 链表是否为空
- length() 链表长度
- travel() 遍历整个链表
- add(item) 链表头部添加元素
- append(item) 链表尾部添加元素
- insert(pos, item) 指定位置添加元素
- remove(item) 删除节点
- search(item) 查找节点是否存在

```
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
```
### 链表与顺序表的对比

链表失去了顺序表随机读取的优点，同时链表由于增加了结点的指针域，空间开销比较大，但对存储空间的使用要相对灵活。

### 单向循环链表
最后一个节点的next为头节点

```
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
```
### 双向链表
每个节点有两个链接：一个指向前一个节点，当此节点为第一个节点时，指向空值；而另一个指向下一个节点，当此节点为最后一个节点时，指向空值。

```
class Node(object):
	"""双向链表节点"""
	def __init__(self, item):
		self.item = item
		self.next = None
		self.prev = None


class DLinkList(object):
	"""双向链表"""
	def __init__(self):
		self._head = None

	def is_empty(self):
		"""判断链表是否为空"""
		return self._head == None

	def length(self):
		"""返回链表的长度"""
		cur = self._head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历链表"""
		cur = self._head
		while cur != None:
			print(cur.item,end=' ')
			cur = cur.next
		print()

	def add(self, item):
		"""头部插入元素"""
		node = Node(item)
		if self.is_empty():
			# 如果是空链表，将_head指向node
			self._head = node
		else:
			# 将node的next指向_head的头节点
			node.next = self._head
			# 将_head的头节点的prev指向node
			self._head.prev = node
			# 将_head 指向node
			self._head = node

	def append(self, item):
		"""尾部插入元素"""
		node = Node(item)
		if self.is_empty():
			# 如果是空链表，将_head指向node
			self._head = node
		else:
			# 移动到链表尾部
			cur = self._head
			while cur.next != None:
				cur = cur.next
			# 将尾节点cur的next指向node
			cur.next = node
			# 将node的prev指向cur
			node.prev = cur



	def search(self, item):
		"""查找元素是否存在"""
		cur = self._head
		while cur != None:
			if cur.item == item:
				return True
			cur = cur.next
		return False

	def insert(self, pos, item):
		"""在指定位置添加节点"""
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			node = Node(item)
			cur = self._head
			count = 0
			# 移动到指定位置的前一个位置
			while count < (pos-1):
				count += 1
				cur = cur.next
			# 将node的prev指向cur
			node.prev = cur
			# 将node的next指向cur的下一个节点
			node.next = cur.next
			# 将cur的下一个节点的prev指向node
			cur.next.prev = node
			# 将cur的next指向node
			cur.next = node        
	def remove(self, item):
		"""删除元素"""
		if self.is_empty():
			return
		else:
			cur = self._head
			if cur.item == item:
				# 如果首节点的元素即是要删除的元素
				if cur.next == None:
					# 如果链表只有这一个节点
					self._head = None
				else:
					# 将第二个节点的prev设置为None
					cur.next.prev = None
					# 将_head指向第二个节点
					self._head = cur.next
				return
			while cur != None:
				if cur.item == item:
					# 将cur的前一个节点的next指向cur的后一个节点
					cur.prev.next = cur.next
					# 将cur的后一个节点的prev指向cur的前一个节点
					cur.next.prev = cur.prev
					break
				cur = cur.next

if __name__ == "__main__":
	ll = DLinkList()
	ll.add(1)
	ll.add(2)
	ll.append(3)
	ll.insert(2, 4)
	ll.insert(4, 5)
	ll.insert(0, 6)
	print("length:",ll.length())
	ll.travel()
	print(ll.search(3))
	print(ll.search(4))
	ll.remove(1)
	print("length:",ll.length())
	ll.travel()                            
```

### 栈
一种容器，后进先出
### 栈的操作

- Stack() 创建一个新的空栈
- push(item) 添加一个新的元素item到栈顶
- pop() 弹出栈顶元素
- peek() 返回栈顶元素
- is_empty() 判断栈是否为空
- size() 返回栈的元素个数


```
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

```

### 队列
先进先出
### 队列的操作
- Queue() 创建一个空的队列
- enqueue(item) 往队列中添加一个item元素
- dequeue() 从队列头部删除一个元素
- is_empty() 判断一个队列是否为空
- size() 返回队列的大小

```
class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        # 后进的后出，所以放list最前面，出的时候取最后一个元素
        self.items.insert(0,item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("1")
    q.enqueue("2")
    q.enqueue("3")
    print q.size()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
```

