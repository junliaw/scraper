import requests
from bs4 import BeautifulSoup

reponse=requests.get('https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt')

soup=BeautifulSoup(reponse.text,'lxml')
titles=soup.findAll('a',{'class' :'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})

title_list=[]
for title in titles:
    title_list.append(title.getText())

tag_list=[]
urls=soup.find_all('a',{'class' :'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})
for url in urls:
    sub_response=requests.get(url.get('href'))
    sub_soup=BeautifulSoup(sub_response.text,'lxml')
    tags=sub_soup.find_all('li',{'class':'bbc-1ufuo2s e2o6ii40'})
    for tag in tags:
        tag_list.append(tag.getText())

print(tag_list)
