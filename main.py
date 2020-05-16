#main.py
from selenium import webdriver
from time import sleep
from secrets import pw
from secrets import login

class InstaBot:
    def __init__(self, username, pw):
        print("init")
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(1.618)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        sleep(1.618)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        sleep(1.618)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
    def getUnfollowers(self):
        print("starting getUnfollowers")
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(2)
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), $sugges')

bot = InstaBot(login, pw)
bot.getUnfollowers()
