from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

b = input("bir şey aratmak istiyormusunuz: ")
if b == "e":
    a = str(input("Ne aramak istiyorsunuz: "))
else:
    pass



class Twitter:
    def __init__(self,username,password):
        self.browser= webdriver.Chrome()
        self.username = username
        self.password = password

    def sing(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameIN= self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
        passwordIN = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")

        usernameIN.send_keys(self.username)
        passwordIN.send_keys(self.password)

        btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div/div")
        btn.click()

        time.sleep(2)

    def search(self, hastag):
        self.browser.get("https://twitter.com/explore")
        time.sleep(3)
        searchin = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchin.send_keys(hastag)
        time.sleep(2)
        searchin.send_keys(Keys.ENTER)
        time.sleep(2)

twitter = Twitter(username,password)
twitter.sing()
twitter.search(a)