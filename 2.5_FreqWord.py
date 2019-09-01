from nltk import *
import re, jieba, sys
from zhtools.langconv import *

# 解決中文顯示
import matplotlib
# 1.查看當前使用字體格式
from matplotlib.font_manager import findfont, FontProperties
# print(findfont(FontProperties(family=FontProperties().get_family()))), 在下面執行那邊執行
# C:\Users\alway\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\mpl-data\fonts\ttf\DejaVuSans.ttf
# 默認使用字體:ttf
# 2.C:\Windows\Fonts, 查找中文字體(簡體或繁體, 這篇取的原文是簡體), 然後複製到找到字體路徑
# 3.設置使用字體
matplotlib.rcParams['font.sans-serif'] = 'SimHei'


# 讀取文本信息
def readFile(path):
    str_doc = ''
    with open(path, 'r', encoding='utf-8') as f:
        str_doc = f.read()
    return str_doc

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

# 利用nltk進行詞類特徵統計
def nltk_wf_feature(word_list=None):
    '''統計詞類方法1'''
    # fdist = FreqDist(word_list)
    # print(fdist.keys(), '\n', fdist.values())

    # print('='*3, '指定詞語詞頻統計', '='*3)
    # w = '倫敦'
    # print(w, '出現頻率:', fdist.freq(w)) # 給定樣本的頻率
    # print(w, '出現次數:', fdist[w]) # 出現次數

    # print('='*3, '頻率分布表', '='*3)
    # fdist.tabulate(10) # 頻率分布表

    # print('='*3, '可視化詞類', '='*3)
    # fdist.plot(30) # 頻率分布表

    '''統計詞類方法2'''
    from collections import Counter
    words = Counter(word_list)
    print(words.keys(), '\n', words.values())

    # wlist = [w for w in words if len(w) > 2]
    wlist = [w for w in words if len(w) == 4]
    print(wlist)



if __name__ == '__main__':
    # 1.查看當前使用字體格式
    # print(findfont(FontProperties(family=FontProperties().get_family())))
    # C:\Users\alway\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\mpl-data\fonts\ttf\DejaVuSans.ttf
    # 默認使用字體:ttf
    # C:\Windows\Fonts, 查找中文字體(簡體或繁體, 這篇取的原文是簡體), 然後複製到找到字體路徑

    # 1.讀取文本
    path = r'dataSet/CSCMNews/体育/30.txt'
    str_doc = readFile(path)
    zh_hant_doc = Converter('zh-hant').convert(str_doc)

    # 2.詞類特徵統計
    word_list = seg_doc(zh_hant_doc)
    # print(word_list)
    nltk_wf_feature(word_list)

