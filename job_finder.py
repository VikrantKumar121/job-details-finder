# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import pandas as pd
from selenium.webdriver.common.keys import Keys

xpath = {
    
    'job_search':'//*[@id="hs-qsb"]',
    'jobs1':'//*[@class="BjJfJf gsrt cPd5d"]'

}
category = input()
browser = webdriver.Chrome(executable_path=r"D:\chromedriver.exe")
browser.get('https://www.google.com/search?q='+ category +'&rlz=1C1CHBF_enIN862IN862&oq=jobs&aqs=chrome..69i57j0l2j69i60l2j69i61.2143j0j7&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwjQ7InqtO_lAhWJA3IKHTD4BXkQiYsCKAB6BAgJEAM#htivrt=jobs&htidocid=2tTPIs9CZPT6qs9bAAAAAA%3D%3D&fpstate=tldetail')
a = browser.find_element_by_xpath('//div[@class="SBFvB"]')
print(a.text)