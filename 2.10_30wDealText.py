import re, jieba, sys, os, time
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

# 迭代器類
class LoadFolders(object):
    def __init__(self, par_path):
        self.par_path = par_path
    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_abdpath = os.path.join(self.par_path, file)
            if os.path.isdir(file_abdpath):
                yield file_abdpath # return

class Loadfiles(object):
    def __init__(self, par_path):
        self.par_path = par_path
    def __iter__(self):
        folders = LoadFolders(self.par_path)
        for folder in folders: # level directory
            catg = folder.split(os.sep)[-1]
            for file in os.listdir(folder): # secondary directory
                file_path = os.path.join(folder, file)
                # 文件具體操作
                if os.path.isfile(file_path):
                    this_file = open(file_path, 'rb')
                    content = this_file.read().decode('utf8')
                yield catg, content
                this_file.close()



if __name__ == '__main__':
    star_time = time.time()

    filepath = os.path.abspath(r'dataSet/CSCMNews')
    files = Loadfiles(filepath)
    n = 5 # 表示抽樣率
    for i, msg in enumerate(files):
        if i % n == 0:
            catg = msg[0]
            content = msg[1]
            content = Converter('zh-hant').convert(content)
            content = seg_doc(content)
            if int(i%n) % 10000 == 0:
                print('{t}***{i} \t docs has been dealed'.format(i=i, t=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())), '\n', catg, ':\t', content[:20])

    end_time = time.time()
    print('Total spent times:%.2f' % (end_time-star_time) + 's')