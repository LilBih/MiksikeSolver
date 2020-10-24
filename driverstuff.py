from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import wx

app = wx.App(False)
width, height = wx.GetDisplaySize()

options = Options()
options.headless = False

base_url = 'https://miksike.net.ua/#pranglimine/training'
user_name = ''
password = ''

driver = webdriver.Chrome(
    executable_path='chromedriver.exe',
    options=options
)
driver.set_window_size(0.5 * width, 0.5 * height)


def isSprint():
    if 'sprint=1' in driver.current_url:
        return True
    return False
