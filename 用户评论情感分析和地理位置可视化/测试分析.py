#coding:utf-8
import re

from matplotlib import collections
from pyecharts.charts import Geo, Line, Pie
from snownlp import SnowNLP
import pandas as pd
import csv
import collections
import pyecharts
import numpy as np # numpy数据处理库
import wordcloud # 词云展示库
import matplotlib.pyplot as plt # 图像展示库
from wordcloud import wordcloud
from preDispose.data_cleaning import make_list
from pyecharts import options as opts

def get_content():
    '''
    @return:
    '''
    lists=[]
    f=open("D:/PyCharm Community Edition 2021.1.3/web实训项目/preDispose/disposed.csv",'r',encoding="utf-8")
    file=csv.reader(f)
    count=0
    for i in file:
        if count!=0:
            print(i[10])
            s = SnowNLP(i[10])
            print(str(s.sentiments))
            lists.append(s.sentiments)
        count+=1;
    lists = [round(i, 3) for i in lists]
    return lists

def draw_line_sentiment(lists):
    print(lists)
    c=Line(init_opts=opts.InitOpts(width='2000px',height='600px'))
    c.add_xaxis(xaxis_data=list(range(1,len(lists)+1)))
    # c.add_xaxis(xaxis_data=content)
    c.add_yaxis(series_name="",y_axis=lists)

    data_zoom = {
        "show": True,
        "title": {"zoom": "data zoom", "back": "data zoom restore"}
    }
    c.set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(title="情感分析得分走势图"),
        # 设置图例is_show=False是不显示图例
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置提示项
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        # 工具箱的设置
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(data_zoom=data_zoom))

    )
    c.set_series_opts()
    c.render('line_sentiments.html')
    line = pyecharts.Line("情感分析得分走势图", width=1200, height=600)
    line.add("情感分析得分",list(range(1,len(lists)+1)),lists, mark_point=['average'], is_datazoom_show=True,is_smooth=True)
    line.render('line_sentiments.html')


#-----------------------------------
def draw_pie_sentiment(lists):
    s = np.arange(0, 1.1, 0.1)
    fenzu = pd.cut(lists, s, right=False)  # 分组区间,长度91
    pinshu = fenzu.value_counts()  # series,区间-个数
    print(fenzu.categories)
    list_label=["(0.0-0.1)", "(0.1-0.2)", "(0.2-0.3)", "(0.3-0.4)", "(0.4-0.5)", "(0.5-0.6)", "(0.6-0.7)", "(0.7-0.8)", "(0.8-0.9)", "(0.9-1.0)"]
    # pie = pyecharts.Pie("评论情感色彩评分", '0->1（消极->积极）', title_pos='center')
    # pie.add('天气类型', list_label, pinshu.tolist(),radius=[20,70],is_label_show=True,legend_pos = 'left', label_text_color = None, legend_orient = 'vertical')
    # pie.render('pie_sentiments.html')

    pie = Pie(init_opts=opts.InitOpts(width='1000px', height='600px'))
    data_pie = [list(i) for i in zip(list_label, pinshu.tolist())]
    pie.add(series_name="该区间占比：", data_pair=data_pie)
    # 设置全局项
    pie.set_global_opts(title_opts=opts.TitleOpts(title="评论情感色彩评分",subtitle="0->1（消极->积极）", pos_left='center', pos_top=20))
    # 设置每项数据占比
    pie.set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item', formatter="{a} <br/> {b}:{c} ({d}%)"))
    pie.render('pie_sentiments.html')


# draw_line_sentiment(get_content())
draw_pie_sentiment(get_content())


def make_wordCloud():
    object_list=[]
    for temp in make_list():
        object_list.append(temp.content)
    print(len(object_list))
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
    print(word_counts_top10)  # 输出检查
    wc = wordcloud.WordCloud(
        font_path = 'C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
        max_words = 200,  # 最多显示词数
        max_font_size = 100  # 字体最大值
    )
    wc.generate_from_frequencies(word_counts)  # 从字典生成词云
    # image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
    # wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐标轴
    plt.show()  # 显示图像

# make_wordCloud()
def VIP_rate():
    true=0
    false=0
    for temp in make_list():
        if temp.vip:
            true+=1
        else:
            false+=1
    # pie = pyecharts.Pie("评论用户中是否VIP比列", '愚人的国度-孙燕姿', title_pos='center')
    # pie.add('', ["vip用户","非vip用户"], [true,false],is_label_show=True,legend_pos = 'left', label_text_color = None, legend_orient = 'vertical', radius = [30, 75])
    # pie.render('Pie-VIP.html')

    pie = Pie(init_opts=opts.InitOpts(width='1000px', height='600px'))
    data_pie = [list(i) for i in zip(["vip用户","非vip用户"],[true,false])]
    pie.add(series_name="该类用户占比：", data_pair=data_pie)
    # 设置全局项
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title="评论用户中VIP比列", subtitle="愚人的国度-孙燕姿", pos_left='center', pos_top=20))
    # 设置每项数据占比
    pie.set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item', formatter="{a} <br/> {b}:{c} ({d}%)"))
    pie.render('pie_VIP.html')
VIP_rate()

