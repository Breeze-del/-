# encoding=utf-8
import json
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import pickle
import matplotlib.pyplot as plt
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
# 将结果写入文件
def output(ls):
    str = ""
    for v in ls:
        str += v.review
    # w =open("res.txt","w",encoding="utf-8")
    # w.write("itemId     "+"count     "+"review     ")
    # for v in ls :
    #     w.write(v.id+"     "+str(v.count)+"     "+v.review+"     \n")
    # w.close()
    w = open("word.txt","w",encoding="utf-8")
    w.write(str)
    w.close()
# 词云分析
def cloud():
    fr = open('word.txt', 'r',encoding="utf-8")
    text = fr.read()
    fr.close()
    # jieba分词
    removes = ['团购', '点评', '但是', '还是', '感觉', '就是', '而且', '没有', '还有', '不过', '知道']
    for w in removes:
        jieba.del_word(w)
    words = jieba.lcut(text)
    words = [w for w in words if w not in removes]
    cuted = ' '.join(words)
    # wordCloud 生成词云
    fontpath = "SourceHanSansCN-Regular.otf"
    #backgroud_Image = plt.imread('cloud.jpg')
    wc = WordCloud(background_color='white',  # 设置背景颜色
                   #mask=backgroud_Image,  # 设置背景图片
                   max_words=100,  # 设置最大现实的字数
                   stopwords=STOPWORDS,  # 设置停用词
                   font_path=fontpath,  # 设置字体格式，如不设置显示不了中文
                   max_font_size=500,  # 设置字体最大值
                   min_font_size=30,  # 设置字体最小值
                   random_state=42,  # 设置有多少种随机生成状态，即有多少种配色方案
                   collocations=False, # 避免重复的单词
                   width=1600, height=1200,margin=10, # 设置图像宽高，字体间距
                   )
    wc.generate(cuted)
    # image_colors = ImageColorGenerator(backgroud_Image)
    # wc.recolor(color_func=image_colors)
    plt.figure(dpi=100)
    plt.imshow(wc, interpolation='catrom', vmax=1000)
    plt.axis('off')
    plt.savefig("zongpingfen1.jpg")
    plt.show()
if __name__ == "__main__":
    cloud()
   # ls=load()
   # ls=deal(ls)
   # output(ls)
   # for v in ls:
   #     print(v.id, v.review)

