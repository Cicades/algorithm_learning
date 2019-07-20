"""
用prim算法解决修路问题
"""

import sys
import os
graph_path = os.path.join(os.path.curdir, '../../graph')
sys.path.append(graph_path)
from Graph import Graph


def prim(graph=None, index=0):
    """
    普利算法：根据给定的图生成MST
    :param graph: 图
    :param index 开始生成MST的顶点的下标
    :return: 列表
    """
    vertexs = graph.vertexs
    edges = graph.edges
    vertexs_num = len(vertexs)  # 顶点的数量
    is_visited = [False] * vertexs_num  # 记录结点是否已被访问
    is_visited[index] = True  # 因为是从index开始生成MST，所以将相应的顶点标记为已访问
    res = list()
    for i in range(vertexs_num-1):
        v1 = None  # 最小权值边的顶点
        v2 = None  # 最小权值边的顶点
        min_weight = 1000  # 最小权值,初始值给个较大的数，以便后续操作
        # 由MST的特征可得n个顶点会得到n-1条边，因此循环n-1次
        for j in range(vertexs_num):
            for k in range(vertexs_num):
                cur_weight = edges[j][k]  # 正在访问的边的权值
                if all([is_visited[j], not is_visited[k], cur_weight, cur_weight < min_weight]):
                    v1 = j
                    v2 = k
                    min_weight = cur_weight
        res.append((vertexs[v1], vertexs[v2], min_weight))
        is_visited[v2] = True
        min_weight = 1000
    return res


if __name__ == '__main__':
    vertexs = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    graph = Graph(vertexs)
    # 根据实际问题添加边，不相通的两个顶点之间的权值为0
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 6, 2)
    graph.add_edge(0, 2, 7)
    graph.add_edge(1, 6, 3)
    graph.add_edge(1, 3, 9)
    graph.add_edge(6, 4, 4)
    graph.add_edge(6, 5, 6)
    graph.add_edge(2, 4, 8)
    graph.add_edge(3, 5, 4)
    graph.add_edge(4, 5, 5)
    res = prim(graph, 1)
    print(res)
