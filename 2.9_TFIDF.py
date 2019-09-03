import re, jieba, sys
from zhtools.langconv import *
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


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

# 利用sklern計算tfidf值特徵
def sklearn_tfidf_feature(corpus=None):
    vectorizer = CountVectorizer() # 構建詞匯表, CountVectorizer 類向量化
    transformer = TfidfTransformer() # 該類會統計每個詞語, TfidfTransformer 類進行預處理
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    # 獲取磁帶模型中的所有詞語
    words = vectorizer.get_feature_names()
    # 將tf-idf矩陣抽取出來, 元素a[i][j]表示j詞在i類文本中的tf-idf權重
    weight = tfidf.toarray()

    for i in range(len(weight)):
        print(u'------這裡輸出第', i, u'類文本的詞語tf-idf權重')
        for j in range(len(words)):
            print(words[j], weight[i][j])

if __name__ == '__main__':
    corpus = []

    path1 = r'dataSet/CSCMNews/体育/30.txt'
    str_doc1 = readFile(path1)
    zh_hant_doc1 = Converter('zh-hant').convert(str_doc1)
    word_list1 = ' '.join(seg_doc(zh_hant_doc1))
    # print(word_list1)

    path2 = r'dataSet/CSCMNews/时政/339800.txt'
    str_doc2 = readFile(path2)
    zh_hant_doc2 = Converter('zh-hant').convert(str_doc2)
    word_list2 = ' '.join(seg_doc(zh_hant_doc2))
    # print(word_list2)

    corpus.append(word_list1)
    corpus.append(word_list2)

    sklearn_tfidf_feature(corpus)