class Kruskal(object):
    """克鲁斯卡尔算法"""

    MAX_NUM = 10000

    def __init__(self, vertexs=list(), matrix=list()):
        self.vertexs = vertexs  # 顶点
        self.matrix = matrix  # 图：邻接矩阵
        self.mst = list()  # 最小生成树
        self.edges = list()  # 边
        self.gen_edges()
        self.ends = [0] * len(self.vertexs)  # 存储最小生成树各个顶点的终点（动态产生的）

    def gen_edges(self):
        """生成边"""
        l = len(self.vertexs)
        for i in range(l):
            for k in range(i, l):
                if self.matrix[i][k] != Kruskal.MAX_NUM:
                    self.edges.append({'start': (self.vertexs[i], i), 'end': (self.vertexs[k], k), 'weight': self.matrix[i][k]})

    def sort_edges(self):
        self.edges = sorted(self.edges, key=lambda edges: edges['weight'])

    def get_end(self, i):
        """获取下标为i的顶点在最小生成树中的终点"""
        while self.ends[i] != 0:
            i = self.ends[i]
        return i

    def run(self):
        self.sort_edges()
        for edge in self.edges:
            v1 = edge['start'][1]
            v2 = edge['end'][1]
            v1_end = self.get_end(v1)
            v2_end = self.get_end(v2)
            if v1_end != v2_end:
                # 不产生回路
                self.mst.append(edge)
                self.ends[v1_end] = v2_end


if __name__ == '__main__':
    vertexs = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    MAX_NUM = 10000  # 在邻接矩阵使用一个极大的数表示两个顶点间不连通
    matrix = [
        [MAX_NUM, 12, MAX_NUM, MAX_NUM, MAX_NUM, 16, 14],
        [12, MAX_NUM, 10, MAX_NUM, MAX_NUM, 7, MAX_NUM],
        [MAX_NUM, 10, MAX_NUM, 3, 5, 6, MAX_NUM],
        [MAX_NUM, MAX_NUM, 3, MAX_NUM, 4, MAX_NUM, MAX_NUM],
        [MAX_NUM, MAX_NUM, 5, 4, MAX_NUM, 2, 8],
        [16, 7, 6, MAX_NUM, 2, MAX_NUM, 9],
        [14, MAX_NUM, MAX_NUM, MAX_NUM, 8, 9, MAX_NUM]
    ]
    kruskal = Kruskal(vertexs=vertexs, matrix=matrix)
    kruskal.run()
    for edge in kruskal.mst:
        print(edge, end=' ')