def map():
    districts=[]
    f = open("D:/PyCharm Community Edition 2021.1.3/web实训项目/preDispose/disposed.csv", 'r', encoding="utf-8")
    file = csv.reader(f)
    flag = False
    wrong=["","其它","瑞士","日本","冰岛","玻利维亚","荷兰","委内瑞拉","阿尔及利亚","丹麦","泰国"
        ,"菏泽市","英国","意大利","捷克","爱尔兰","挪威","美国","卢森堡","伯利兹"]
    for i in file:
        if flag:
            if len(i[5])>4:
                temp=re.findall(r'-(.*?)$',i[5])[0].strip()
                # print(temp)
                if(temp not in wrong):
                    districts.append(re.findall(r'-(.*?)$',i[5])[0].strip())
            elif i[5].strip() not in wrong:
                print(i[5].strip())
                districts.append(i[5].strip())
        flag=True;
    count = {}  # 将结果用一个字典存储
    # 统计结果
    for value in districts:
        # get(value, num)函数的作用是获取字典中value对应的键值, num=0指示初始值大小。
        count[value] = count.get(value, 0) + 1
    # 打印输出结果
    list1=[key for key in count.keys()]
    list2=[value for value in count.values()]
    list3=[]
    for temp in range(len(list1)):
        item=[list1[temp],list2[temp]]
        list3.append(item)
    # print(list3)
    geo = (
        Geo()
            .add_schema(maptype="china")
            .add("geo", [['北京市', 34], ['合肥市', 6], ['武汉市', 30], ['赣州市', 6], ['葫芦岛市', 1], ['威海市', 3], ['广州市', 25], ['苏州市', 8], ['毕节地区', 1], ['兴安盟', 1], ['宁德市', 3], ['呼和浩特市', 3], ['汕头市', 6], ['哈尔滨市', 15], ['深圳市', 25], ['济宁市', 4], ['东莞市', 5], ['抚州市', 2], ['滨州市', 2], ['济南市', 14], ['宜昌市', 2], ['吉林市', 2], ['南京市', 21], ['烟台市', 2], ['南宁市', 5], ['安庆市', 5], ['兰州市', 12], ['上海市', 24], ['宜宾市', 2], ['泉州市', 5], ['温州市', 7], ['百色市', 2], ['江门市', 2], ['扬州市', 4], ['太原市', 4], ['庆阳市', 4], ['天津市', 11], ['成都市', 21], ['宿迁市', 1], ['南通市', 1], ['铜仁地区', 2], ['杭州市', 20], ['丽水市', 1], ['郑州市', 11], ['西安市', 20], ['珠海市', 2], ['乌鲁木齐市', 3], ['荆州市', 2], ['石嘴山市', 1], ['昌吉回族自治州', 1], ['湖州市', 2], ['濮阳市', 1], ['青岛市', 6], ['周口市', 3], ['承德市', 2], ['柳州市', 3], ['金华市', 7], ['六安市', 4], ['宿州市', 1], ['揭阳市', 2], ['广安市', 5], ['佛山市', 15], ['通化市', 2], ['沈阳市', 2], ['桂林市', 3], ['上饶市', 2], ['鹤壁市', 1], ['临沂市', 3], ['乐山市', 1], ['广元市', 1], ['金昌市', 1], ['清远市', 1], ['衢州市', 1], ['石家庄市', 5], ['焦作市', 1], ['信阳市', 1], ['厦门市', 3], ['玉溪市', 1], ['商丘市', 2], ['南昌市', 6], ['邢台市', 2], ['沧州市', 1], ['长沙市', 22], ['运城市', 1], ['泰安市', 2], ['嘉兴市', 2], ['常德市', 1], ['大连市', 5], ['阳江市', 2], ['漳州市', 3], ['新乡市', 2], ['贵阳市', 5], ['曲靖市', 2], ['长春市', 7], ['重庆市', 26], ['达州市', 3], ['聊城市', 1], ['郴州市', 1], ['天水市', 2], ['无锡市', 6], ['衡阳市', 3], ['绍兴市', 2], ['镇江市', 3], ['三明市', 1], ['娄底市', 1], ['德州市', 2], ['宝鸡市', 1], ['香港', 1], ['开封市', 2], ['红河哈尼族彝族自治州', 1], ['咸宁市', 2], ['鄂尔多斯市', 1], ['阜阳市', 2], ['盐城市', 2], ['泸州市', 4], ['福州市', 2], ['枣庄市', 1], ['邯郸市', 3], ['茂名市', 2], ['亳州市', 1], ['黄冈市', 3], ['惠州市', 2], ['常州市', 3], ['漯河市', 1], ['桃园县', 1], ['南阳市', 1], ['潍坊市', 3], ['云浮市', 2], ['哈密地区', 2], ['昆明市', 3], ['澎湖县', 1], ['保山市', 1], ['廊坊市', 1], ['西双版纳傣族自治州', 2], ['许昌市', 2], ['襄樊市', 2], ['汕尾市', 1], ['保定市', 3], ['十堰市', 2], ['延边朝鲜族自治州', 1], ['贵港市', 1], ['台北市', 3], ['黄石市', 1], ['海口市', 2], ['崇左市', 1], ['临汾市', 1], ['北海市', 1], ['拉萨市', 1], ['通辽市', 1], ['衡水市', 1], ['汉中市', 3], ['台州市', 2], ['宜春市', 2], ['内江市', 1], ['巴中市', 3], ['怒江傈僳族自治州', 1], ['淄博市', 1], ['西宁市', 1], ['芜湖市', 1], ['梅州市', 3], ['吴忠市', 1], ['永州市', 2], ['锦州市', 1], ['宁波市', 1], ['日照市', 1], ['伊犁哈萨克自治州', 2], ['林芝地区', 1], ['湛江市', 1], ['渭南市', 1], ['临沧市', 1], ['岳阳市', 1], ['洛阳市', 1], ['甘南藏族自治州', 1], ['舟山市', 1], ['四平市', 1]])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="评论者地理位置分布图"),
        )
    )
    geo.render("map_user_distribute.html")
map()


f.close()