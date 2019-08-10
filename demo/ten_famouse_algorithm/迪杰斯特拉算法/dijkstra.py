class Dijkstra(object):
    """迪杰斯特拉算法"""

    N = 65535  # 取一个较大数，表示两定点间不能连通

    def __init__(self, vertexs=[], matrix=[]):
        self.vertexs = vertexs  # 顶点
        self.matrix = matrix  # 邻接矩阵
        self.vertex_len = len(self.vertexs)
        self.is_visited = [False] * self.vertex_len  # 标记节点是否已求出最短路径
        self.known_dist = [Dijkstra.N] * self.vertex_len  # 存储已知的出发点到各个顶点的最短距离
        self.unknown_dist = [None] * self.vertex_len  # 存储待计算的起始点到各顶点的距离
        self.path = [''] * self.vertex_len  # 存储起点到各顶点最短距离的路径

    def run(self, index):
        """以index为出发点计算其到各个顶点的最短距离"""
        # 将原矩阵中index到各顶点的距离复制一份，并初始化路径
        for i in range(self.vertex_len):
            self.unknown_dist[i] = self.matrix[index][i]
            self.path[i] = '{}=>{}'.format(self.vertexs[index], self.vertexs[i])

        self.known_dist[index] = 0
        self.is_visited[index] = True
        for k in range(self.vertex_len-1):
            new_index, new_shortest_dist = self.get_new_shortest_dist()
            self.known_dist[new_index] = new_shortest_dist
            self.is_visited[new_index] = True
            self.update_unknown_dist(new_index)
        self.print_res(index)

    def update_unknown_dist(self, index):
        """
        以index为出发点更新未知最短距离的顶点
        :param index:
        :return: None
        """
        for i in range(self.vertex_len):
            if not self.is_visited[i]:
                temp_weight = self.known_dist[index] + self.matrix[index][i]
                if temp_weight < self.unknown_dist[i]:
                    self.unknown_dist[i] = temp_weight
                    self.path[i] = self.path[index] + '=>{}'.format(self.vertexs[i])

    def get_new_shortest_dist(self):
        """将新的已知最短距离的节点加入集合"""
        temp_min = Dijkstra.N
        index = None  # 新节点的下标
        for i in range(self.vertex_len):
            if not self.is_visited[i] and self.unknown_dist[i] < temp_min:
                index, temp_min = i, self.unknown_dist[i]
        return index, temp_min

    def print_res(self, start):
        """打印结果"""
        for i in range(self.vertex_len):
            print('{}到{}的最短距离为：{},路径为：{}'.format(self.vertexs[start], self.vertexs[i], self.known_dist[i], self.path[i]))


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
    djs = Dijkstra(vertexs=vertexs, matrix=matrix)
    start = 0
    djs.run(start)

