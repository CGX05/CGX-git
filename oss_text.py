import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import re

edge=Options()
edge.add_argument("--headless")
web=webdriver.Edge(options=edge)
web.get("https://compass.gitee.com/explore")
# 模拟浏览器滚动页面操作
s=10
time_a=1
for i in range(s):
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(time_a)
http=web.page_source
# print(http)

#中文
pattern=r'<a class="mb-2 block truncate text-xl font-bold hover:underline" href="/collection/(.*?)">(.*?)</a>'
a=re.findall(pattern,http,re.DOTALL)
# print(a)

# 前6
pattern2=r'<p class="mb-1 truncate break-words text-xl font-bold  hover:underline"><a href="(.*?)">(.*?)</a></p>'
p=re.findall(pattern2,http,re.DOTALL)
# print(p)

# 近期热门
pattern3=r'<a class="flex w-full items-center text-sm hover:underline" href="(.*?)"><span class="mr-1 h-1 w-1 flex-shrink-0 bg-black"></span><span class="truncate">(.*?)</span></a>'
p1=re.findall(pattern3,http,re.DOTALL)
# print(p1)
for href3,text3 in p1:
    print(text3)

data=[]
for href1,text1 in a:
    data.append(text1)
# print(data)
data2=[]
for href2,text2 in p:
    data2.append(text2)
# print(data2)
# 深度学习框架：tensorflow，pytorch，mindspore
one=data[0]
one_1=",".join(data2[:3])
print("%s:%s"%(one,one_1))
# 关系型数据库：openGauss-server，oceanbase，tidb
two=data[1]
two_2=",".join(data2[3:])
print("%s:%s"%(two,two_2))
