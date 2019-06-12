"""斐波那契查找法（黄金分割法）
利用斐波那契数列（从第三项开始）F(k-1)/F(k)近似0.618(黄金分割)特性，不断缩小查找范围

1.F(k) = F(k-1) + F(k -2) => 为方便确定mid的下标可转化为： F(k)-1 = (F(k-1)-1) + 1 + (F(k -2)-1)
2.mid=low + F(k-1)-1
3.当待查询的数组的长度不足F(k)-1时，使用数组的最后一项进行填充
"""

class FibonacciSearch(object):
	"""斐波那契查找"""
	def __init__(self):
		self.fibonacci_li = list() # Fibonacci数列

	def gen_fibonacci(self, l):
		"""根据待查寻数列的长度生成Fibonacci数列"""
		res = [1, 1]
		a, b = 1, 1
		c = a + b
		while l > c - 1:
			res.append(c)
			a, b = b, c
			c = a + b
		res.append(c)
		self.fibonacci_li = res

	def search(self, arr, val):
		"""查找"""
		if val < arr[0] or val > arr[-1]:
			# 待查询数值超出数组范围
			return -1
		l = len(arr) # 数组的长度
		self.gen_fibonacci(l)
		gap = self.fibonacci_li[-1] - l # 带查询数组长度与理想长度差
		temp_li = arr + [arr[-1] for x in range(gap)] # 填充数组
		low = 0
		high = l - 1
		k = len(self.fibonacci_li) - 1 # fibonacci数组的下标
		while low <= high:
			mid = low + self.fibonacci_li[k-1] - 1
			if temp_li[mid] == val:
				if mid <= high:
					return mid
				else:
					return high
			elif val < temp_li[mid]:
				high = mid - 1
				k -= 1
			else:
				low = mid + 1
				k -= 2
		return -1

if __name__ == '__main__':
	li = [17, 20, 26, 31, 44, 45, 53, 56, 77, 93]
	f = FibonacciSearch()
	print(f.search(li, 93))


			
			
