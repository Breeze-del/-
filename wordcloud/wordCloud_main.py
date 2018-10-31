# encoding=utf-8
import json
class item:
    def __init__(self):
        self.id=0 # 店铺id
        self.review="" # 店铺评论
        self.count=1 # 评论的个数 也就是店铺总的订单量
        self.flag = False #  未被遍历

#  从文件中读入用户点评的json数据
#  存入类中
def load():
    f = open("useritem.json",encoding="utf-8")
    setting = json.load(f)
    ls=[]
    for v in setting["RECORDS"]:
        a=item()
        a.id=v["item_id"]
        a.review=v["review"]
        ls.append(a)
    f.close()
    return ls
# 将返回的店铺信息 统计单个店铺的词云
def deal(ls):
    for i in range(len(ls)):
        name = ls[i].id
        for j in range(i,len(ls)):
            if ls[j].id == name and ls[j].flag == False:
                ls[i].review += ls[j].review
                ls[j].flag=True
                ls[i].count+=1
    return ls
def output(ls):
    w =open("res.txt","w",encoding="utf-8")
    w.write("itemId     "+"count     "+"review     ")
    for v in ls :
        w.write(v.id+"     "+str(v.count)+"     "+v.review+"     \n")
    w.close()
if __name__ == "__main__":
   ls=load()
   ls=deal(ls)
   output(ls)
   for v in ls:
       print(v.id, v.review)
