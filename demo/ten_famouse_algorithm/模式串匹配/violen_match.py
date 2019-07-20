"""
暴力法模式串匹配，该方法存在大量回溯
"""


def violence_match(text, string):
    """
    前缀匹配（暴力法）
    :param text: 文本
    :param string: 模式串
    :return: 模式串在文本中的第一次出现的下标，否则返回-1
    """
    i = 0  # 文本下标
    j = 0  # 模式串下标
    while i < len(text) and j < len(string):
        if text[i] == string[j]:
            i += 1
            j += 1
        else:
            # 回溯
            i = i - j + 1
            j = 0
    if j == len(string):
        return i - j
    else:
        return -1


if __name__ == '__main__':
    text = '123412345123456'
    string = '345'
    index = violence_match(text, string)
    print(index)
