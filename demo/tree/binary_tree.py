# 二叉樹

class Node(object):
	"""节点类"""
	def __init__(self, data):
		self.data = data
		self.lchild = None # 左孩子
		self.rchild = None # 右孩子

class BinaryTree(object):
	"""二叉樹"""
	def __init__(self, node=None):
		self.root = node

	def breadth_travel(self):
		"""广度优先遍历"""
		if self.root is None:
			print('二叉树为空！')
			return
		queque = [self.root]
		while queque:
			cur_node = queque.pop(0)
			print(cur_node.data, end=' ')
			if cur_node.lchild:
				queque.append(cur_node.lchild)
			if cur_node.rchild:
				queque.append(cur_node.rchild)
		print('\n广度遍历结束!')

	def add(self, data):
		"""在完全二叉树的末尾添加节点"""
		node = Node(data)
		if self.root is None:
			self.root = node
			return
		queque = [self.root]
		while queque:
			cur_node = queque.pop(0)
			if cur_node.lchild is None:
				cur_node.lchild = node
				return
			else:
				queque.append(cur_node.lchild)
			if cur_node.rchild is None:
				cur_node.rchild = node
				return
			else: 
				queque.append(cur_node.rchild)

	def delete(self, cur, data):
		"""删除节点(假设删除的都是叶子结点)"""
		if cur is None:
			print('二叉树为空！')
			return

		if cur.lchild:
			if cur.lchild.data == data:
				cur.lchild = None
				print('删除成功！')
				return
			else:
				self.delete(cur.lchild, data)

		if cur.rchild:
			if cur.rchild.data == data:
				cur.rchild = None
				print('删除成功！')
				return
			else:
				self.delete(cur.rchild, data)
			
	def pre_order_traverse(self, root):
		"""先序遍历（先根序遍历）"""
		if root is None:
			return
		print(root.data, end=' ')
		self.pre_order_traverse(root.lchild)
		self.pre_order_traverse(root.rchild)

	def in_order_traverse(self, root):
		"""中序遍历"""
		if root is None:
			return
		self.in_order_traverse(root.lchild)
		print(root.data, end=' ')
		self.in_order_traverse(root.rchild)



if __name__ == '__main__':
	binary_tree = BinaryTree()
	for i in range(10):
		binary_tree.add(i)
	binary_tree.breadth_travel()
	print('先根序遍历：', end='')
	binary_tree.pre_order_traverse(binary_tree.root)
	print('中根序遍历：', end='')
	binary_tree.in_order_traverse(binary_tree.root)
	print('')
	binary_tree.delete(binary_tree.root, 10)
	binary_tree.breadth_travel()