import requests
import lxml
from lxml import etree

name = input("请输入歌手名称：")

url1 = "https://music.163.com/#/search/m/?s=" + name + "&type=1"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
cookie = {
    "_iuqxldmzr_": "32; _ntes_nnid=c6fa1f5ef3f742904bcb682ffd5c5bcf,1626254762837; _ntes_nuid=c6fa1f5ef3f742904bcb682ffd5c5bcf; NMTID=00OGoVZRGT6Wu98H0efq1FYObbyuRYAAAF6pFZnBg; WNMCID=xklcvv.1626254763547.01.0; WEVNSM=1.0.0; WM_NI=fWazgd053ej7nKTb1%2BmprYx%2BErVDOkpjnyYvxOVO2eRRN7kUJyU%2FDdnqfdi9zc7L%2BEI9GznmauM8sGFNPe%2BnJU1y4Lp8AA0p8bSYS0KP7eds%2F4V%2BKb3W2lDSMmslcBQdc0s%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeacb753b5b3bba5c85d95e78aa7c45f838b9fbab6738aa8a485f06db4e79ba7ea2af0fea7c3b92aa689af9be670f4ebfd86e93dae959c83b421afb0bebafb2187ae9aa5ce61b4b6a29adc7ebc919ab0b16f928e82d8ea5f8aa79bd0c770aeafaa85ec33babdf9adaa4f8be7899bed67a3ab83d9f24d8692a086aa668a8bff9ab748b4e88fa2b37cfcbe9dbad23c8990f986e779edec9accca6af189fe8dc7598fb3bd8de24a93bcadd1f237e2a3; WM_TID=YksikXYrfv9AQEUVARc%2ByJglNn0otFQw; __csrf=cf39475dc5a0512e309fe8e60f91cfca; MUSIC_U=28f8957ad04bc25375e7da68030d3be92b2e1588fe73dbf5ec78113e25d050de33a649814e309366; ntes_kaola_ad=1; playerid=40704021; JSESSIONID-WYYY=MXA5ueNDXhjc9KMyvG8UpwTn7IyMtufawA3tCT8VF1z7U1cymdjZHMcEwmD5w2VFm4knoq%2FD5uM5InUeIMs%5CHnq%2FbpyZ%2FIE9%2BT9bEJrJPIeYJxpk%5CCJ8A8%2B%5CnB695%2BEZXfgiZt2rCMTBU%5CCwUJRcDwfQDPbfJ4NO6V7Scd7ofBls0%2F3%5C%3A1626286158966"}
try:
    r = requests.get(url1, headers=header, cookies=cookie)

except requests.exceptions.ConnectionError:
    r.status_code = "Connection refused"
    print(response.status_code)

from selenium import webdriver

driver = webdriver.Chrome()
driver.get(r.url)
iframe = driver.find_element_by_xpath("//iframe")  # 可以修改xpath, 这里默认获取到第一个iframe节点
driver.switch_to.frame(iframe)  # 切换到iframe中
id1 = []
id2 = []
names = []
a1 = driver.find_elements_by_xpath('//html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div/a[1]')
n1 = driver.find_elements_by_xpath('//html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div/a[1]/b')
for i in range(10):
    a2 = a1[i].get_attribute('href')
    id1.append(a2)
    n2 = n1[i].get_attribute('title')
    names.append(n2)
for i in id1:
    id2.append(i.split('=')[1])

for i in range(10):
    music=requests.get(url="http://music.163.com/song/media/outer/url?id="+id2[i]+".mp3",headers=header)
    with open(r"C:\Users\asus\Desktop\歌曲\%s.mp3"%(name+'-' +names[i]),'wb') as file:
        file.write(music.content)
        print('%s.mp3 success!' %(name+'-' +names[i]))
