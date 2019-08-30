from jpype import *

paraStr1 = '台灣中研院計算技術研究所的王綠教授正在教授自然語言處理課程'
print('='*30 + 'HanLP分詞' + '='*30)
HanLP = JClass('com.hankcs.hanlp.HanLP')
print(HanLP.segment(paraStr1))