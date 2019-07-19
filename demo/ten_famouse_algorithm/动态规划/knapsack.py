"""
动态规划（dynamic）：与分治法相似，同样是将问题拆分为子问题，不同的是分治法中的子问题间不存在联系
而动态规划中一个子问题的求解建立在前一个子问题求解的基础上
下面对背包问题进行求解
"""


class Knapsack(object):
    """求解背包问题"""
    def __init__(self, capacity=0):
        """
        :param capacity: 背包容量
        """
        self.capacity = capacity

    def init_table(self, goods_num):
        """初始化表"""
        table = list()
        for i in range(goods_num+1):
            row = []
            for j in range(self.capacity+1):
                row.append([])
            table.append(row)
        return table

    def count(self, goods):
        """计算商品的总价值,和总重量"""
        sum = 0
        weight = 0
        for g in goods:
            sum += g['price']
            weight += g['weight']
        return sum, weight

    def pack(self, goods=list()):
        """将商品放入背包，在不超过背包容量的情况下使背包的价值最大"""
        table = self.init_table(len(goods))
        for i in range(1, len(goods)+1):
            # i 表示第i个商品
            for j in range(1, self.capacity+1):
                # j表示背包的容量
                if goods[i-1]['weight'] > j:
                    # 待放入的物品的重量大于背包的容量
                    table[i][j] = table[i-1][j]
                else:
                    cur_weight = goods[i-1]['weight']  # 当前物品的重量
                    cur_price = goods[i-1]['price']  # 当前物品的价格
                    if self.count(table[i-1][j])[0] > (cur_price + self.count(table[i-1][j-cur_weight])[0]):
                        table[i][j] = table[i-1][j]
                    else:
                        table[i][j] = table[i-1][j-cur_weight] + [goods[i-1]]
        print(table[i][j])


if __name__ == '__main__':
    knapsack = Knapsack(4)
    goods = [
        {'name': '吉他', 'weight': 1, 'price': 1500},
        {'name': '音响', 'weight': 4, 'price': 3000},
        {'name': '电脑', 'weight': 3, 'price': 2000},
        {'name': '耳机', 'weight': 2, 'price': 3000}
    ]
    knapsack.pack(goods)
