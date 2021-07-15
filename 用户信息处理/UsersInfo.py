#爬取单独一首歌的评论用户信息
link='https://music.163.com/#/song?id=29004400'
#link为需要爬取歌曲链接
from selenium import webdriver
import time
import cloudmusic
import json

wd = webdriver.Chrome(r'e:\chromedriver.exe')

wd.get(link)
uid_list=[]
u_birth_list=[]
u_place_list=[]
time.sleep(1)
wd.switch_to.frame('g_iframe')
song_name=wd.find_element_by_class_name('f-ff2').text

i=0
while 1:
    i=i+1
    #前100页评论
    if i>100:
        user_list = [uid_list, u_birth_list, u_place_list]
        filename = song_name + '.json'
        with open(filename, 'w') as file_obj:
            json.dump(user_list, file_obj)
        break
    comments=wd.find_elements_by_class_name('itm')
    for comment in comments:
        user=comment.find_element_by_class_name('head')
        uid=user.find_element_by_tag_name('a').get_attribute('href')
        uid = int(uid.replace('https://music.163.com/user/home?id=', ''))
        uid_list.append(uid)
        try:
            u_birth=int(time.localtime(cloudmusic.getUser(uid).birthday/1000).tm_year)
        except:
            u_birth=None
        u_birth_list.append(u_birth)
        try:
            place=cloudmusic.getUser(uid).province
        except:
            place=None
        u_place_list.append(place)

    pages = wd.find_element_by_css_selector('div[class*="u-page"]')
    target = pages.find_element_by_xpath('//*[contains(@class,"znxt")]')
    if 'js-disabled' in target.get_attribute('class'):
        user_list=[uid_list,u_birth_list,u_place_list]
        filename=song_name+'.json'
        with open(filename, 'w') as file_obj:
            json.dump(user_list, file_obj)
        break
    else:
        wd.execute_script("arguments[0].scrollIntoView();", target)
        try:
            target.click()
            time.sleep(1)
        except:
            user_list = [uid_list, u_birth_list, u_place_list]
            filename = song_name + '.json'
            with open(filename, 'w') as file_obj:
                json.dump(user_list, file_obj)
            break

#爬取完毕关闭窗口
wd.close()
