import jieba, sys
from zhtools.langconv import *

'''結巴中文分詞基本操作'''
print('='*40)
print('1. 分詞')
print('-'*40)
# 1.全模式, 掃描所有可以成詞的詞語, 速度非常快, 不能解決歧異
seg_list = jieba.cut('我來到台北的台北大學', cut_all=True)
print('Full Mode:' + ','.join(seg_list))

# 2.默認是精確模式, 適合文本分析
seg_list = jieba.cut('我來到台北的台北大學', cut_all=False)
print('\nDefault Mode:' + ','.join(seg_list))

# 3.搜索引擎模式, 對長詞再次切分, 提高招回率, 適合用搜索引擎
# jieba.cut_for_search 該方法適合用於搜索引擎構建到牌所引的分詞, 粒度比較細
seg_list = jieba.cut_for_search('我來到台北的台北大學', HMM=False)
print('\n搜索引擎模式:' + ','.join(seg_list))


print('='*40)
print('2. 添加自定義辭典/調整辭典')
print('-'*40)

# seg_list = jieba.cut('如果放到數據庫中將出錯', HMM=False)
# hope_result=>如果/放到/數據庫/中/將/出錯
print('原文檔: \t' + '/'.join(jieba.cut('如果放到數據庫中將出錯')))
print(jieba.suggest_freq(('中', '將'), True))
print('改進文檔: \t' + '/'.join(jieba.cut('如果放到數據庫中將出錯')))

print('\n原文檔: \t' + '/'.join(jieba.cut('[台中]正確應該不會被切分')))
print(jieba.suggest_freq(('台中'), True))
print('改進文檔: \t' + '/'.join(jieba.cut('[台中]正確應該不會被切分')))

'''2.家財自定義分詞辭典'''
sys.path.append('../')
jieba.load_userdict('dataSet/StopWord/user_dict.txt') # 加載辭典

seg_list1 = jieba.cut('今天很高興在慕課網和大家交流學習')
print('\n加載自定義分詞詞典: \n' + '/'.join(seg_list1))

print('='*40)
print('3. 關鍵詞的提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)
# tf-idf（英語：term frequency–inverse document frequency）
# 是一種用於資訊檢索與文字挖掘的常用加權技術。tf-idf是一種統計方法，
# 用以評估一字詞對於一個檔案集或一個語料庫中的其中一份檔案的重要程度。
# 字詞的重要性隨著它在檔案中出現的次數成正比增加，
# 但同時會隨著它在語料庫中出現的頻率成反比下降。
# tf-idf加權的各種形式常被搜尋引擎應用，
# 作為檔案與用戶查詢之間相關程度的度量或評級。
# 除了tf-idf以外，網際網路上的搜尋引擎還會使用基於連結分析的評級方法，
# 以確定檔案在搜尋結果中出現的順序。
import jieba.analyse

def readFile(path):
    str_doc = ''
    with open(path, 'r', encoding='utf-8') as f:
        str_doc = f.read()
    return str_doc

filepath = r'dataSet/CSCMNews/体育/16.txt'
str_doc = readFile(filepath)

print('='*40)
print('extract_tags')
print('-'*40)
zh_hant_doc = Converter('zh-hant').convert(str_doc)
for x, w in jieba.analyse.extract_tags(zh_hant_doc, 10, withWeight=True): # withWeight 為是否一併返回關鍵詞權重值
    print('%s %s' % (x,w))

print('='*40)
print('textrank')
print('-'*40)
# textrank 算法是一种用于文本的基于图的排序算法，
# 通过把文本分割成若干组成单元（句子），构建节点连接图，
# 用句子之间的相似度作为边的权重，通过循环迭代计算句子的TextRank值，
# 最后抽取排名高的句子组合成文本摘要。
for x, w in jieba.analyse.textrank(zh_hant_doc, 10, withWeight=True): # withWeight 為是否一併返回關鍵詞權重值
    print('%s %s' % (x, w))

print('='*40)
print('4. 詞性標註')
print('-'*40)
import jieba.posseg

words = jieba.posseg.cut('我愛台北西門町')
for word, flag in words:
    print('%s %s' % (word, flag))

print('='*40)
print('5. tokenize: 返回詞語在原文的起止位置')

print('-'*40)
print(' 默認模式')
print('-'*40)
result = jieba.tokenize('永和服裝飾品有限公司')
for tk in result:
    # print(tk)
    print('word %s\t\t start:%d\t\t end:%d' %(tk[0], tk[1], tk[2]))

print('-'*40)
print(' 搜索模式')
print('-'*40)
result = jieba.tokenize('永和服裝飾品有限公司', mode='search')
for tk in result:
    # print(tk)
    print('word %s\t\t start:%d\t\t end:%d' %(tk[0], tk[1], tk[2]))
