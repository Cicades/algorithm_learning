"""插值查找

插值查找由二分查找演变而来，是针对关键字分布较为均匀的情况所做的优化,例如查找顺序数列[1,2,3...100]中的任何一个数，只需一趟便能获得结果

二分查找：mid = (low + high) / 2 => mid = low + 1/2 * (high -low)

插值查找：mid = low + (find_val - arr[low])/(arr[high] - arr[low]) * (high - low)
"""

def insert_value_sort(arr, find_val, low=0, high=-1):
	"""插值排序"""
	if low > high:
		return -1
	mid = low + int((find_val - arr[low]) / (arr[high] - arr[low]) * (high -low))
	if arr[mid] == find_val:
		return mid
	elif find_val < arr[mid]:
		return insert_value_sort(arr, find_val, low, mid-1)
	else:
		return insert_value_sort(arr, find_val, mid+1, high)

if __name__ == '__main__':
	li = [17, 20, 26, 31, 44, 45, 53, 56, 77, 93]
	res = insert_value_sort(li, find_val=45, low=0, high=len(li)-1)
	print(res)