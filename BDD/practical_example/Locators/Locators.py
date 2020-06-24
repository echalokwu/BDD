from selenium import webdriver


class Locators:

    def __init__(self, driver):
        self.driver = driver
        self.url = "www.python.com"

    def go_to_url(self, url):
        self.driver.get(self.url)
