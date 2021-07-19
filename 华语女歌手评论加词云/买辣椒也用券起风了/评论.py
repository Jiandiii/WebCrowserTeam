import time
import re
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\pythonProject\venv\Scripts\chromedriver.exe')
driver.get("https://music.163.com/#/song?id=1330348068")  # 歌曲链接
driver.implicitly_wait(10)  # 隐试等待
driver.maximize_window()  # 最大化浏览器
driver.switch_to.frame(0)
# 下拉页面
js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
driver.execute_script(js)
divs = driver.find_elements_by_css_selector('.itm')
# 定义爬取的评论数
for click in range(100):
    divs = driver.find_elements_by_css_selector('.itm')
    for div in divs:
        cnt = div.find_element_by_css_selector('.cnt.f-brk').text
        cnt = cnt.replace('\n', '')
        cnt = re.findall('：(.*)', cnt)[0]  # 去掉发布评论的人名字
        # 定义保存路径
        with open('起风了.txt', mode='a', encoding='UTF-8') as f:
            f.write(cnt + '\n')
    driver.find_element_by_css_selector('.znxt').click()
    time.sleep(1)
driver.quit()