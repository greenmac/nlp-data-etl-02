import os, time
import sys
sys.setrecursionlimit(1000000)

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
                yield catg, file



if __name__ == '__main__':
    start_time = time.time()

    filepath = os.path.abspath(r'dataSet/CSCMNews/')
    # print(filepath)
    files = Loadfiles(filepath)
    for i, msg in enumerate(files):
        if i%10000 == 0:
            print('{t} *** {i} \t docs has been read '.format(i=i, t=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))

    end_time = time.time()
    print('Total spent times:%.2f' % (end_time-start_time) + 's')      