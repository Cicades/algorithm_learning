"""线索化二叉树

普通的二叉树有2n-(n-1)=n+1指针域被闲置，为了有效利用这些空指针，
规定将节点左空指针指向其前驱节点，右空指针指向其后继节点，由此构成线索二叉树
根据节点线索化的顺序不同，可分为前序线索化二叉树，中序...，后序...

"""
# 二叉樹


class Node(object):
    """节点类"""
    def __init__(self, data):
        self.data = data
        self.lchild = None # 左孩子
        self.rchild = None # 右孩子
        self.pointer_type = {'left': 0, 'right': 0} # 指针的类型，0代表指向子树，1代表指向前驱或者后继


class ThreadedBinaryTree(object):
    """二叉樹"""
    def __init__(self, node=None):
        self.root = node
        self.pre = None

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

    def infix_threaded(self, cur):
        """中序线索化二叉树"""
        if cur is None:
            return
        # 线索化左子树
        self.infix_threaded(cur.lchild)
        # 处理当前节点
        if cur.lchild is None:
            cur.lchild = self.pre
            cur.pointer_type['left'] = 1
        if self.pre and self.pre.rchild is None:
            self.pre.rchild = cur
            self.pre.pointer_type['right'] = 1
        self.pre = cur
        # 线索化右子树
        self.infix_threaded(cur.rchild)

    def infix_threaded_traverse(self):
        """中序线索化遍历"""
        cur = self.root
        while cur is not None:
            while cur.pointer_type['left'] == 0:
                cur = cur.lchild
            print(cur.data)
            while cur.pointer_type['right'] == 1:
                cur = cur.rchild
                print(cur.data)
            cur = cur.rchild


if __name__ == '__main__':
    binary_tree = ThreadedBinaryTree()
    for i in range(10):
        binary_tree.add(i)
    root = binary_tree.root
    binary_tree.infix_threaded(root)
    print('中序线索化遍历：')
    binary_tree.infix_threaded_traverse()
