# encoding=utf-8
import jieba
import wordcloud
# 从文件读入信息
def read(filname):
    f = open(filname,"r",encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        a=Item()
        line.split(" ")
if __name__=="__main__":
    read("res.txt")