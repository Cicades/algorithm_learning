def gen_yanghuitriangel(num_rows):
	"""生成杨辉三角"""
	res = []
	for i in range(num_rows):
		row = []
		for j in range(i+1):
			if j == 0 or j == i:
				row.append(1)
				continue
			temp = res[i-1][j-1] + res[i-1][j]
			row.append(temp)
		res.append(row)
	return res

if __name__ == '__main__':
	res = gen_yanghuitriangel(5)
	print(res)