# 约瑟夫问题：
# 假设n个小孩围成一个圈，从第k个小孩开始（1<=k<=n）,从1开始报数，报数为m的小孩出列，
# 接下从出列的小孩下个位置开始继续报数,到m则出列，并继续重复上述过程
# 问：小孩出列顺序
import sys
sys.path.append('../../demo/data_structure/')
from single_circle_link_list import SingleCircleLinkList

def get_josephu_list(cll, k, m):
	"""使用单向循环队列实现约瑟夫问题
		k 开始报数的位置
		m 报数的界限
	"""
	length = cll.length
	if not length:
		return []

	if any([k < 1, k > length, m < 1]):
		print('参数违法！')
		return
	res = []
	cur = cll.head
	# 移动到开始报数的位置
	for i in range(k - 1):
		cur = cur.next
	if m == 1:
		start = cur
		# 当k=1时，指针移动时无法定位到要删除的前一个元素，因此单独拿出来处理
		# 此时相当于遍历整个链表
		while cur.next is not start:
			res.append(cur.data)
			cur = cur.next
		res.append(cur.data)
		return res
	while cur.next is not cur:
	# 移动到报数结束的前一个位置
		for i in range(m - 2):
			cur = cur.next

		res.append(cur.next.data)

		cur.next = cur.next.next
		cur = cur.next
	res.append(cur.data)
	return res

if __name__ == '__main__':
	cll = SingleCircleLinkList()
	cll.append('小黑')
	cll.append('小白')
	cll.append('小红')
	cll.append('小绿')
	res = get_josephu_list(cll, 2, 2)
	print(res)
