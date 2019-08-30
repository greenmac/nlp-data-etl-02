import re, jieba, sys
from zhtools.langconv import *

# 讀取文本信息
def readFile(path):
    str_doc = ''
    with open(path, 'r', encoding='utf-8') as f:
        str_doc = f.read()
    return str_doc

# 正則對字符串清洗
def textParse(str_doc):
    # 去掉字符
    str_doc = re.sub('\u3000', '', str_doc)
    # 去除空格
    str_doc = re.sub('\s+', ' ', str_doc)
    # 去除換行符
    str_doc = str_doc.replace('\n', ' ')
    # 正則過濾掉特殊符號, 標點, 英文, 數字等
    r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+'
    str_doc = re.sub(r1, ' ', str_doc)
    return str_doc

# 創建停用詞列表
def get_stop_words(path=r'dataSet/StopWord/NLPIR_stopwords.txt'):
    file = open(path, 'r', encoding='utf-8').read().split('\n')
    return set(file)

# 去掉一些停用詞和數字
def rm_tokens(words, stwlist):
    word_list = list(words)
    stop_words = stwlist
    for i in range(word_list.__len__())[::-1]:
        if word_list[i] in stop_words: # 去除停用詞
            word_list.pop(i)
        elif word_list[i].isdigit(): # 去除數字
            word_list.pop(i)
        elif len(word_list[i]) == 1 : # 去除單個字符
            word_list.pop(i)
        elif word_list[i] == ' ' : # 去除空字符
            word_list.pop(i)
    return word_list

# 利用jieba對文本進行分詞, 返回切詞後的list
def seg_doc(str_doc):
    # 1.正則處理原文本
    sent_list = str_doc.split('\n')
    sent_list = map(textParse, sent_list)
    # 2.獲取停用詞
    stwlist = get_stop_words()
    # 3.分詞並去除停用詞
    word_2dlist = [rm_tokens(jieba.cut(part, cut_all=False), stwlist) for part in sent_list]
    # 4.合併列表
    word_list = sum(word_2dlist, [])

    return word_list


if __name__ == '__main__':
    path = r'dataSet/CSCMNews/体育/30.txt'
    str_doc = readFile(path)
    zh_hant_doc = Converter('zh-hant').convert(str_doc)
    word_list = seg_doc(zh_hant_doc)
    print(word_list)
    # print('-'*40)
