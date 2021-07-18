# import pandas as pd
import re
import csv
from web实训项目.bean.item import comment_item

def make_list():
    f=open("D:/PyCharm Community Edition 2021.1.3/web实训项目/preDispose/country.csv",'r',encoding="utf-8")
    file=csv.reader(f)
    list=[]
    i=0
    for temp in file:
        if i!=0 and len(temp)==11:
            #把是否是VIP转换成True or False
            flag=False
            # print(temp)
            if temp[1]=="是":
                flag=True
            #利用正则表达式去除表情等有关的无用字符
            if re.sub(r'[\[\]]+',"",re.sub(r'(?<=\[)(.*?)(?=\])',"",temp[10]))!="":
                #替换评论内容中的换行符
                i=comment_item(temp[0],flag,temp[2],temp[3],temp[4],temp[5],temp[6],int(temp[7]), temp[8], temp[9], re.sub(r'\n',"",temp[10]))
                # print(i)
                list.append(i)
            # else:
                # print(temp[5])
        i=1
    return list

def write():
    f = open('disposed.csv', 'w', encoding='utf-8')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f, lineterminator='\n')
    csv_writer.writerow(["user", "VIP", "dynamic", "foucs", "fans", "district", "listen_songs", "acclaim", "comment", "time", "content"])
    for temp in make_list():
        print(temp)
        csv_writer.writerow([temp.name, temp.vip, temp.dynamic, temp.foucs_num, temp.fans, temp.district, temp.listen_songs, temp.acclaim, temp.commented_num, temp.time, temp.content])
    print("ok")
    f.close()
write()