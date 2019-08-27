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

# line = r'this is python 數據預處理課程, 這次課程很好, env is Anaconda4.4, 本次授課時間是2019年8月26日'

# rege_str1 = '^t.*' # 開頭+任意次數
# rege_str2 = '.*?(s+)'
# rege_str3 = '.*?([\u4E00-\u9FA5]+課)' # 提取中文
# rege_str4 = '(\d{4}年)'

# res = re.match(rege_str4, line)
# if res:
#     print(res.group(1))
# else:
#     print('this is null')

'''日期的提取'''
# line = '張三出生於1990年1月1日'
# line = '李四出生於1990-10-1'
# line = '王五出生於1990-10-01'
# line = '孫六出生於1990/10/1'
# line = '張七出生於1990-10'

# rege_str = '.*出生於(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))'
# res = re.match(rege_str, line)
# if res:
#     print(res.group(1))
# else:
#     print('this is null')

'''電話號碼提取'''
# line = '我的手機號碼是15828525756 就是這個號碼'
# line = '我的手機號碼是15928523456就是這個號碼'
# line = '我的手機號碼是19943544555就是這個號碼'
# line = '我的手機號碼是13857990934就是這個號碼'
line = '我的手機號碼是17757990934就是這個號碼'

rege_str = '.*?(1[5937]\\d{9})'
res = re.match(rege_str, line)
if res:
    print(res.group(1))
else:
    print('this is null')
