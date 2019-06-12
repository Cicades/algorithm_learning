def gen_fibonacci(count):
	"""生成Fibonacci数列"""
	res = [1, 1]
	a, b = 1, 1
	while count:
		c = a + b
		res.append(c)
		a, b = b, c
		count -= 1
	return res

if __name__ == '__main__':
	print(gen_fibonacci(10))
