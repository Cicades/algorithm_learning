"""迷宫问题：找出逃出迷宫的路径

1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 0 0 0 0 1
1 1 1 0 0 0 0 1
1 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1
说明： 
1. 用二维数组(8 * 8)map来模拟迷宫的地图
2. i, j 表示出发的位置
3. 入口为map[1][1], 出口为map[6][6]
4. 当map[i][j]为0表示该点没走过，为1时表示为墙，为2时表示该点为通路，为3时表示该点已经走过但是走不通
5. 确定迷宫探索的策略：下——>右——>上——>左,如果走不通则进行回溯

补充：寻找最短路径
可以将所有的迷宫探索策略列出来，记录每种策略所产生的路径的长度，最后从中选取路径最短的
"""
import pprint
def gen_map():
	"""生成迷宫地图"""
	maze_map = [[0 for x in range(8)] for x in range(8)]
	row = len(maze_map)
	col = len(maze_map[0])
	for i in range(8):
		maze_map[0][i] = 1
		maze_map[-1][i] = 1
		maze_map[i][0] = 1
		maze_map[i][-1] = 1

	maze_map[2][2] = 1
	maze_map[3][1:3] = [1, 1]
	return maze_map

def forward(maze_map, i, j):
	"""从i,j 处探索迷宫路线"""
	if maze_map[6][6] == 2:
		# 找到迷宫入口
		print('已找到离开路线！')
		return True
	else:
		if maze_map[i][j] == 0:
			# 该点尚未探索过
			maze_map[i][j] = 2
			if forward(maze_map, i+1, j):
				# 向下走
				return True
			elif forward(maze_map, i, j+1):
				# 向右走
				return True
			elif forward(maze_map, i-1, j):
				# 向上走
				return True
			elif forward(maze_map, i, j-1):
				# 向左走
				return True
			else:
				maze_map[i][j] = 3
				return False
		else:
			# 该点已经探索标识为1，2，3
			return False

if __name__ == '__main__':
	maze_map = gen_map()
	forward(maze_map, 1, 1)
	pprint.pprint(maze_map)