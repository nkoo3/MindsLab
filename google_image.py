import sys, os
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib, urllib.request
import requests
import random
import time
from selenium.webdriver.common.keys import Keys

###initial set

url = "https://www.google.com/search"
searchItem = "dog"
size = 300

params ={
   "q":searchItem
   ,"tbm":"isch"
   ,"sa":"1"
   ,"source":"lnms&tbm=isch"
}

#Type in the URL

url = url+"?"+urllib.parse.urlencode(params)
driver = webdriver.Chrome()
time.sleep(0.5)
driver.get(url)
html = driver.page_source
time.sleep(0.5)

#Get number of images for a page

soup_temp = BeautifulSoup(html,'html.parser')
img4page = len(soup_temp.findAll("img"))

#Scroll the page down 

elem = driver.find_element_by_tag_name("body")
imgCnt =0
while imgCnt < size*10:
    elem.send_keys(Keys.PAGE_DOWN)
    rnd = random.random()
    print(imgCnt)
    time.sleep(rnd)
    imgCnt+=img4page

#Find all the images

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
img = soup.findAll("img")

driver.find_elements_by_tag_name('img')

fileNum=0
srcURL=[]

for line in img:
   if str(line).find('data-src') != -1 and str(line).find('http')<100:  
      print(fileNum, " : ", line['data-src'])  
      srcURL.append(line['data-src'])
      fileNum+=1
      
#Create directory and save images there

dir_path ='./img/' 
dir_name = searchItem
directory = dir_name + dir_path
parent_dir = "/Users/nancykoo/Desktop/ImageScraper"
path = os.path.join(parent_dir, directory) 
os.mkdir(path) 
print("Directory '%s' created" %directory) 

n=1
for i in img :  
  imgUrl = i['data-src'] 
  with urlopen(imgUrl) as f: 
      with open(path + dir_name + str(n) + '.jpg', 'wb') as h:  
          img = f.read() 
          h.write(img) 
      n += 1 
      print(imgUrl)          
print('Download complete') 
