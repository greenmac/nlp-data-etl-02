# coding=utf-8
import time

def feb1(max):
    n, a, b = 0, 0, 1
    while n < max:
        if n < 20:
            print('->', b)
        a, b = b, a+b
        n = n+1

# 生成器算法實現費波那契數列
def feb2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1

def generatorDome():
    max_num = 100000000 # 最大迭代數

    t1 = time.time()
    feb1(max_num)
    t2 = time.time()
    print('Feb1 Total Time %.2f' % (t2-t1)+'s')

    t3 = time.time()
    b = feb2(max_num)
    t4 = time.time()
    print('Feb2 Total Time %.2f' % (t4-t3)+'s')


if __name__ == '__main__':
    generatorDome()