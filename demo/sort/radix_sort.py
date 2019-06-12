"""基数排序

以空间换时间的经典排序算法
"""

def radix_sort(arr):
	"""基数排序"""
	max_digits = len(str(max(arr))) # 待排序序列中最大数的位数，这里假设待排序的数都是非负整数
	buckets = [ [] for i in range(10) ] # 桶
	for i in range(max_digits):
		# 从低位到高位进行排序
		for val in arr:
			# 将待排序的数列加入桶
			digit = val // 10 ** i % 10
			buckets[digit].append(val)
		arr.clear() # 将排序的数组进行清空，也可写成 arr=[]
		for bucket in buckets:
			# 从桶中取出元素，还原成一维数组，交付下次排序
			while bucket:
				arr.append(bucket.pop(0))
	return arr

if __name__ == '__main__':
	arr = [10, 1, 355, 76, 24, 102, 233, 8]
	print(radix_sort(arr))