import requests
from lxml import etree
from bs4 import BeautifulSoup
import csv

def getinfo(url):

    header = {
        "HOST": "account.for-test.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        "Cookie": "PHPSESSID=8r8u5oh198r6dlrrgs949iueg0; yunsuo_session_verify=a94ca3b6a89d4b38dda7982df1c9d509; yunsuo_leech_key=5",

        }

    res = requests.get(url,headers=header)
    # html = etree.HTML(res.text)

    soup = BeautifulSoup(res.content, 'lxml')
    contents = soup.find_all('span', 'con')

    def new_list(i):
        s = str(i).replace(r'<span class="con">', '').replace(r'</span>', '')
        return s

    content = list(map(new_list, contents))

    qes = content[0]
    a = content[1]
    b = content[2]
    c = content[3]
    d = content[4]
    ans = content[5]
    jiexi = content[6]
    info = content[7]

    return [qes,a,b,c,d,ans,jiexi,info]

def save_data(infos):

    with open('tiku30.csv','a',newline='',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(infos)

if __name__ == "__main__":

    for i in range(1,91):
        url = "http://account.for-test.cn/jlptshitidata.php?shitibiaoming=t_30&tihao={}&shitibiao=30&yanzheng=1&yshipin=&jinru=0".format(i)
        infos = getinfo(url)
        save_data(infos)
