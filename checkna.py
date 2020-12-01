#!/usr/bin/env python
# coding: utf-8
print("               電腦設備維修爬蟲 v0.0.2 By:Pin-Yi-chuchu")
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
response = requests.get('http://馬賽克.cyut.edu.tw/sys_rpi/auth.asp?username=帳號&passwd=密碼')
response.encoding = 'big5'
html = response.text
print("-----------------------------以下輸出訊息-----------------------------")
ans = html.find('收尋關鍵字')
print(theTime)
if ans == -1:
    ans = '沒有收尋到關鍵字回應內容'
else:
    ans = '有收尋到關鍵字回應內容' #寄信到ifttt達成line bot提醒服務
    mime=MIMEText("信件內容", "plain", "utf-8") #撰寫內文內容，以及指定格式為plain，語言為中文
    mime["Subject"]="標題" #撰寫郵件標題
    mime["From"]="Xxxxxxx@gmail.com" #撰寫你的暱稱或是信箱
    mime["To"]="trigger@applet.ifttt.com" #撰寫你要寄的人
    msg=mime.as_string() #將msg將text轉成str
    smtp=smtplib.SMTP("smtp.gmail.com", 587)  #googl的ping
    smtp.ehlo() #申請身分
    smtp.starttls() #加密文件，避免私密信息被截取
    smtp.login("帳號", "密碼") 
    from_addr="帳號"
    to_addr=["trigger@applet.ifttt.com"]
    status=smtp.sendmail(from_addr, to_addr, msg)
if status=={}:
    print("郵件傳送成功!") #顯示是否成功
else:
    print("郵件傳送失敗!")
smtp.quit()
print(ans)
print("")
print("")
a = input("請輸入Enter來結束爬蟲")
