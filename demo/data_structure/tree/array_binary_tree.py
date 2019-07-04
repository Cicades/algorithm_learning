"""顺序存储二叉树

用顺序表存储二叉树的数据
关键点：
1.顺序存储二叉树一般只考虑完全二叉树
2.下标为n的节点的左孩子的下标为2n+1，右孩子下标为2n+2，父节点的下标为(n-1)/2
"""

class ArrayBinaryTree(object):
	"""顺序存储二叉树"""
	def __init__(self, arr=[]):
		self.arr = arr

	def pre_order_traverse(self, index=0):
		"""先序遍历"""
		if index > len(self.arr) - 1:
			return
		print(self.arr[index], end=' ')
		self.pre_order_traverse(2 * index + 1)
		self.pre_order_traverse(2 * index + 2)

if __name__ == '__main__':
	tree = ArrayBinaryTree(list(range(10)))
	tree.pre_order_traverse()
