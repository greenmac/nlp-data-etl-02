# coding=utf-8
import os, time

def traversalDir(rootDir):
    for i, lists in enumerate(os.listdir(rootDir)):
        path = os.path.join(rootDir, lists)
        if os.path.isfile(path):
            if i%10000 == 0:
                print('{t} *** {i} \t docshas been read'.format(i=i, t=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        if os.path.isdir(path):
            traversalDir(path)




if __name__ == '__main__':
    t1 = time.time()

    rootDir = r'dataSet/CSCMNews'
    traversalDir(rootDir)

    t2 = time.time()
    print('Total Cost Time %.2f' %(t2-t1)+'s')
