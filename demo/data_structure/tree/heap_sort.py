"""堆排序

堆：一种完全二叉树的特殊结构
1）大顶堆：父节点的值大于子节点
2）小顶堆：与大顶堆相反
堆排序的基本思想（升序）：
1）将待排序的序列构造成一个大顶堆
2）将堆的根节点与堆的最后一个节点交换
3）将剩余的n-1个元素重新构造成一个堆
4）重复2，3步
"""


def gen_heap(arr, i, length):
	"""将待排序序列构造成大顶堆"""
	k = i * 2 + 1
	while k < length:
		if k+1 < length and arr[k+1] > arr[k]:
			# 左孩子和右孩子相比较
			k += 1
		if arr[k] > arr[i]:
			# 较大的孩子与父节点比较
			arr[k], arr[i] = arr[i], arr[k]
			i = k
		else:
			break
		k = 2 * i + 1

def heap_sort(arr):
	"""堆排序"""
	# 构建堆
	n = (len(arr) - 2) // 2
	for i in range(n, -1, -1):
		gen_heap(arr, i, len(arr))
	# 将堆顶元素与末尾元素相交换
	for j in range(len(arr)-1, 0, -1):
		arr[0], arr[j] = arr[j], arr[0]
		gen_heap(arr, 0, j)


if __name__ == '__main__':
	arr = [54,226,93,17,77,31,44,55,20]
	heap_sort(arr)
	print(arr)