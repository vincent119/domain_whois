# -*- coding: utf-8 -*-
#
# for windowns 
#
#
import os,sys
import re
import whois
import datetime
import time
import prettytable as pt

## -- main start ----
fileName = 'Domain_list.txt'
filePath = (os.path.dirname(os.path.abspath(__file__)))
file = filePath +'\\'+fileName
if not os.path.exists(file):
  print('找不到 Domain_list.txt....')
  print('請建立 Domain_list.txt,跟執行檔同一個目錄即可 ')
  os.system("pause")
  sys.exit()
  


tb1 = pt.PrettyTable()
tb1.field_names = ['域名', '到期時間']

with open(file,'r',encoding = 'UTF-8') as fs:
  domains = fs.readlines()
  domains = [x.rstrip('\n') for x in domains] 

for sname in domains:
  time.sleep(1)
  wd = whois.whois(sname)
  if wd:
    #print(wd)
    expDate = wd.expiration_date[1]
    tb1.add_row([sname,str(expDate.strftime('%Y-%m-%d'))])
    #print('| '+sname +' | '+str(expDate.strftime('%Y-%m-%d'))+'     | ' ) 
print(tb1)
os.system("pause")
