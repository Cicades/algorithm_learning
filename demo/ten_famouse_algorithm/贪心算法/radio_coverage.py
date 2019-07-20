"""
使用贪心算法解决电台覆盖问题, 使用贪心算法求得的解不一定是最优解
问题描述：
选择最少的广播台，让所有地区都可以接收到信号
广播台     覆盖地区
k1        北京，上海，天津
k2        广州，北京，深圳
k3        成都，上海，杭州
k4        上海，天津
k5        杭州，大连
"""


def main(cities, radios):
    selected_radios = list()
    most_cover_cities = 0
    most_cover_radio = dict()
    while cities:
        for radio in radios:
            for city in radio['cover_cities']:
                temp = 0
                if city in cities:
                    temp += 1
            if most_cover_cities < temp:
                most_cover_cities = temp
                most_cover_radio = radio
        selected_radios.append(most_cover_radio)
        cities = [city for city in cities if city not in most_cover_radio['cover_cities']]
        most_cover_radio = dict()
        most_cover_cities = 0

    return selected_radios


if __name__ == '__main__':
    uncovered_cities = ['北京', '上海', '天津', '广州',
                        '深圳', '成都', '杭州', '大连']  # 电台尚未覆盖的城市
    radios = [
        {'name': 'k1', 'cover_cities': ['北京', '上海', '天津']},
        {'name': 'k2', 'cover_cities': ['广州', '北京', '深圳']},
        {'name': 'k3', 'cover_cities': ['成都', '上海', '杭州']},
        {'name': 'k4', 'cover_cities': ['上海', '天津']},
        {'name': 'k5', 'cover_cities': ['杭州', '大连']}
    ]
    selected_radios = main(uncovered_cities, radios)
    for radio in selected_radios:
        print(radio['name'], end=' ')
