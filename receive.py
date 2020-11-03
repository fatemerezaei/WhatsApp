from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from requests import get
import keyboard
import time
import click
import os
import sys
import csv
import threading
import time
# Replace below path with the absolute path 
# to chromedriver in your computer 
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
'''
  profile=webdriver.FirefoxProfile()
  browser = webdriver.Firefox(profile)

'''
#driver = webdriver.Firefox()
#profile=webdriver.FirefoxProfile()
driver = webdriver.Chrome('/home/fatemeh/Downloads/chromedriver') #webdriver.Firefox(profile) 
'''executor_url = driver.command_executor._url
session_id = driver.session_id

print (session_id)
print (executor_url)

driver.get("http://tarunlalwani.com")'''
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600) 

target = '"Jigar Tala"'
  
# Replace the below string with your own message 
string = "How are u?"
log = open('path.txt','w')
log.write("Body Time Type Size \n")
log.close()


x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
num = 48
text  ='d'

def repeatfun():
      global text
      global num
      global log
      threading.Timer(0.9, repeatfun).start()
      
      #url = driver.page_source
      #soup = bs(url, "lxml")
      #div = soup.find_all("div", { "class" : "FTBzM.message-in" })
      #div = driver.find_element_by_class_name('_1ays2')
      #x_path = '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input'
      #div = driver.find_element_by_xpath(x_path) 
      #div = soup.findAll("div", {"class": "-1wsdb"})

      path = "//*[@id='main']/div[3]/div/div/div[3]/div["+str(num)+"]/div/div/div/div[1]/div/span/span"
      path = "//*[@id='main']/div[3]/div/div/div[3]/div[last()]/div/div/div/div[1]/div/span/span"
      div = driver.find_elements(By.XPATH,path);
      if len(div)>0:
          if div[0].text!=text:
              text = div[0].text
              print(div[0].text,"New Messag received")
              log = open('path.txt','a')
              log.write(text +" "+str(time.time())+ "\n")
              log.close()
      else:

           path = '//*[@id="main"]/div[3]/div/div/div[3]/div[last()]/div/div[1]/div/div[1]/span[2]'#//*[@id="main"]/div[3]/div/div/div[3]/div[16]/div/div[1]/div/div[1]/span[2]
           div = driver.find_elements(By.XPATH,path);
           if len(div)>0:
              if div[0].text!=text:
                 text = div[0].text
                 print(div[0].text,"New Messag received")
                 log = open('path.txt','a')
                 log.write(text +" "+str(time.time())+ "\n")
                 log.close()
     

      

          
      
  
           
repeatfun()
#logger.close()

