from functools import reduce
'''
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f, L)
'''
def prod(L):
    return reduce(lambda x, y: x * y, L)

L1 = []
while 1:
    s = input('请往连乘数列中添加数字(一次输入一个，输入end结束)：\n')

    if s == 'end':
        break
    s = float(s)

    L1.append(s)

print('连乘列表为：\n',L1)
print('计算结果为：\n',prod(L1))

