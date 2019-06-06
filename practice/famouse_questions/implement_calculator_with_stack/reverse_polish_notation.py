"""使用逆波兰表达式实现计算器的功能
（1）逆波兰表示又称后缀表达式
（2）中缀表达式符合人类的认知习惯，但不利于计算机计算，所以一般是将中缀表达式转换成逆波兰表达式，再进行计算

（3）中缀表达式转逆波兰表达式：
	1.使用两个栈分别存储运算符（s1）和临时转换结果(s2)
	2.从左至右扫描中缀表达式
	  2.1扫描的字符是数字，直接插入s2
	  2.2扫描的字符是运算符
		2.2.1 如果s1为空，直接入s1
		2.2.2 如果s1不为空
			2.2.2.1 如果待入栈运算符的优先级小于或等于s1栈顶运算符则（或者s1的栈顶字符是'('），
					则将s1栈顶运算符取出并入s2栈，一直重复上述过程，直到不满足条件
			2.2.2.2 反之，将运算符入s1栈
	  2.3扫描的字符是'(',直接入s1栈
	  2.4扫描的字符是')',不断从s1弹出元素并入s2，直到弹出的元素为'('
	3.中缀表达式扫描完毕，将s1中的所有元素依次弹出并入s2栈
	4.至此，从s2的栈底到栈顶存储的便是逆波兰表达式

 (4) 逆波兰表达式计算：
 	0.使用一个栈存储数字
	1.从左至右依次扫描
	2.字符为数字则压入栈
	3.字符为运算符则从栈依次弹出两个元素进行相应的运算，并将结果入栈
	4.当表达式扫描完毕，数字栈仅剩一个元素，即是表达式的运算结果
"""

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
		if isinstance(char, int):
			return 1
		if char.isdigit():
			return 1
		elif char in self.operators.keys():
			return 0
		elif char == ')':
			return -1
		elif char == '(':
			return -2
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
		if oper2 == '(':
			return True
		if self.operators[opre1] > self.operators[oper2]:
			# 运算符1的权重大于运算符2
			return True
		else:
			return False

	def infix_to_suffix(self, expression):
		"""中缀表达式转换为逆波兰表达式, 
		为简化操作多位数的操作，输入中缀表达式，数字与字符之间以空格隔开
		"""
		res = list() # 结果栈
		opers = list() # 运算符栈
		char_li = expression.split(' ')
		for char in char_li:
			char_type = self.is_num(char) # 字符串类型 ==> 1：数字; 0：运算符; -1：')';-2: '('
			if char_type == 1:
				res.append(int(char))
			elif char_type == 0:
				if not opers:
					# 运算符栈为空
					opers.append(char)
				else:
					# 运算符栈不为空
					if self.compare_weight(char, opers[-1]):
						opers.append(char)
					else:
						temp_char = opers[-1]
						while not self.compare_weight(char, temp_char):
							res.append(opers.pop(-1))
							if not opers:
								break
							temp_char= opers[-1]
						opers.append(char)
			elif char_type == -1:
				while opers[-1] != '(':
					res.append(opers.pop(-1))
				opers.pop(-1)
			else:
				opers.append(char)

		while opers:
			res.append(opers.pop(-1))
		return res


	def calculate_with_suffix_notaion(self, suffix_notation):
		"""根据后缀表达式计算结果"""
		nums = list()
		for char in suffix_notation:
			char_type = self.is_num(char)
			if char_type == 1:
				nums.append(char)
			elif char_type == 0:
				num1 = nums.pop(-1)
				num2 = nums.pop(-1)
				res = self.calculate(num2, num1, char)
				nums.append(res)
		return nums.pop(-1)

	def run(self, infix_expression):
		"""计算表达式的结果并返回"""
		suffix_notation = self.infix_to_suffix(infix_expression)
		return self.calculate_with_suffix_notaion(suffix_notation)

if __name__ == '__main__':
	calculator = Calculator()
	infix_expression = '1 + 2 * 3 - ( 4 / 4 )'
	print(calculator.run(infix_expression))