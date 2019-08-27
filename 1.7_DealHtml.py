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

'''
re.I 使匹配對大小寫不敏感
re.L 做本地化識別(locale-aware)匹配
re.M 多行匹配, 影響 ^ 和 $
re.S 使 . 匹配包括患行在內的所有字符
re.U 根據Unicode字符集解析字符. 這個標誌影響 \w, \W, \b, \B
re.X 該標誌通過給予你更靈活的格式以便你將正則表達式寫得更容易
'''

# 清洗HTML標籤文本
# @param htmlstr HTML字符串
def filter_tags(htmlstr):
    # 過濾DOCTYPE
    html = ' '.join(htmlstr.split()) # 去掉多餘空格
    re_doctype = re.compile(r'<!DOCTYPE .*?>', re.S)
    res = re_doctype.sub('', htmlstr)

    # 過濾CDATA
    re_cdata = re.compile('//<!CDATA\[[ >] //\] > ', re.I)
    res = re_cdata.sub('', res)

    # script
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
    res = re_script.sub('', res)

    # style
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
    res = re_style.sub('', res) # 去掉style

    # 處理換行
    re_br = re.compile('<br\s*?/?>')
    res = re_br.sub('', res) # 將br轉換為換行

    # HTML標籤
    re_h = re.compile('</?\w+[^>]*>')
    res = re_h.sub('', res) # 去掉HTML標籤

    # 剔除超連結
    http_link = re.compile('(http://.+.html)')
    res = http_link.sub('', res) # 去掉HTML標籤

    # 多餘的空格
    blank_line = re.compile('\n+')
    res = blank_line.sub('', res)

    blank_line_l = re.compile('\n')
    res = blank_line_l.sub('', res)

    blank_line_kon = re.compile('\t')
    res = blank_line_kon.sub('', res)
  
    blank_line_one = re.compile('\r\n')
    res = blank_line_one.sub('', res)

    blank_line_two = re.compile('\r')
    res = blank_line_two.sub('', res)

    blank_line_three = re.compile(' ')
    res = blank_line_three.sub('', res)

    return res
    
def readFile(path):
    str_doc = ''
    with open(path, 'r', encoding='utf-8') as f:
        str_doc = f.read()
    return str_doc

if __name__ == '__main__':
    str_doc = readFile(r'./htmldome.txt')
    # print(str_doc)
    res = filter_tags(str_doc)
    print(res)