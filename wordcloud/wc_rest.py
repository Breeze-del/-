# encoding=utf-8
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import flask
class Cloud(BaseHTTPRequestHandler):
    def do_GET(self):
        qrImg={'src':'www.baidu.com'}
        self.protocal_version = 'HTTP/1.1'  # 设置协议版本
        self.send_response(200)  # 设置响应状态码
        self.send_header("Welcome", "Contect")  # 设置响应头
        self.end_headers()
        self.wfile.write(json.dumps(qrImg).encode())  # 输出响应内容

# 输入一个店铺id 返回生成的词云图片地址
def cloud(itemid, di):
    text = di[itemid]
    # jieba分词
    removes = ['团购', '点评', '但是', '还是', '感觉', '就是', '而且', '没有',
               '还有', '不过', '知道','什么','比较','这里''我们','以前','一下','一次']
    for w in removes:
        jieba.del_word(w)
    words = jieba.lcut(text)
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
    plt.savefig("./CloudImages/"+itemid+".jpg")
    plt.show()

# 返回字典类型
def JD():
    f = open("record.json", encoding="utf-8")
    di = json.load(f)
    return di

# 开启http服务
def start__server(host):
    http_server = HTTPServer(host,Cloud)
    http_server.serve_forever() #设置监听并一直接受请求
    print("Starting server, listen at: %s:%s" % host)

if __name__=="__main__":
    host = ('localhost', 8888)
    items = JD()
    start__server(host)
