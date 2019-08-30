import os, re, time

def textParse(str_doc):
    # 正則過濾掉特殊符號, 標點, 英文, 數字等
    r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+'
    # 去除空格
    r2 = '\s+'
    str_doc = re.sub(r1, ' ', str_doc)
    str_doc = re.sub(r2, ' ', str_doc)
    # 去除換行符
    str_doc = str_doc.replace('\n', '')
    return str_doc

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
    start_time = time.time()

    filepath = r'dataSet/CSCMNews'
    files = Loadfiles(filepath)
    n = 2 # n表示抽樣
    for i, msg in enumerate(files):
        if i%n == 0:
            catg = msg[0]
            content = msg[1]
            content = textParse(content) # 數據清洗
            if int(i/n) % 5000 == 0:
                print('{t} *** {i} \t docs has been dealed'.format(i=i, t=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())), '\n', catg, ':\t', content[:20])

    end_time = time.time()
    print('Total spent times:%.2f' % (end_time-start_time) + 's')      