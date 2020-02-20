import os
from like import InstagramBot, get_credential

username, password = get_credential()


insta = InstagramBot(username,password)
insta.signin()
insta.searchhashtag('instachile')
insta.click_first_image()
insta.next_page()
if insta.get_time(600):
    insta.click_hearth()