from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.blocking import BlockingScheduler
import requests

url = 'https://account.shodan.io/login'
values = {'username': 'user',
          'password': 'pass'}

r = requests.post(url, data=values)

def some_job():
    browser = webdriver.Chrome()
    keyword = 'keyword'
    browser.get('https://www.shodan.io/')
    elem = browser.find_element_by_id('search_input') 
    return elem.send_keys(keyword + Keys.RETURN)

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=1)
scheduler.start()

