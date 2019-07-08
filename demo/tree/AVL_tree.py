"""自平衡二叉查找树
概念：对二叉排序树的改进，AVL树得名于它的发明者
特点：AVL tree中任何一个节点的左子树和右子树的高度之差不超过1
"""

from binary_sort_tree import Node, BinarySortTree


class AVLNode(Node):
    """AVL树节点类"""
    @property
    def height(self):
        """获取树的高度"""
        left_height = 0 if self.lchild is None else self.lchild.height
        right_height = 0 if self.rchild is None else self.rchild.height
        return max(left_height, right_height) + 1

    @property
    def left_tree_height(self):
        """获取左子树的高度"""
        return 0 if self.lchild is None else self.lchild.height

    @property
    def right_tree_height(self):
        """获取右子树的高度"""
        return 0 if self.rchild is None else self.rchild.height

    def left_rotate(self):
        """左旋转
        当右子树的高度-左子树的高度>1时，应当削减右子树的高度
        """
        new_node = AVLNode()  # 创建一个新节点
        new_node.data = self.data
        new_node.rchild = self.rchild.lchild
        new_node.lchild = self.lchild
        self.data = self.rchild.data
        self.rchild = self.rchild.rchild
        self.lchild = new_node

    def right_rotate(self):
        """右旋
        当左子树的高度-右子树的高度>1,应当削减左子树的高度
        """
        new_node = AVLNode()
        new_node.data = self.data
        new_node.lchild = self.lchild.rchild
        new_node.rchild = self.rchild
        self.data = self.lchild.data
        self.rchild = new_node
        self.lchild = self.lchild.lchild


class AVLTree(BinarySortTree):
    """AVL树"""
    @property
    def height(self):
        """获取树的高度"""
        return self.root.height

    def add(self, node):
        """添加节点"""
        super(AVLTree, self).add(node)
        if self.root.right_tree_height - self.root.left_tree_height > 1:
            # 右子树的高度-左子树的高度>1
            if self.root.rchild.left_tree_height > self.root.rchild.right_tree_height:
                # 当右子树的左子树高度大于右子树时，单一的旋转不能构造AVL
                self.root.rchild.right_rotate()  # 对右子树进行右旋转
                self.root.left_rotate()  # 对整颗树进行左旋转
            else:
                self.root.left_rotate()
            return
        if self.root.left_tree_height - self.root.right_tree_height > 1:
            # 左子树的高度-右子树的高度>1
            if self.root.lchild.left_tree_height < self.root.lchild.right_tree_height:
                # 当左子树的左子树高度小于右子树时，单一的旋转不能构造AVL
                self.root.lchild.left_rotate()  # 对左子树进行左旋转
                self.root.right_rotate()  # 对整颗树进行右旋转
            else:
                self.root.right_rotate()
            return


if __name__ == '__main__':
    print('测试左旋转：')
    arr = [4, 3, 6, 5, 7, 8]
    tree = AVLTree()
    for v in arr:
        tree.add(AVLNode(v))
    tree.infix_order_traverse()
    height = tree.height
    left_height = tree.root.left_tree_height
    right_height = tree.root.right_tree_height
    print('树的高度为%d' % height)
    print('子树的高度：')
    print(left_height, right_height)

    # 测试右旋转
    print('测试右旋转：')
    arr = [10, 12, 8, 9, 7, 6]
    tree = AVLTree()
    for v in arr:
        tree.add(AVLNode(v))
    tree.infix_order_traverse()
    height = tree.height
    left_height = tree.root.left_tree_height
    right_height = tree.root.right_tree_height
    print('树的高度为%d' % height)
    print('子树的高度：')
    print(left_height, right_height)

    # 测试双
    print('测试双旋转：')
    arr = [10, 11, 7, 6, 8, 9]
    tree = AVLTree()
    for v in arr:
        tree.add(AVLNode(v))
    tree.infix_order_traverse()
    height = tree.height
    left_height = tree.root.left_tree_height
    right_height = tree.root.right_tree_height
    print('树的高度为%d' % height)
    print('子树的高度：')
    print(left_height, right_height)
