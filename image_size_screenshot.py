# 이미지 크기 지정해서 캡쳐

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
driver.get("https://map.kakao.com/?map_type=TYPE_MAP&traffic_state=2&urlLevel=4&urlX=507000&urlY=1130000") #크롤링할 URL

#set to new window size
driver.set_window_size(3000, 3000) # 캡쳐할 이미지 가로 세로 크기
sleep(10) # 지도 로딩할 시간

#obtain screenshot of page within body tag
driver.find_element_by_tag_name('body').screenshot("kakaomap.png")
