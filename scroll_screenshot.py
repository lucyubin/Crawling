# 스크롤 내려서 full 페이지 스크린 캡쳐

from time import sleep

# import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# https://stackoverflow.com/questions/59365968/opening-inspect-pressing-f12-on-chrome-via-selenium
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# create webdriver object
driver = webdriver.Chrome(executable_path=r'D:/논문/chromedriver.exe', options=options) #크롬드라이버.exe 위치

# get naver.com
driver.get("https://naver.com") #크롤링할 URL

# full size 
## https://www.youtube.com/watch?v=iOpGGW__oz4
## https://pythonbasics.org/selenium-screenshot/

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment

sleep(10)
driver.find_element_by_tag_name('body').screenshot('naver.png')

