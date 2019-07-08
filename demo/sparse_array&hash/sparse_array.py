# 稀疏矩阵
# 稀疏矩阵的每个元素都是一个三元组，
# 其中第一个三元组记录原矩阵的维数以及非零元素的个数，
# 剩下的三元组记录着原矩阵中非0元素的横纵坐标以及值
def compress(arr):
	"""将普通二维矩阵压缩成稀疏矩阵"""
	res = []
	if not arr:
		return res
	row = len(arr)
	col = len(arr[0])
	count = 0 # 非0数值的个数
	res.append([row, col, count])
	for i in range(row):
		for j in range(col):
			if arr[i][j] != 0:
				res.append([ i, j, arr[i][j] ])
				count += 1
	res[0][-1] = count
	return res

def extract(arr):
	"""将系数矩阵还原成普通矩阵"""
	row = arr[0][0]
	col = arr[0][1]
	if not row:
		return []
	res = list()
	for i in range(row):
		res.append(list([0] * col))

	for item in arr[1:]:
		res[item[0]][item[1]] = item[-1]
	return res



if __name__ == '__main__':
	arr = []
	for i in range(10):
		arr.append(list([0] * 10))

	arr[0][-2] = 1
	arr[3][5] = 2

	sparse_arr = compress(arr)
	print(sparse_arr)
	extract_arr = extract(sparse_arr)
	print(extract_arr)