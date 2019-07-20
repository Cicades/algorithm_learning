"""
kmp 算法
关键点：求出next表，模式字符串前缀后后缀的最大公共元素长度
"""


def gen_next(string):
    """
    生成部分匹配值表（next）
    :param string: 模式字符串
    :return: kmp_next
    """
    kmp_next = [0] * len(string)
    kmp_next[0] = 0  # 字串的长度为1，不存在前缀和后缀，所以部分匹配值为0
    j = 0  # 可以理解为string[:i]的前缀的最后一个字符的下标，i表示后缀最后一个字符的下标
    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = kmp_next[j-1]
        if string[i] == string[j]:
            j += 1
        kmp_next[i] = j
    return kmp_next


def kmp_search(text, string, kmp_next):
    """
    kmp搜索算法
    :param text: 文本
    :param string: 模式字符串
    :param kmp_next: 部分匹配值表
    :return: index
    """
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != string[j]:
            j = kmp_next[j-1]
        if text[i] == string[j]:
            j += 1
        if j == len(string):
            return i - j + 1
    return -1


if __name__ == '__main__':
    string = 'ABCDABD'
    text = 'BBC ABCDAB ABCDABCDABDE'
    kmp_next = gen_next(string)
    # index = kmp_search(text, string, kmp_next)
    print(kmp_next)
    # print('搜索结果为：%d' % index)
