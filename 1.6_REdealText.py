import re

# . 任意字符
# * 任意次數
# ^ 任意開頭
# $ 結尾
# ? 非貪婪模式, 提取第一個字符
# + 至少出現一次
# {1} 出現一次
# {3,} 出現3次以上
# {2,5} 最少2次最多5次
# \d 匹配數字
# [\u4E00-\u9FA5] 漢字的匹配
# | 或的關係
# 
# [] 滿足任意一個都可以, [2345]任意 [0-9]區間 [^1]非1
# \s 為空格 \S 非空格
# \w 匹配[A-za-z0-9_] \W 反匹配[A-za-z0-9_]

# 正則對字符串的清洗
def textParse(str_doc):
    # 正則過濾掉特殊符號, 標點, 英文, 數字等
    r1 = '[a-zA-Z0-9!"#$%^\'()*+,-./：: ;: |<=>?@, -。 ?、]^_`{|}~]+'
    # 去除空格
    r2 = '\s+'
    str_doc = re.sub(r1, ' ', str_doc)
    str_doc = re.sub(r2, ' ', str_doc)
    # 去除換行符
    str_doc = str_doc.replace('\n', '')
    return str_doc

def readFile(path):
    str_doc = ''
    with open(path, 'r', encoding='utf-8') as f:
        str_doc = f.read()
    return str_doc



if __name__ == '__main__':
    # 1.讀取文本
    path = r'dataSet/CSCMNews/体育/0.txt'
    str_doc = readFile(path)
    # print(str_doc)

    # 2.數據清洗
    res = textParse(str_doc)
    print(res)