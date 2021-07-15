import requests
from lxml import etree

url = 'https://music.163.com/discover/artist'


# 返回解析后的网页字符串格式


def get_xpath(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ( KHTML, like Gecko) Chrome'
                      '/78.0.3904.70 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return etree.HTML(response.text)


# parse()函数获取分类页的分类项目名称及跳转URL
# 可以通过修改不同的html.xpath()中的内容进入不同分类

def parse():
    html = get_xpath(url)
    names = html.xpath('/html/body/div[3]/div[1]/div/div[4]/ul/li/a/text()')
    params = html.xpath('/html/body/div[3]/div[1]/div/div[4]/ul/li/a/@href')
    print(names)
    print(params)
    fenlei_url = 'https://music.163.com' + input("params:")
    print(fenlei_url)
    parse_fenlei(fenlei_url)


# parse_fenlei()函数获取热门歌手们的URL


def parse_fenlei(fenlei_url):
    html = get_xpath(fenlei_url)
    hot_url_params = html.xpath('/html/body/div[3]/div[2]/div/div/div[2]/ul/li/div/a/@href')
    for i in hot_url_params:
        hot_url = 'https://music.163.com' + i
        print(hot_url)
        parse_singer(hot_url)


#  跳至艺人简介部分
#

def parse_singer(hot_url):
    html = get_xpath(hot_url)
    params = html.xpath('/html/body/div[3]/div[1]/div/div/ul/li[4]/a/@href')
    singers_url = 'https://music.163.com' + params[0]
    print(singers_url)
    parse_detail(singers_url)


# 展示艺人详细信息


def parse_detail(singers_url):
    html = get_xpath(singers_url)
    desc_list = html.xpath('//div[@class="n-artdesc"]/p/text()')
    name = html.xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/h2[1]/text()')
    if desc_list != []:
        write_singer(desc_list, name[0])
    else:
        print('很遗憾，该歌手或乐队暂无介绍！！！')


# 将信息转为txt文档存储至本地

def write_singer(desc_list, name):
    file_path = 'D:\GitCode\Python\chenff\歌手信息\韩国女歌手/' + name + '.txt'
    file = open(file_path, 'a', encoding='utf-8')
    file.write('\n'.join(desc_list))


if __name__ == '__main__':
    parse()
    print("文件已经全部存储完毕！！！")
