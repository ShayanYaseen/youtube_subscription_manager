import wget
import webbrowser
import os.path
from os import path
import time
import pathlib

def replace_line(file_name, line_num, text,txt,fold):
    lines = open('template.js', 'r').readlines()
    open(file_name, 'w').close()
    out = open(file_name, 'w')
    out.writelines(text)
    out.writelines(txt)
    out.writelines(fold)
    out.writelines(lines)
    out.close()


print('Beginning subscription file download')
url = 'https://www.youtube.com/subscription_manager?action_takeout=1'
webbrowser.open(url, new=2)
print('Download xml file and place under directory')
while (not(path.exists("subscription_manager"))):
    print("Waiting...")
    time.sleep(1)
print("File downloaded")

has = dict()
flag2 = 0
tmp = ""
with open('subscription_manager', 'r') as file:
    for line in file:
        for word in line.split():
            if flag2:
                tmp += word
                if word[-1] == '"':
                    flag2 = 0
            if word[0:5] == 'title':
                tmp = word[6:]
                flag2 = 1
            elif word[0:6] == "xmlUrl":
                y = 1
                for x in tmp:
                    if tmp[y] == '"':
                        break
                    y = y+1
                tmp = tmp[1:y]
                has[tmp] = "https://www.youtube.com/channel/"+word[60:-1]
                flag2 = 0
no_of_categories = int(input("How many categories do you want ?\n"))
fold = dict()
print("Enter all the category names")
for x in range(0,no_of_categories):
    name_cat = input("Enter Category Name :\n")
    fold[x+1] = name_cat

mapped = dict()
list_of_book = list()
for keys, values in has.items():
    print(fold)
    print("______________________________")
    print(keys,values)
    colmn = int(input("Enter Category Number from 1 to n\n"))
    mapped[keys]=colmn
    print("______________________________")


f1 = 0
tmp_sr =''
tmp_sl =''
for key,value in sorted(mapped.items(), key=lambda item: item[1]):
    if value == f1:
        tmp_sl += (key+"\n")
        tmp_sr += has[key]+"\n"

    else:
        f1 = value
        if tmp_sl!="":
            replace_line('scripts.js', 0, 'var name = `'+tmp_sl + '`;\n',
                         'var url = `'+tmp_sr+'`;\n', 'var folder = `'+fold[value-1]+ '`;\n')
            curr_direct = str(pathlib.Path(__file__).parent.absolute())
            webbrowser.open('file://' + curr_direct + "/index.html")
            tmp5 = 0
            while tmp5!=1:
                tmp5 = int(input("Download the bookmark for this category then press 1\n"))
        tmp_sl = key+"\n"
        tmp_sr = has[key]+"\n"


replace_line('scripts.js', 0, 'var name = `'+tmp_sl + '"`;\n',
             'var url = `'+tmp_sr+'`;\n', 'var folder = `'+fold[no_of_categories] + '`;\n')
curr_direct = str(pathlib.Path(__file__).parent.absolute())
webbrowser.open('file://' + curr_direct + "/index.html")
