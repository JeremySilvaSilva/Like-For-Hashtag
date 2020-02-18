import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.remote.file_detector import UselessFileDetector


BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class InstagramBot():
    def __init__(self,email,password):
        options = webdriver.ChromeOptions()
        options.add_extension('/home/jeremyandress/Desktop/instagram.py/movil.crx')
        self.browser = webdriver.Chrome(BASE_PATH+'/chromedriver',chrome_options=options)
        self.email = email
        self.password = password
        self.sleep = random.randint(3,9)
    def signin(self):

        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(self.sleep)

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(self.sleep)

        notify = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]')
        notify.click()
        # image = self.browser.find_element_by_xpath('//*[@id="react-root"]/form/input')
        # image.send_keys('/home/jeremyandress/Pictures/paprika.jpg')

        nani = self.browser.file_detector = UselessFileDetector()
        print(nani)

        article = self.browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/section/div/div[1]/div/article[1]')
        print(article)




username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


insta = InstagramBot(username,password)
insta.signin()