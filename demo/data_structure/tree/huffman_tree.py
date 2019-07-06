"""霍夫曼树

概念：带权路径（wpl 【weighted path lenght of tree】）最小的二叉树
"""
from binary_tree import BinaryTree, Node


def gen_huffman_tree(arr):
    """生成霍夫曼树"""
    li = list()
    for v in arr:
        node = Node(v)
        li.append(node)
    while len(li) > 1:
        # 根据节点的权重值对节点进行排序
        li.sort(key=lambda n: n.data)
        # 取出前两个树构造新树
        n1 = li.pop(0)
        n2 = li.pop(0)
        new_node = Node(n1.data + n2.data)
        new_node.lchild = n1
        new_node.rchild = n2
        li.append(new_node)
    return BinaryTree(li.pop(0))


if __name__ == '__main__':
    arr = [2, 0, 1, 6, 2, 1, 4, 3, 0, 9]
    huffman_tree = gen_huffman_tree(arr)
    huffman_tree.pre_order_traverse(huffman_tree.root)
    print('')
    huffman_tree.in_order_traverse(huffman_tree.root)

