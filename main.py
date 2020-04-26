#main.py
from selenium import webdriver
from time import sleep
from secrets import pw

class InstaBot:
    def __init__(self, username, pw):
        print("test")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(999)

InstaBot("ptflp", pw)
