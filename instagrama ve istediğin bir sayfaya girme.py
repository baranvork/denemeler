from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

a = input("bir siteye girmek içinmi geldiniz: ")

if a == "e" :
    b = str(input("hangi siteye gitmek istiyorsunuz: "))
else:
    pass

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password



    def singIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)


        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def get(self, username):
        self.browser.get("https://www.instagram.com/"+username)





instagram = Instagram(username,password)
instagram.singIn()
instagram.get(b)


