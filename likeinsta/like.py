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
        options.add_extension(os.getcwd() +'/movil.crx')
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
        self.searchhashtag('instachile')
        self.hashtaglike(30)
        # self.like(0)

    def searchhashtag(self,hashtag):
        self.browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')


    def hashtaglike(self,num):
        from tqdm import tqdm
        count = 0
        time.sleep(self.sleep)
        script = '#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > a > div > div._9AhH0'
        self.browser.execute_script(f'document.querySelector("{script}").click()')
        pbar = tqdm(total = num)
        while num > count:
            try:
                time.sleep(random.randint(3,9))
                hearth = 'body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button'
                self.browser.execute_script(f'document.querySelector("{hearth}").click()')
                time.sleep(random.randint(3,12))
                next_page = 'body > div._2dDPU.vCf6V > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow'
                self.browser.execute_script(f'document.querySelector("{next_page}").click()')
                count += 1
                pbar.update(1)
            except:
                self.searchhashtag('instachile')
                time.sleep(random.randint(3,15))
                script = '#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > a > div > div._9AhH0'
                self.browser.execute_script(f'document.querySelector("{script}").click()')
        pbar.close()


    def like(self,num):
        count = num
        for likes in range(5):
            count += 1
            try:
                
                script = f'#react-root > section > main > section > div > div:nth-child(1) > div > article:nth-child({likes+1}) > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button'
                butt = "button.querySelector('svg[fill=\"#ed4956\"]');"  
                js = f'button = document.querySelector("{script}"); {butt}'
                if not self.browser.execute_script(js):
                    time.sleep(random.randint(1,3))
                    js = f'button = document.querySelector("{script}").click()'
                    self.browser.execute_script(js)
            except Exception as e:
                if count < 10:
                    print(f'Error : {e}')
                    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    self.like(count)
        if count < 10:
            print('--Vuelta--')
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.like(count)





username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


insta = InstagramBot(username,password)
insta.signin()