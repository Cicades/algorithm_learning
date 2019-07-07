"""二叉排序树
特点:
1）左孩子的值比父节点要小，右孩子的值比父节点要大
2）便于插入和查找
"""


class Node(object):
    """节点类"""
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def search(self, data):
        """根据给定的值查找节点"""
        if self is None:
            return None
        if self.data == data:
            return self
        elif self.data > data:
            return self.lchild.search(data)
        else:
            return self.rchild.search(data)

    def search_parent(self, data):
        """根据给定的值查找节点的父节点"""
        if self is None or self.data == data:
            return None
        if (self.lchild and self.lchild.data == data) or (self.rchild and self.rchild.data == data):
            return self
        if self.lchild and data < self.data:
            return self.lchild.search_parent(data)
        if self.rchild and data >= self.data:
            return self.rchild.search_parent(data)

    def get_right_tree_min_node(self):
        """获取当前节点右子树的最小节点"""
        parent = None
        node = self.rchild
        while node.lchild:
            if node.lchild.lchild is None:
                parent = node
            node = node.lchild
        return node, parent


class BinarySortTree(object):
    """而叉排序树"""
    def __init__(self, root=None):
        self.root = root

    def __add(self, cur, node):
        """添加节点"""
        if cur is None:
            return
        if node.data < cur.data:
            if cur.lchild is None:
                cur.lchild = node
            else:
                self.__add(cur.lchild, node)
        else:
            if cur.rchild is None:
                cur.rchild = node
            else:
                self.__add(cur.rchild, node)

    def add(self, node):
        """添加节点"""
        if self.root is None:
            self.root = node
        else:
            self.__add(self.root, node)

    def __infix_order_reverse(self, cur):
        """中序遍历"""
        if cur is None:
            return
        self.__infix_order_reverse(cur.lchild)
        print(cur.data, end=' ')
        self.__infix_order_reverse(cur.rchild)

    def infix_order_traverse(self):
        """中序遍历"""
        self.__infix_order_reverse(self.root)

    def search(self, data):
        """查找节点"""
        return self.root.search(data)

    def search_parent(self, data):
        """查找父节点"""
        return self.root.search_parent(data)

    def del_node(self, data):
        """删除节点
        考虑几种情况：
        （1）删除的节点为叶子节点
            令父节点指向该节点的指针为空
        （2）删除的节点为非叶子节点
            1）删除的节点只有一个子节点
            令父节点指向该节点的指针指向该节点的子节点
            2）删除的节点有两个子节点
            从该节点的左子树找出值最大的节点或从右子树找出最小的节点，并替换需要删除的节点
        """
        if self.root is None:
            print('树为空，不能删除！')
        parent = self.root.search_parent(data)
        target = self.root.search(data)
        if target.lchild is None and target.rchild is None:
            # 删除的节点为叶子节点
            if parent.lchild and parent.lchild.data == target.data:
                # 删除的节点为左节点
                parent.lchild = None
            if parent.rchild and parent.rchild.data == target.data:
                # 删除的节点为右节点
                parent.rchild = None
        elif target.lchild and target.rchild:
            # 删除的节点存在两个子节点
            min_node, min_node_parent = target.get_right_tree_min_node()
            target.data = min_node.data
            if min_node_parent is None:
                # 右子树最小节点为删除节点的右节点
                if min_node.rchild is None:
                    # 最小节点为叶子节点
                    target.rchild = None
                else:
                    # 最小节点有孩子节点
                    target.rchild = min_node.rchild
            else:
                # 最小节点的父节点不为空
                min_node_parent.lchild = None
        else:
            # 待删除的节点只有一个子节点
            if parent.lchild and parent.lchild.data == data:
                # 待删除的节点为左节点
                if target.lchild:
                    # 待删除的节点只有左节点
                    parent.lchild = target.lchild
                elif target.rchild:
                    # 待删除的节点只有右节点
                    parent.lchild = target.rchild
            elif parent.rchild and parent.rchild.data == data:
                # 待删除的节点为右节点
                if target.lchild:
                    # 待删除的节点只有左节点
                    parent.rchild = target.lchild
                elif target.rchild:
                    # 待删除的节点只有右节点
                    parent.rchild = target.rchild


if __name__ == '__main__':
    tree = BinarySortTree()
    arr = [7, 3, 10, 12, 5, 1, 9, 2]
    for v in arr:
        tree.add(Node(v))
    tree.infix_order_traverse()
    print('')
    print('删除节点12：')  # 删除叶子节点
    tree.del_node(12)
    tree.infix_order_traverse()
    print('')
    print('删除节点1：')  # 删除只有一个叶子节点的节点
    tree.del_node(1)
    tree.infix_order_traverse()
    print('')
    print('删除节点3：')  # 删除有两个叶子节点的节点
    tree.del_node(3)
    tree.infix_order_traverse()
    print('')
    print('删除根节点7：')  # 删除根节点
    tree.del_node(7)
    tree.infix_order_traverse()

