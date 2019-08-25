from selenium import webdriver
from pages.loginpage import LoginPage
import time
import unittest
from base.webdriverfactory import WebDriverFactory

class Logintest(unittest.TestCase):
    def test001(self):

        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        """Enter valid user name and valid password then click login button"""
        lp=LoginPage(driver)
        lp.login("azimedalkilinc@gmail.com","mert1991")

        expectedUrl = "https://learn.letskodeit.com/"
        actualUrl = driver.current_url
        if expectedUrl == actualUrl:
            print("Test case TC001: Pass")
        else:
            print("Test case TC001: Fail")

    def test002(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        """Enter invalid user name and valid password then click login button"""
        lp=LoginPage(driver)
        lp.login("azime@gmail.com","mert1991")

        if driver.find_element_by_xpath("//div[@class='alert alert-danger']").text=="Invalid email or password.":
            print("Test case TC002: Pass")
        else:
            print("Test case TC002: Fail")

    def test003(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        """Enter valid user name and invalid password then click login button"""
        lp = LoginPage(driver)
        lp.login("azimedalkilinc@gmail.com", "mert1234")

        if driver.find_element_by_xpath("//div[@class='alert alert-danger']").text=="Invalid email or password.":
            print("Test case TC003: Pass")
        else:
            print("Test case TC003: Fail")

    def test004(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        """Enter valid password and click login button"""
        lp = LoginPage(driver)
        lp.login("", "mert1991")

        if driver.find_element_by_xpath("//div[@class='alert alert-danger']").text == "Invalid email or password.":
            print("Test case TC004: Pass")
        else:
            print("Test case TC004: Fail")

    def test005(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        """Enter valid user name and click login button"""
        lp = LoginPage(driver)
        lp.login("azime@gmail.com", "")

        if driver.find_element_by_xpath("//div[@class='alert alert-danger']").text == "Invalid email or password.":
            print("Test case TC005: Pass")
        else:
            print("Test case TC005: Fail")

        driver.close()
        driver.quit()





