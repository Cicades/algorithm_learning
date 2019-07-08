"""使用栈实现表达式的计算（前缀表达式版）
思路：
1.依次扫面待计算的表达
2.遇到数字则存入数字栈
3.遇到运算符
  3.1如果运算符栈为空，则直接入栈
  3.2如果运算符栈不为空
	3.2.1 如果待入栈的运算符的优先级大于栈顶的运算符，则直接入栈
	3.2.2 反之，如果其优先级小于等于栈顶的运算符，则从数字栈弹出两个数字，从运算符栈弹出一个运算符，将三者的运算结果入数字栈，最后等待的运算符入栈
"""
import sys

sys.path.append('../../../demo/others/')

from sequence_stack import SequenceStack

class Calculator(object):
	"""使用栈模拟计算机"""
	_instance = None # 存放唯一的实例对象
	_init_flag = False

	def __new__(cls, *args, **kwargs):
		cls._instance = super().__new__(cls) if cls._instance is None else cls._instance # 实现单例模式
		return cls._instance

	def __init__(self):
		if Calculator._init_flag:
			return
		self.num_stack = SequenceStack(10) # 数字栈
		self.oper_stack = SequenceStack(10) # 运算符栈
		self.operators = {
			'-': 0,
			'+': 0,
			'*': 1,
			'/': 1
		} # 支持的运算符
		Calculator._init_flag = True

	def is_num(self, char):
		"""判断字符的类型
		
		Arguments:
			char {str}
		
		Returns:
			bool
		
		Raises:
			Exception
		"""
		if char.isdigit():
			return True
		elif char in self.operators.keys():
			return False
		else:
			raise Exception('表达式包含非法字符！')

	def calculate(self, num1, num2, operator):
		"""计算两个数字和一个运算符的值
		
		Arguments:
			num1 {int}
			num2 {int}
			operator {str}
		"""
		if operator == '-':
			return (num1 - num2)
		elif operator == '+':
			return (num1 + num2)
		elif operator == '/':
			return (num1 / num2)
		elif operator == '*':
			return (num1 * num2)
	

	def compare_weight(self, opre1, oper2):
		"""比较权重"""
		if self.operators[opre1] > self.operators[oper2]:
			# 运算符1的权重大于运算符2
			return True
		else:
			return False

	def run(self, expression):
		"""计算表达式的结果并返回"""
		expression = expression.strip() # 去除两端空白字符
		l = len(expression)
		index = 0 # 表达式扫描的下表
		while index < l:
			char = expression[index]
			if self.is_num(char):
				count = 0
				while (index + count) < l and self.is_num(expression[index + count]):
					count += 1
				self.num_stack.push(int(expression[index: index + count]))
				index += count
			else:
				# 待入栈字符为运算符
				if self.oper_stack.is_empty():
					# 运算符栈为空
					self.oper_stack.push(char)
				else:
					if self.compare_weight(char, self.oper_stack.peek()):
						# 带插入元素权重大于栈顶元素
						self.oper_stack.push(char)
					else:
						num2 = self.num_stack.pop()
						num1 = self.num_stack.pop()
						operator = self.oper_stack.pop()
						temp_res = self.calculate(num1, num2, operator)
						self.num_stack.push(temp_res)
						self.oper_stack.push(char)
				index += 1

		# 表达式遍历完毕
		while not self.oper_stack.is_empty():
			num2 = self.num_stack.pop()
			num1 = self.num_stack.pop()
			operator = self.oper_stack.pop()
			temp_res = self.calculate(num1, num2, operator)
			self.num_stack.push(temp_res)

		return self.num_stack.pop()

if __name__ == '__main__':
	
	cal = Calculator()
	res = cal.run('10*20/200+1')
	print(res)