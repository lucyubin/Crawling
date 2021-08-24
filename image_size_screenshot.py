# �̹��� ũ�� �����ؼ� ĸ��

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
driver = webdriver.Chrome(executable_path=r'D:/��/chromedriver.exe', options=options) #ũ�ҵ���̹�.exe ��ġ

# get naver.com
driver.get("https://map.kakao.com/?map_type=TYPE_MAP&traffic_state=2&urlLevel=4&urlX=507000&urlY=1130000") #ũ�Ѹ��� URL

#set to new window size
driver.set_window_size(3000, 3000) # ĸ���� �̹��� ���� ���� ũ��
sleep(10) # ���� �ε��� �ð�

#obtain screenshot of page within body tag
driver.find_element_by_tag_name('body').screenshot("kakaomap.png")
