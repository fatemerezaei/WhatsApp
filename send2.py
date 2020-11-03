from selenium import webdriver
import time
import pickle
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import os
import random
import numpy as np


max_IPD = 300 * 1000
min_IPD = 5 * 1000
shape = 0.93
n_ipds = 20000
samples = (np.random.pareto(shape, n_ipds) + 1) * min_IPD
ipds = [(max_IPD/1000 if x > max_IPD else math.ceil(x/1000))for x in samples]


def read_from_file(address):
    target = open(address, 'r')
    content = target.read()
    return content

file_address = 'ipd_messages.txt'
f = open(file_address, "r")
content = f.read().split("\n")
types = []
#ipds = []
for c in content:
    information = c.split(" ")
    try:
       # ipds.append(float(information[0]))
        types.append(information[1])
    except:
        pass

print(len(types),len(ipds))
driver = webdriver.Chrome('/home/fatemeh/whatsapp/chromedriver')  # webdriver.Firefox(profile)

driver.maximize_window()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
#cookies = pickle.load(open("cookies.pkl", "rb"))
#for cookie in cookies:
#    driver.add_cookie(cookie)
#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

target = '"Jigar Tala"'

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()


files = os.listdir('/home/fatemeh/data/texts/')
contents = []
for f in files:
    cnt = read_from_file('/home/fatemeh/data/texts/'+ f)
    #if "\xe2" in cnt:
    index = cnt.find('\xe2')
    #print(index, "FFFFFFFFF", f, cnt, "\n")
    contents.append(cnt[:index])
'''


raceback (most recent call last):
  File "send2.py", line 173, in <module>
    print("Error in sending" ,types[k], n, inst)     # arguments stored in .args
IndexError: list index out of range

'''
photos = os.listdir('/home/fatemeh/data/photo_pdf/')
videos = os.listdir('/home/fatemeh/data/video/')
audios = os.listdir('/home/fatemeh/data/audio/')
n = 0
file_n = str(time.time())
tar = open('/home/fatemeh/whatsapp/sep/africa/message_type_file_' + file_n + ".txt", 'w')
k = 9000#random.randint(0, len(types) - 10000 )
# stopped trukey at k = 18000
print("Starting with K:", k)
seen = set()
for i in range(len(ipds)):
    try:
	if types[k] == 'video':
	    print("video")#//*[@id="main"]/footer/div[1]/div[1]/div[2]/div
	    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div').click()

	    n = random.randint(0, len(videos) - 1 )
            while videos[n] in seen:
		n = random.randint(0, len(videos) - 1)

	    seen.add(videos[n])
            
	    driver.find_element_by_css_selector("input[type='file']").send_keys(
	        '/home/fatemeh/data/video/' + videos[n])

	    #time.sleep(5)#//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div
	    
	    wait =WebDriverWait(driver, 200)
	    clicker = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')))

	    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')))

	    driver.find_element_by_css_selector("span[data-icon='send']").click()

	    tar.write(types[k] + " " + videos[n] + " " + str(time.time())+ "\n")
	    #size = (os.path.getsize('/home/fatemeh/data/vids/' + videos[n]))/(10**6)
	    #time_to_wait = size/0.2# time to wait before sending another file, so the video is played fully.

	    #print(time_to_wait, "Wait for next video")
	    #time.sleep(time_to_wait)
	    time.sleep(30)
	elif types[k] in ['photo', 'image']:
#find_element_by_xpath
	    print("photo")
	    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div').click()
	    #n = n % len(photos)#
	    n = random.randint(0,len(photos) - 1 )

            while photos[n] in seen:
		n = random.randint(0, len(photos) - 1 )

	    seen.add(photos[n])

	    #driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/#li[3]').send_keys('/home/fatemeh/data/photo/' + photos[n])
	    driver.find_element_by_css_selector("input[type='file']").send_keys(
	        '/home/fatemeh/data/photo_pdf/' + photos[n])
	    #time.sleep(1)
	    clicker = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')))
	    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')))

	    driver.find_element_by_css_selector("span[data-icon='send']").click()
	    tar.write(types[k] + " " + photos[n] +" "+str(time.time())+"\n")

	    #time.sleep(30)

	elif types[k] =='audio':# or types[k]=='text':

	    print("audio")
	    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div').click()
	    #n = n % len(audios)#
	    n = random.randint(0, len(audios) - 1 )


            while audios[n] in seen:
		n = random.randint(0, len(audios) - 1 )

	    seen.add(audios[n])
	    #driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/#li[3]').send_keys('/home/fatemeh/data/photo/' + photos[n])
	    driver.find_element_by_css_selector("input[type='file']").send_keys(
	        '/home/fatemeh/data/audio/' + audios[n])
	    clicker = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')))
	    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')))
	    driver.find_element_by_css_selector("span[data-icon='send']").click()
	    tar.write(types[k] + " " + audios[n] +" "+str(time.time())+"\n")
	    #time.sleep(5)
	    #time.sleep(30)

	else:  # types[i] == 'text':
	    #print("############", len(contents[n]),type(contents[n]))
	    #n = n % len(contents)#
            print("Text")
	    n = random.randint(0, len(contents) - 1 )
	    input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')#'_3u328.copyable-text.selectable-text')
	    tar.write(types[k] + " " + str(len(contents[n])) +"\n")
	    input_box.send_keys(contents[n] + " "+str(time.time())+"\n")


	   # time.sleep(10)
	time.sleep(ipds[i])#ipds[i]
        k += 1

	#print(i, 5)
    except Exception as inst:
       #print(type(inst))    # the exception instance
       print("Error in sending" ,n, inst)     # arguments stored in .args
       k+=1
tar.close()
        # print(i,ipds[i])
