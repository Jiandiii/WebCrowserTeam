from selenium import webdriver
import time
import cloudmusic
import json
from bs4 import  BeautifulSoup

wd = webdriver.Chrome(r'e:\chromedriver.exe')


wd.get('https://music.163.com/#/discover/toplist?id=3778678')
#找热歌榜
wd.switch_to.frame('g_iframe')

toplist=wd.find_element_by_id('song-list-pre-cache')
#songs
songs_list=toplist.find_elements_by_class_name('tt')
n=0
for song in songs_list:
    n=n+1
    if n>50:
        break
    uid_list=[]
    u_birth_list=[]
    u_place_list=[]
    link = song.find_element_by_tag_name('a').get_attribute('href')
    wd1 = webdriver.Chrome(r'e:\chromedriver.exe')
    wd1.get(link)
    time.sleep(1)
    wd1.switch_to.frame('g_iframe')
    song_name=wd1.find_element_by_class_name('f-ff2').text
    i=0
    while 1:
        i=i+1
        if i>50:
            user_list = [uid_list, u_birth_list, u_place_list]
            filename = song_name + '.json'
            with open(filename, 'w') as file_obj:
                json.dump(user_list, file_obj)
            break
        comments=wd1.find_elements_by_class_name('itm')
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

        pages = wd1.find_element_by_css_selector('div[class*="u-page"]')
        target = pages.find_element_by_xpath('//*[contains(@class,"znxt")]')
        if 'js-disabled' in target.get_attribute('class'):
            user_list=[uid_list,u_birth_list,u_place_list]
            filename=song_name+'.json'
            with open(filename, 'w') as file_obj:
                json.dump(user_list, file_obj)
            break
        else:
            wd1.execute_script("arguments[0].scrollIntoView();", target)
            try:
                target.click()
                time.sleep(3)
            except:
                break

    #爬取完毕关闭窗口
    wd1.close()
wd.close()
pass