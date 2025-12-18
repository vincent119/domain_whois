# -*- coding: utf-8 -*-
#
# for windowns
#
#
import datetime
import os
import re
import sys
import time

import prettytable as pt
import whois
from progressbar import ETA, Bar, Percentage, ProgressBar, Timer


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":"yes",   "y":"yes",  "ye":"yes",
             "no":"no",     "n":"no"}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while 1:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")

def save_file(object):
  tb1 = object
  datapath = 'c:\domin_temp\\'
  filename = (time.strftime("%Y-%m-%d-%H%M%S", time.localtime()))+'.domain_query.txt'
  if not os.path.exists(datapath):
    os.makedirs(datapath)
  pfile = datapath + filename
  #file = open(pfile, 'w', encoding = 'UTF-8')
  with open(pfile,'w') as file:
    file.write(str(tb1))
  print('已經儲存到 '+filename)
  os.system("pause")

widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),
      ' ', ETA(), ' ']


## -- main start ----
fileName = 'Domain_list.txt'
filePath = (os.path.dirname(os.path.abspath(__file__)))
file = filePath +'\\'+fileName

if not os.path.exists(file):
  print('找不到 Domain_list.txt....')
  print('請建立 Domain_list.txt,跟執行檔同一個目錄即可 ')
  os.system("pause")
  sys.exit()


total = 1000
tb1 = pt.PrettyTable()
tb1.field_names = ['域名', '到期時間']


with open(file,'r',encoding = 'UTF-8') as fs:
  domains = fs.readlines()
  domains = [x.rstrip('\n') for x in domains]

i = 1
pbar = ProgressBar(widgets=widgets, maxval=10*total).start()
for sname in domains:
  pbar.update(100 * i + 1)
  i = i + 10
  time.sleep(1)
  wd = whois.whois(sname)
  if  wd:
    if isinstance(wd.expiration_date,list):
      expDate = wd.expiration_date[1]
      tb1.add_row([sname,str(expDate.strftime('%Y-%m-%d'))])
    else:
      tb1.add_row([sname,(wd.expiration_date).strftime('%Y-%m-%d')])

pbar.finish()
print(tb1)
if query_yes_no('是否要儲存到檔案','no'):
  save_file(tb1)



#os.system("pause")
