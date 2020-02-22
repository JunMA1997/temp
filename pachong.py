import time
import re
import random
import requests
from bs4 import BeautifulSoup
import csv
import sys


count = 0

#url = 'http://epub.cnki.net/grid2008/brief/detailj.aspx?filename=RLGY201806014&dbname=CJFDLAST2018'

#这个headers信息必须包含，否则该网站会将你的请求重定向到其它页面
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection':'keep-alive',
    'Host':'dict.youdao.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

def get_url_list(start_url,filename):
    url_list = []
    with open(filename,"r",encoding="utf-8") as f:
        words=f.read()
        words=words.split("\n")
        for word in words:
            url = start_url + word
            url_list.append(url)
    # print(url_list)
    return url_list

def get_data(url_list, fw):
    try:
        # 通过url_results.txt读取链接进行访问
        
        for url in url_list:
            global count
            # print(url)
            if url == '':
                continue
            word=url.split("q=")[1]
            # print(word)
            try:
                html = requests.get(url.replace('\n', ''), headers=headers)
                soup = BeautifulSoup(html.text, 'html.parser')
            except KeyboardInterrupt:
                
                exit()
            except:
                print("error")
            # print(soup.find('div',class_="trans-wrapper clearfix").find('div',class_="trans-container").find('p',class_="wordGroup"))
            
            
            translation=[]

            try:
                for byGroup in soup.find('div',class_="trans-wrapper clearfix").find('div',class_="trans-container").find_all('p'):                                    
                    for t in byGroup.find_all("a",class_="search-js"):
                        translation.append(t.get_text())
                    
                # 获取翻译
            except:
                pass           
            if(not translation):
                with open('noresults.txt','w',encoding='utf-8',newline='') as f1:
                    f1.write(word)
                    print(count)
                    count+=1
                    continue
            print(count)
            count+=1
            fw.writerow([word,translation])
            
        print("爬取完毕")
    finally:
        #print()
        a=0

if __name__ == '__main__':
    try:
        with open('results.txt','w',encoding='utf-8',newline='') as f:
            fw = csv.writer(f)            
            start_url = "http://dict.youdao.com/search?q="
            url_list = get_url_list(start_url,sys.argv[1])
            print("开始爬取")
            get_data(url_list,fw)
    finally:
        f.close()
