import requests
from bs4 import BeautifulSoup

reponse=requests.get('https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt')

soup=BeautifulSoup(reponse.text,'lxml')
titles=soup.findAll('a',{'class' :'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})

title_list=[]
for title in titles:
    title_list.append(title.getText())

print(title_list)