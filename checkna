#!/usr/bin/python
print("               朝陽行政電腦設備維修爬蟲 v0.0.1 By:Pin-Yi-chuchu")
print("爬蟲中.")
print("爬蟲中.....")
print("爬蟲中.........")
print("爬蟲中.............")
print("爬蟲中..................")
print("爬蟲中...................................")
print("")


import requests
from bs4 import BeautifulSoup
response = requests.get('http://t2-5f-249.cyut.edu.tw/sys_rpi/auth.asp?txt_username=account&txt_passwd=password')
response.encoding = 'big5'
html = response.text
print("-----------------------------以下輸出訊息-----------------------------")
ans = html.find('網路組')
CRED = '\033[41m'  
CEND = '\033[0m'
GRED = '\033[42m'  
if ans == -1:
     ans = '[ 網路組 ] 目前沒有維修'
else:
     ans = '[ 網路組 ] 有維修!!!有維修!!!有維修!!!'
print(ans)
print("")
print("")

a = input("請輸入任意符號或字元來結束爬蟲:")
