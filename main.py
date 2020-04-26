#main.py
from selenium import webdriver

class InstaBot:
    def __init__(self, username, pw):
        print("test")
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")

InstaBot()