# coding=cp936

import urllib
import urllib2
import re
import time
import random
import shutil

print '.'*20+'开始采集代理'+'.'*20

f = open('proxy_list.txt','w')
exp1 = re.compile("(?isu)<tr[^>]*>(.*?)</tr>")
exp2 = re.compile("(?isu)<td[^>]*>(.*?)</td>")
htmlSource = urllib.urlopen("http://cn-proxy.com/").read()
for row in exp1.findall(htmlSource):
   for col in exp2.findall(row)[:2]:

    f.write('\n'+col)

f.close()

#with open('proxy_list.txt', 'r') as f:
#    with open('proxy_list.txt.new', 'w') as g:
#        for line in f.readlines():
#            if '服务器地址' not in line:
#                g.write(line)
#shutil.move('proxy_list.txt.new', 'proxy_list.txt')

#with open('proxy_list.txt', 'r') as f:
#    with open('proxy_list.txt.new', 'w') as g:
#        for line in f.readlines():
#            if '端口' not in line:
#                g.write(line)
#shutil.move('proxy_list.txt.new', 'proxy_list.txt')

file = open("proxy_list.txt",'r')
lines = file.readlines()
newlines = []
j = 1
for i in range(len(lines)):
    if(j!=len(lines)-2):
        string = lines[j].replace('\n','')+':'+lines[j+1].replace('\n','')
        newlines.append(string)
        j=j+2

open("proxy_list.txt","w").write('%s' % '\n'.join(newlines))
file.close()


print '.'*20+'采集完成'+'.'*20

##########################################################################################3
print '*'*50
print '本程序主要采集豆瓣<请不要害羞>小组的图片'
print '采集的图片在文件夹Doubanimg内.'
print '代理采集程序没有验证，所以如果不成功请重新运行本程序.'
print '本程序在Win下有BUG可能需要多执行几次'
print '#'*50
print 'By 肾虚公子'
print '#'*50

f0=open('proxy_list.txt','r')
dat0=f0.readlines()
f0.close()
proxy_SJ = random.choice(dat0)


proxy_handler = urllib2.ProxyHandler({'http':'%s'%proxy_SJ})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

def gethtml2(url2):
    html2 = urllib2.urlopen(url2).read().decode('utf-8')
    return  html2

def gettoimg(html2):
    reg2 = r'http://www.douban.com/group/topic/\d+'
    toplist = re.findall(reg2,html2)
    x = 0
    for topicurl in toplist:
        x+=1
    return topicurl

def download(topic_page):
    reg3 = r'http://img3.douban.com/view/group_topic/large/public/.+\.jpg'
    imglist = re.findall(reg3,topic_page)
    i = 1
    download_img = None
    for imgurl in imglist:
        img_numlist = re.findall(r'p\d{7}',imgurl)
        for img_num in img_numlist:
            download_img = urllib.urlretrieve(imgurl,'Doubanimg/%s.jpg'%img_num)
            time.sleep(1)
            i+=1
            print (imgurl)
    return download_img

page_end = int(input('请输入采集页码数:'))
print '页面正在采集中，如遇错误请重新再试'+'.'*50
num_end = page_end*25
num = 0
page_num = 1
while num<=num_end:
    html2 = gethtml2('http://www.douban.com/group/haixiuzu/discussion?start=%d'%num)
    topicurl = gettoimg(html2)
    topic_page = gethtml2(topicurl)
    download_img=download(topic_page)
    num = page_num*25
    page_num+=1

else:
    print('程序采集完成')

