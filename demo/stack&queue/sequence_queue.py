# 队列的实现，使用顺序表
# 

class Queue(object):
	"""队列的实现"""
	def __init__(self, maxsize=0):
		self.__head = -1 # 队头指针,指向队列第一个元素的前一个元素 
		self.__rear = -1 # 队尾指针，指向队列最后一个元素
		self.__maxsize = maxsize # 队列的最大容量
		self.__body = list(range(3))

	def is_empty(self):
		"""判断队列是否为空"""
		return self.__head == self.__rear

	def is_full(self):
		"""判断队列是否为满"""
		return self.__rear == self.__maxsize - 1
	
	def get_queue(self):
		"""出队"""
		if self.is_empty():
			print('队列为空！')
			return
		self.__head += 1
		return self.__body[self.__head]

	def enter_queue(self, data):
		"""入队"""
		if self.is_full():
			print('队列已满，不能添加元素！')
			return
		self.__rear += 1
		self.__body[self.__rear] = data

if __name__ == '__main__':
	queue = Queue(3)
	queue.enter_queue(3)
	queue.enter_queue(2)
	queue.enter_queue(1)