# 顺序栈
# 先进后出

class SequenceStack(object):
	"""顺序栈的实现"""
	def __init__(self, maxsize=0):
		self.top = -1 # 栈顶
		self.bottom = 0 # 栈底
		self.maxsize = maxsize # 最大容量
		self.__body = list(range(maxsize)) # 存储栈元素的列表

	def is_empty(self):
		"""栈是否为空"""
		return self.top == -1

	def is_full(self):
		"""判断栈是否为满"""
		return self.top == self.maxsize - 1

	def push(self, data):
		"""入栈"""
		if self.is_full():
			print('栈已满！')
			return

		self.top += 1
		self.__body[self.top] = data

	def pop(self):
		"""出栈"""
		if self.is_empty():
			print('栈已空！')
			return
		val = self.__body[self.top]
		self.top -= 1
		return val

	def peek(self):
		"""查看栈顶元素"""
		return self.__body[self.top]

	def traverse(self):
		for i in range(self.top + 1):
			print(self.__body[i], end=' ')
