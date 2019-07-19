"""
分治算法（divided-and-conquer），"分而治之"，将大的问题拆分为若干个子问题，最后将子问题的解合并得到目标解
下面对汉诺塔问题进行求解
"""


class HanoiTower(object):
    """汉诺塔问题"""
    def __init__(self, num):
        """
        初始化
        :param num: 需要移动的圆盘
        """
        self.num = num

    @staticmethod
    def move(num, a, b, c):
        """汉诺塔圆盘移动"""
        if num == 1:
            # 如果只有一个圆盘，直接从a移动到c
            print('{}=>{}'.format(a, c))
        else:
            HanoiTower.move(num-1, a, c, b)  # num-1个圆盘从a移动到b
            HanoiTower.move(1, a, b, c)  # 将最后一个盘从a移动到c
            HanoiTower.move(num-1, b, a, c)  # 将num-1个盘从b移动到c

    def run(self):
        """求解汉诺塔问题"""
        HanoiTower.move(self.num, 'A', 'B', 'C')


if __name__ == '__main__':
    hanoi_tower = HanoiTower(5)
    hanoi_tower.run()


