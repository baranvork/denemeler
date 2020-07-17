from selenium import webdriver
a = input("nereye gitmek istiyorsun: ")
driver = webdriver.Chrome()
url = ("http://"+ a + ".com")

driver.get(url)
driver.maximize_window()
