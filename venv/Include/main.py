import urllib.request
import re
from bs4 import BeautifulSoup


# 打印爬取网页的各类信息
def getAddress(url):
    list=[]
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    soup = BeautifulSoup(data, 'html.parser')
    # 爬取结果
    response = urllib.request.urlopen(request)
    for link in soup.find_all("a"):  # 获取标签为img的内容\
        try:
            address = link.get('href')  # 获取标签属性为href的内容，即图片地址
            pattern = '^http:|https:'
            m = re.match(pattern, address)
            if (m != None):
                list.append(address)
                print(address)
        except:
            print("解析网页错误")
    return  list


if __name__ == '__main__':

    # 网址
    url = "http://www.baidu.com/"
    list = getAddress(url)
    # 打印结果
    s = set(list)  # 去重
    for address in s:
        # 根据获取到的网页链接继续遍历
        getAddress(address)