# encoding=utf-8
import jieba
import wordcloud
import json
class resturant:
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
        a=resturant()
        a.id=v["item_id"]
        a.review=v["review"]
        a.flag=False
        ls.append(a)
    f.close()
    return ls
# 将返回的店铺信息 统计单个店铺的词云
def deal(ls):
    for i in range(len(ls)):
        if ls[i].flag == False:
            name = ls[i].id
            ls[i].flag=True
            for j in range(i, len(ls)):
                if ls[j].id == name and ls[j].flag == False:
                    ls[i].review += ls[j].review
                    ls[j].flag = True
                    ls[i].count += 1
                    ls[j].id="zzzzzzzz"
    return ls
# 将结果写入文件
def output(ls):
    di={}
    for i in range(0,len(ls)):
        di[ls[i].id]=ls[i].review
    print(ls[0].id+" "+ls[0].review)
    print(di[ls[0].id])
    #di[ls[0].id]=ls[0].review
    #di[ls[1].id]=ls[1].review
    with open("record.json", "w",encoding="utf-8") as f:
        json.dump(di, f,ensure_ascii=False)
    f.close()
    print("加载入文件完成...")
if __name__=="__main__":
    ls=load()
    ls=deal(ls)
    output(ls)