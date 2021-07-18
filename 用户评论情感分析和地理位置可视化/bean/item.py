# author:ever
# contact: test@test.com
# datetime:2020/6/19 23:20
# software: PyCharm

"""
文件说明：定义实体类

"""
class comment_item:
    # 定义基本属性
    name = ''
    vip = False
    acclaim=0
    commented_num=0
    time=""
    content=""
    dynamic=""
    foucs_num=""
    fans=""
    district=""
    listen_songs=""

    # 定义构造方法
    def __init__(self,name,vip,dynamic,foucs_num,fans,district,listen_songs,acclaim,commented_num,time,content):
        self.name = name
        self.vip = vip
        self.dynamic=dynamic
        self.foucs_num=foucs_num
        self.fans=fans
        self.district=district
        self.listen_songs=listen_songs
        self.acclaim = acclaim
        self.commented_num = commented_num
        self.time = time
        self.content = content

    # 定义toString
    def __str__(self):
        return '昵称：%s|VIP：%s|动态数：%s|关注量：%s|粉丝数：%s|地区：%s|累计听歌数：%s|点赞：%s|被评论数：%s|时间：%s|内容：%s' % (self.name, self.vip, self.dynamic, self.foucs_num, self.fans, self.district, self.listen_songs, self.acclaim, self.commented_num, self.time, self.content)
