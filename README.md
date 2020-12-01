# Python-Line Bot 系統爬蟲提醒(windows)
## 可自動登入帳號密碼，並撈取需登入後才可獲得資料，爬蟲後分析並用Line Bot提醒

**參考資料來源**
* python 套件介紹 https://reurl.cc/8naykR *
* Jupyter 套件介紹 https://reurl.cc/Gr6bXv *

**以下目錄**
* 安裝pytohn
* 安裝Jupyter
  * 執行腳本(3台虛擬機)
  * 初始化設定(master)

# 安裝pytohn

**1. 到python首頁下載最新版本python執行檔，並完成安裝。**
```
https://www.python.org/
```
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/1.png)

**2. 開啟cmd執行指令是否安裝成功(執行查詢版本)。**
```
python ––version
```
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/2.PNG)

# 安裝Jupyter

**1. 使用Python程式語言的套件管理程式pip來做安裝(由於是版本3所以使用pip3)。**
```
pip3 install jupyter    
```
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/3.PNG)

**2. 啟動Jupyter網頁服務。**
```
jupyter notebook  
```
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/4.PNG)
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/5.PNG)

**3. 選取New，選python3，開啟新的編輯頁面。**

![image](https://github.com/880831ian/Python-LineBot/blob/main/images/6.png)
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/7.PNG)

# 爬蟲撰寫

**1. 輸入腳本標頭檔以及函式庫。**
```
#!/usr/bin/env python
# coding: utf-8

import requests
import datetime
import smtplib 
```
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/8.PNG)

**2. response get 該網址的帳號密碼頁面，以及需要收尋的關鍵字。**
```
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
```
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/9.PNG)

**3. 用if else 來判斷是否收尋成功。**
```
if ans == -1:
    ans = '沒有收尋到關鍵字回應內容'
else:
    ans = '有收尋到關鍵字回應內容'
```
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/10.PNG)

**4. 加入若收尋成功執行寄信(這邊寄信給ifttt來觸發Line Bot提醒)。**
```
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
```
![image](https://github.com/880831ian/Python-LineBot/blob/main/images/11.PNG)

**5. 附上整段程式碼**
```
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
```

**6. Line Bot通知畫面。**

![image](https://github.com/880831ian/Python-LineBot/blob/main/images/12.PNG)

