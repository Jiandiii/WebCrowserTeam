import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
import re

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67"
}

data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_29814898",
    "threadId": "R_SO_4_29814898"
}

f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
e = "010001"
i = "Bm56RleYW815Ym2l"

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def get_encSecKey():
    return "13038f2eb1481e0ebfa4578a3c35d216f233d8c78214a1655c8f82100033794a163e5ffb0a39dc13968eae60412576716fbe6c203fe564f6c37d2516b21383020dd80ac0faf064416358557eecc1b8aa96d9072552793a700e965fbe5d5be24bfccfb9ce450aa706401d381dcf606a8e25778326dd6ca7a4b958cfa397a2e15c"

def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second

def enc_params(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))
    return str(b64encode(bs), "utf-8")

# resp = requests.post(url, data={
#     "params": get_params(json.dumps(data)),
#     "encSecKey": get_encSecKey()
# })
if __name__ == '__main__':

    page = int(input('请输入需要爬取的页数：'))
    print('爬爬爬~')
    fp = open('./contend.txt', 'w', encoding='utf-8')
    for j in range(1,page+1):
        page_num = str(j*20)
        data = {
            'csrf_token': "",
            'cursor': "-1",
            'offset': "0",
            'orderType': "1",
            'pageNo': "1",
            'pageSize': page_num,
            'rid': "R_SO_4_29814898",
            'threadId': "R_SO_4_29814898"
        }

        response = requests.post(url,data={
            "params":get_params(json.dumps(data)),
            "encSecKey":get_encSecKey()
        },headers=headers)


        result = json.loads(response.content.decode('utf-8'))
        #hotComments
        for hot in range(len(result['data']['hotComments'])):
            # fp.write('昵称：' + result['data']['hotComments'][hot]['user']['nickname'] + '\n')
            fp.write(result['data']['hotComments'][hot]['content'] + '\n')
            # fp.write('点赞数' + str(result['data']['hotComments'][hot]['likedCount']) + '\n')

        #print(result['data']['hotComments'][1]['user']['nickname'])

        #comments
        for r in range(20):
            fp.write('comments')
            # fp.write('昵称：'+result['data']['comments'][r]['user']['nickname']+'\n')
            fp.write(result['data']['comments'][r]['content']+'\n')
            # fp.write('点赞数'+str(result['data']['comments'][r]['likedCount'])+'\n')
    print('爬完了~')
