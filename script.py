from selenium import webdriver
import time

browser=webdriver.Chrome("C:\chromedriver.exe")#find path of chromedriver
browser.get("https://discord.com/")#the site you want to use on
time.sleep(1)#wait 1 sec
username1 = input("enter username : ")

time.sleep(10)
#Login
Username=browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div[2]/button")
time.sleep(1)
Username.click()
time.sleep(1)

Username1=browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div[2]/form/input")
Username1.send_keys(username1)#write your username inside input
time.sleep(2)
Username2=browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div[2]/form/button/img")
Username2.click()
time.sleep(3)
Username3=browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]")
Username3.click()

















#Password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")#password input xpath
#Password.send_keys("orel8520@")#write your password inside input
#Password.submit()
#time.sleep(1)#wait 1 sec


#NotNow
#Notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")#find not now notifiction
#Notnow.click()#click on it
#time.sleep(1)#wait 1 sec
