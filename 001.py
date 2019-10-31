import os

def normalize(name):
    result = name[0].upper() + name[1:].lower()
    return result

if __name__=='__main__':
    str = input("请依次输入英文姓名(每个姓名中间用空格分隔)：")
    strlist = str.split(' ')
    #print(strlist)
    print(list(map(normalize, strlist)))
    os.system("pause")