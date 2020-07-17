from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

a = input("Ne aratmak istiyorsun: ")

driver = webdriver.Chrome()

url = "http://google.com"
driver.get(url)
driver.maximize_window()

searchinput = driver.find_element_by_name("q")
searchinput.send_keys(a)
searchinput.send_keys(Keys.ENTER)




result = driver.page_source
print(result)
