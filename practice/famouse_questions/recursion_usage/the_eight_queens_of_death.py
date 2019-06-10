"""八皇后问题（回溯算法）

"""

class EightQueens(object):
	"""八皇后问题"""
	_QUEENS = 8 # 皇后数
	_SIZE = 8 # 棋盘大小8*8

	def __init__(self):
		self.res = list(range(EightQueens._QUEENS)) # 存放结果
		self.count = 0 # 存放可行解法数量

	def print_res(self):
		"""打印结果"""
		for val in self.res:
			print(val, end=' ')
		print('\r')

	def judge(self, n):
		"""判断第n个皇后是否和前n-1个的位置冲突"""
		for i in range(n):
			if self.res[i] == self.res[n] or abs(n - i) == abs(self.res[i] - self.res[n]):
				# 判断是否处于同一列或者对角线
				return False
		return True

	def place_queen(self, n):
		"""放置第n个皇后"""
		if EightQueens._QUEENS == n:
			# n从0开始，当n等于8时，意味开始放置第9皇后，即已求解出八皇后的位置
			# 并开始回溯，进行下一轮求解
			self.print_res()
			self.count += 1
			return 
		for i in range(EightQueens._SIZE):
			# 确定皇后在当前行的位置
			self.res[n] = i
			if self.judge(n):
				# 如果不冲突，则排放下一个皇后
				self.place_queen(n+1)
			# 如果冲突则进入下一次循环，即将皇后摆放至下一列
	
	def run(self):
		"""开启八皇后求解"""
		self.place_queen(0)
		print('共有{}种解法'.format(self.count))

if __name__ == '__main__':
	queens = EightQueens()
	queens.run()

