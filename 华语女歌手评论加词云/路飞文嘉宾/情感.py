import pandas as pd
import snownlp as SnowNLP
import re
import os
import wordcloud
import jieba
import imageio
file = open('嘉宾.txt', mode='r', encoding='utf-8')
txt = file.read()
txt_list = jieba.lcut(txt)
string = ' '.join(txt_list)
shan = {'的', '这', '因为', '很', '和', '都', '那', '首歌', '听', '在', '不论', '是否', '我', '你', '了', '啦', '他', '她', '它', '吧', '是', '不是', '有', '没有', '会', '也', '就', '在', '不', '吗', '啊'}
wc = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='white',
    font_path='msyh.ttc',
    stopwords=shan
)
wc.generate(string)
wc.to_file('嘉宾.png')