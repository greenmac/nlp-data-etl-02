from zhtools.langconv import *

def readFile(path):
    str_doc = ''
    with open(path, 'r', encoding='utf-8') as f:
        str_doc = f.read()
    return str_doc

# 1.簡體字轉化繁體字
path1 = r'dataSet/CSCMNews/体育/16.txt'
str1 = readFile(path1)
line1 = Converter('zh-hant').convert(str1)
print('繁體字--->簡體字: \n', line1)

print('==========')
# 2.繁體字轉化簡體字
path2 = r'zh_exsample.txt'
str2 = readFile(path2)
line2 = Converter('zh-hans').convert(str2)
print('簡體字--->繁體字: \n', line2)
