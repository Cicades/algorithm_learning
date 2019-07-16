"""图

图的存储结构：
（1）邻接矩阵
（2）邻接表

"""


class Graph(object):
    """图"""

    def __init__(self, vertexs=[]):
        self.vertexs = vertexs  # 顶点
        self.edges = list() if not vertexs else [[0 for x in vertexs] for x in vertexs]  # 边（临界矩阵）

    def add_vertex(self, data):
        """添加顶点"""
        self.vertexs.append(data)
        if not self.edges:
            self.edges.append([0])
        else:
            self.edges.append([0] * (len(self.vertexs) - 1))
            for edges_li in self.edges:
                edges_li.append(0)

    def add_edge(self, v1, v2):
        """根据给定的两个顶点下标建立链接"""
        self.edges[v1][v2] = 1
        self.edges[v2][v1] = 1

    def show_edges(self):
        """打印边（邻接矩阵）"""
        for li in self.edges:
            print(li)

    def get_first_neighbor(self, index):
        """返回index顶点的第一个邻接节点"""
        for i in range(len(self.vertexs)):
            if self.edges[index][i]:
                return i
        return -1

    def get_next_neighbor(self, v1, v2):
        """已知v1的一个邻接点为v2，求v1下一个邻接点"""
        for i in range(v2+1, len(self.vertexs)):
            if self.edges[v1][i]:
                return i
        return -1

    def __dfs(self, is_visited, index):
        """
        图的深度遍历
        :param is_visited: 记录访问过的节点
        :param index: 开始遍历的节点的下标
        """
        print(self.vertexs[index])
        is_visited[index] = True  # 将该顶点设置为已访问
        neighbor = self.get_first_neighbor(index)
        while neighbor != -1:
            # 存在邻接点
            if not is_visited[neighbor]:
                # 邻接点尚未被访问
                self.__dfs(is_visited, neighbor)
            else:
                neighbor = self.get_next_neighbor(index, neighbor)

    def dfs(self):
        """图的深度遍历"""
        is_visited = [0] * len(self.vertexs)
        for i in range(len(self.vertexs)):
            if not is_visited[i]:
                self.__dfs(is_visited, i)

    def bfs(self):
        """广度优先遍历"""
        is_visited = [False] * len(self.vertexs)
        for i in range(len(self.vertexs)):
            if is_visited[i]:
                continue
            self.__bfs(i, is_visited)

    def __bfs(self, i, is_visited):
        """
        图的广度优先遍历
        :param i: 开始进行遍历的顶点的下标
        :param is_visited: 记录顶点是否已经被访问
        :return:
        """
        queue = list()  # 存放已被访问的顶点
        print(self.vertexs[i])  # 输出当前节点
        is_visited[i] = True  # 将当前节点标记为已访问
        queue.append(i)
        while queue:
            u = queue.pop(0)
            w = self.get_first_neighbor(u)
            while w != -1:
                # 找到第一个邻接点
                if not is_visited[w]:
                    print(self.vertexs[w])
                    is_visited[w] = True
                    queue.append(w)
                else:
                    w = self.get_next_neighbor(u, w)


if __name__ == '__main__':
    vertexs = ['A', 'B', 'C', 'D']
    graph = Graph(vertexs)
    graph.add_vertex('E')
    # 添加边
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.show_edges()
    print('深度遍历：')
    graph.dfs()  # 深度遍历
    print("广度遍历：")
    graph.bfs()  # 广度遍历

