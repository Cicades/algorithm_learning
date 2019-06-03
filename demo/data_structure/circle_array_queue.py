# 循环队列
# 关键点：
# 1. front指向队列第一个元素
# 2. rear指向队列最后一个元素的下一个元素
# 3. 判空： front = rear
# 4. 判满： (rear + 1) % max_size = front,（rear+1）是为了与判空的添加区别开来

class CircleArrayQueue(object):
	"""顺序循环队列"""
	def __init__(self, max_size=0):
		self.__front = 0
		self.__rear = 0
		self.__max_size = max_size + 1
		self.__body = list(range(self.__max_size)) # 因为实现的队列为了判空方便会预留一个空元素，所以将用户传入的max_size加一

	def is_empty(self):
		return self.__front == self.__rear

	def is_full(self):
		return (self.__rear + 1) % self.__max_size == self.__front

	def enter_queue(self, data):
		"""入队"""
		if self.is_full():
			print('队列已满！')
			return
		self.__body[self.__rear] = data
		self.__rear = (self.__rear + 1) % self.__max_size

	def leave_queue(self):
		"""出队"""
		if self.is_empty():
			print('队列已空！')
			return
		val = self.__body[self.__front]
		self.__front = (self.__front + 1) % self.__max_size
		return val

	@property
	def length(self):
		"""返回队列的长度"""
		return (self.__rear + self.__max_size - self.__front) % self.__max_size

	def traverse(self):
		"""遍历"""
		if self.is_empty():
			print('队列为空！')
		for i in range(self.length):
			print(self.__body[self.__front + i], end=' ')
		print('\n遍历结束！')

if __name__ == '__main__':
	q = CircleArrayQueue(3)
	q.leave_queue()
	print('队列的长度为：' + str(q.length))
	print('队列是否为空：' + str(q.is_empty()))
	q.enter_queue(1)
	q.enter_queue(2)
	q.enter_queue(3)
	q.enter_queue(4)
	print('队列是否为满:' + str(q.is_full()))
	print('队列的长度为：' + str(q.length))
	q.traverse()
	for i in range(4):
		q.leave_queue()