from selenium import webdriver
import time

browser=webdriver.Chrome("C:\chromedriver.exe")#find path of chromedriver
browser.get("https://www.instagram.com/")#the site you want to use on
time.sleep(3)#wait 3 sec

#Login
Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")#username input xpath
Username.send_keys("username put here")#write your username inside input
time.sleep(3)#wait 3 sec
Password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")#password input xpath
Password.send_keys("password inside here")#write your password inside input
Password.submit()
time.sleep(3)#wait 3 sec

#NotNow
Notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")#find not now notifiction
Notnow.click()#click on it
time.sleep(4)#wait 4 sec
#Turnoff
Turnoff=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")#turn off notificion
Turnoff.click()#click on turn off
time.sleep(2)#wait 3 sec

for i in range(99999):#99999 you can change it to how much time you want it redo this process
    for i in range(5):
        browser.find_element_by_xpath('//button[text()="Follow"]')\
                                                                    .click()#gg wp if u didnt relize whats that
        time.sleep(1)#wait 1
    browser.refresh()#refreshing the page
    
        
