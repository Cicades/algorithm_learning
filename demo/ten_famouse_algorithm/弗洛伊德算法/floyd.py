import copy
import pprint


def floyd(vertexs=list(), matrix=list()):
    """弗洛伊德算法"""
    matrix = copy.deepcopy(matrix)
    l = len(vertexs)
    for i in range(l):
        # i 表示中介顶点的下标
        for k in range(l):
            # k 表示出发点的下标
            for j in range(l):
                # j表示目标点的下标
                if k == j:
                    matrix[k][j] = 0
                    continue
                temp = matrix[k][i] + matrix[i][j]
                if matrix[k][j] > temp:
                    matrix[k][j] = temp
    return matrix


if __name__ == '__main__':
    vertexs = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    N = 65535
    matrix = [
        [N, 5, 7, N, N, N, 2],
        [5, N, N, 9, N, N, 3],
        [7, N, N, N, 8, N, N],
        [N, 9, N, N, N, 4, N],
        [N, N, 8, N, N, 5, 4],
        [N, N, N, 4, 5, N, 6],
        [2, 3, N, N, 4, 6, N]
    ]
    res = floyd(vertexs, matrix)
    pprint.pprint(res)
