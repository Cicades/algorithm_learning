from copy import deepcopy


class KnightTravel(object):
    """骑士周游算法"""
    def __init__(self, row, col):
        """
        初始化
        :param col: 棋盘的列数
        :param row: 棋盘的行数
        """
        self.col = col
        self.row = row
        self.cheese_board = list()
        self.finished = False
        for r in range(row):
            self.cheese_board.append([0]*self.col)
        self.is_visited = deepcopy(self.cheese_board)

    def run(self, x, y):
        """
        运行骑士周游算法
        :param x: 起点的横坐标
        :param y: 起点的纵坐标
        :return:
        """
        cheese_board = deepcopy(self.cheese_board)
        self.travel(cheese_board, x, y, 1)

    def travel(self, cheese_board, x, y, step):
        cheese_board[x][y] = step
        self.is_visited[x][y] = 1
        next_li = self.get_next(x, y)
        while next_li:
            node = next_li.pop(0)
            if not self.is_visited[node[0]][node[1]]:
                self.travel(cheese_board, node[0], node[1], step+1)
        if step <= self.col * self.row and not self.finished:
            print(step)
            cheese_board[x][y] = 0
            self.is_visited[x][y] = 0
        else:
            self.finished = True

    def get_next(self, x, y):
        """
        根据当前的坐标获取所有的可行落子点
        :param x: 当前坐标的横坐标
        :param y: 当前坐标的纵坐标
        :return: list
        """
        next_li = list()
        # 当前棋子最多有8个落子点，下面一一列举，并将可能的落子点保存起来
        if x - 2 >= 0 and y + 1 < self.row:
            next_li.append((x-2, y+1))
        if x - 2 >= 0 and y - 1 >= 0:
            next_li.append((x-2, y-1))
        if x + 2 < self.col and y + 1 < self.row:
            next_li.append((x+2, y+1))
        if x + 2 < self.col and y - 1 >= 0:
            next_li.append((x+2, y-1))
        if y - 2 >= 0 and x + 1 < self.col:
            next_li.append((x+1, y-2))
        if y - 2 >= 0 and x - 1 >= 0:
            next_li.append((x-1, y-2))
        if y + 2 < self.row and x + 1 < self.row:
            next_li.append((x+1, y+2))
        if y + 2 < self.row and x - 1 >= 0:
            next_li.append((x-1, y+2))
        return next_li


if __name__ == '__main__':
    k = KnightTravel(6, 6)
    from pprint import pprint
    k.run(1, 3)
    pprint(k.cheese_board)
