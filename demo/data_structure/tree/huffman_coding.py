"""霍夫曼编码
霍夫曼编码是在变长编码的基础上改进的一种编码模式，广泛应用于数据压缩，且是一种前缀编码
前缀编码：任何一种编码都不能是另外一种编码的前缀
"""


class Node(object):
    """节点类"""
    def __init__(self, data, weight):
        self.data = data  # 字符数据
        self.weight = weight  # 权重
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


class HuffmanCoding(object):
    """霍夫曼编码"""
    def __init__(self, string):
        self.string = string
        self.char_count_dict = dict()
        self.huffman_code_map = dict()

    def count_char(self):
        """统计待压缩字符串中个字符出现的次数"""
        res = dict()
        for char in self.string:
            if char not in res:
                res[char] = 1
            else:
                res[char] += 1
        self.char_count_dict = res

    def gen_huffman_tree(self):
        """生成霍夫曼树"""
        nodes_li = list()
        for key, val in self.char_count_dict.items():
            node = Node(key, val)
            nodes_li.append(node)
        while len(nodes_li) > 1:
            nodes_li.sort(key=lambda n: n.weight)
            n1 = nodes_li.pop(0)
            n2 = nodes_li.pop(0)
            new_node = Node(data=None, weight=n1.weight+n2.weight)  # 构造新的节点
            new_node.lchild = n1
            new_node.rchild = n2
            nodes_li.append(new_node)
        return nodes_li.pop(0)

    def gen_huffman_code_map(self, root):
        """生成霍夫曼编码对照表
        向左的路径为0
        向右的路径为1
        """
        self.pre_order_traverse(root, '', '')

    def pre_order_traverse(self, cur, code, codes):
        """前序遍历"""
        # 处理当前节点
        if cur is None:
            return
        codes += code
        if cur.data is not None:
            self.huffman_code_map[cur.data] = codes
        self.pre_order_traverse(cur.lchild, '0', codes)
        self.pre_order_traverse(cur.rchild, '1', codes)

    def compress(self):
        """根据生成霍夫曼编码表对数据压缩"""
        res = ''
        nums = list()
        for c in self.string:
            res += self.huffman_code_map[c]
        for i in range(0, len(res), 8):
            if i+8 <= len(res):
                nums.append(int(res[i:i+8], 2))
            else:
                nums.append(int(res[i:], 2))
        return nums

    def run(self):
        self.count_char()  # 统计字符
        root = self.gen_huffman_tree()  # 生成霍夫曼树
        self.gen_huffman_code_map(root)  # 生成霍夫曼编码对照表
        return self.compress()


if __name__ == '__main__':
    string = 'i like like like java do you like a java'
    huffman_coding = HuffmanCoding(string)
    res = huffman_coding.run()
    print(res)
    print(len(res))
