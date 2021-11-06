from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.binary_location = "D:\Google\chrome\Application\chrome.exe"
chrome_driver_binary = "D:\Google\chrome\Application\chromedriver"
chrome_service = Service(executable_path=chrome_driver_binary)
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get('https://www.baidu.com')
time.sleep(3)
driver.quit()

# 获取请求链接
print(driver.current_url)

# 获取 cookies
print(driver.get_cookie())

# 获取源代码
print(driver.page_source)

# 获取文本的值
print(input.text)