"""哈希表

散列表（Hash table，也叫哈希表），是根据关键码值(Key value)而直接进行访问的数据结构。
也就是说，它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。
这个映射函数叫做散列函数，存放记录的数组叫做散列表

实例：
1.使用hash表存储学生的学号和姓名
2.使用顺序表加链表来构建哈希表
3.哈希函数采用取模
"""

class Student(object):
	"""学生结点"""
	def __init__(self, stu_id=None, stu_name=None):
		self.stu_id = stu_id
		self.stu_name = stu_name
		self.next = None


class StudentList(object):
	"""学生链表"""
	def __init__(self):
		self.head = None

	def append(self, stu_id, stu_name):
		"""追加元素"""
		stu = Student(stu_id, stu_name)
		if self.head is None:
			self.head = stu
			return
		cur = self.head
		while cur.next is not None:
			cur = cur.next
		cur.next = stu

	def traverse(self):
		"""遍历链表"""
		if self.head is None:
			print('链表为空！')
			return
		cur = self.head
		while cur.next is not None:
			print('(id:{}, name:{})'.format(cur.stu_id, cur.stu_name), end='  ')
			cur = cur.next
		print('(id:{}, name:{})'.format(cur.stu_id, cur.stu_name))

	def find_by_id(self, stu_id):
		"""根据id返回学生信息"""
		if self.head is None:
			return None
		cur = self.head
		while cur is not None:
			if cur.stu_id == stu_id:
				break
			cur = cur.next
		return cur


class HashTable(object):
	"""哈希表"""
	def __init__(self, lenght):
		"""根据给定的长度初始化hash表"""
		self.body = [StudentList() for x in range(lenght)]
		self.lenght = lenght

	def add(self, stu_id, stu_name):
		"""添加学生信息"""
		stu_li = self.body[self.hash_fun(stu_id)] # 确定学生存储的位置
		stu_li.append(stu_id, stu_name)


	def hash_fun(self, id):
		"""散列函数，根据id返回存储的位置"""
		return id % self.lenght

	def show_all(self):
		"""遍历整个hash表"""
		for index, stu_li in enumerate(self.body):
			print('{}:'.format(index))
			stu_li.traverse()

	def find_by_id(self, stu_id):
		"""根据id返回学生信息"""
		res = self.body[self.hash_fun(stu_id)].find_by_id(stu_id)
		return res


if __name__ == '__main__':
	from random import randint
	h = HashTable(5)
	h.add(randint(1, 100), '鸣人')
	h.add(randint(1, 100), '佐助')
	h.add(randint(1, 100), '小樱')
	h.add(randint(1, 100), '春野')
	h.add(randint(1, 100), '鹿丸')
	h.add(randint(1, 100), '丁次')
	h.add(randint(1, 100), '袁飞日斩')
	h.add(10, '月光疾风')
	h.show_all()
	res = h.find_by_id(10)
	print('id为10的学生姓名为：' + res.stu_name)