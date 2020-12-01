#!/usr/bin/env python
# coding: utf-8
print("               朝陽行政電腦設備維修爬蟲 v0.0.2 By:Pin-Yi-chuchu")
print("爬蟲中.")
print("爬蟲中.....")
print("爬蟲中.........")
print("爬蟲中.............")
print("爬蟲中..................")
print("爬蟲中...................................")
print("")

import requests
import datetime
import smtplib
from email.mime.text import MIMEText
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
from bs4 import BeautifulSoup
response = requests.get('http://t2-5f-249.cyut.edu.tw/sys_rpi/auth.asp?txt_username=10630101&txt_passwd=@10630101')
response.encoding = 'big5'
html = response.text
print("-----------------------------以下輸出訊息-----------------------------")
ans = html.find('網路組')
CRED = '\033[41m'  
CEND = '\033[0m'
GRED = '\033[42m'  
print(theTime)
if ans == -1:
    ans = '[ 網路組 ] 目前沒有維修'
else:
    ans = '[ 網路組 ] 有維修!!!有維修!!!有維修!!!'
    mime=MIMEText("有維修!!!有維修!!!有維修!!!", "plain", "utf-8") #撰寫內文內容，以及指定格式為plain，語言為中文
    mime["Subject"]="網路組維修通知" #撰寫郵件標題
    mime["From"]="s10627046@gm.cyut.edu.tw" #撰寫你的暱稱或是信箱
    mime["To"]="trigger@applet.ifttt.com" #撰寫你要寄的人
    msg=mime.as_string() #將msg將text轉成str
    smtp=smtplib.SMTP("smtp.gmail.com", 587)  #googl的ping
    smtp.ehlo() #申請身分
    smtp.starttls() #加密文件，避免私密信息被截取
    smtp.login("s10627046@gm.cyut.edu.tw", "@Ian880831") 
    from_addr="s10627046@gm.cyut.edu.tw"
    to_addr=["trigger@applet.ifttt.com"]
    status=smtp.sendmail(from_addr, to_addr, msg)
if status=={}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
smtp.quit()

print(ans)
print("")
print("")

a = input("請輸入Enter來結束爬蟲")


# In[ ]:





# In[ ]:




