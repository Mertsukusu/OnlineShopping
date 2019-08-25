from selenium import webdriver
from pages.selectcourse_page import SelectCourse
import time
import unittest
from base.webdriverfactory import WebDriverFactory

class CourseTests(unittest.TestCase):
    def testingcourse(self):
        """TestCase TC001; Go to Let Kode it and login"""
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        ## Go to Login Page and Sign In Lets Kode it
        sc=SelectCourse(driver)
        sc.login("test@email.com","abcabc")

        currentpage = driver.current_url
        expectedpage= "https://learn.letskodeit.com/"

        if currentpage==expectedpage:
            print("TestCase TC001: Pass")
        else:
            print("TestCase TC001: Fail")

        """TestCase TC002; Click All Course Button"""

        ## Click All course button then go to all course page
        sc.allcourse()

        currentresult = driver.current_url
        expectedresult = "https://learn.letskodeit.com/courses"
        if currentresult == expectedresult:
            print("TestCase TC002: Pass")
        else:
            print("TestCase TC002: Fail")

        """TestCase TC003; Click Search button and write Python """
        ##Write Python to search button
        sc.searchbutton("python")

        element = driver.find_element_by_xpath("//input[@id='search-courses']")
        if element.is_enabled():
            print("TestCase TC003: Pass")
        else:
            print("TestCase Tc003: Fail")

        """TestCase TC004; Click Category Button and select Software Testing """

        sc.categoryall()
        sc.softwaretesting()

        currentresult = driver.current_url
        expectedresult = "https://learn.letskodeit.com/courses/category/Software%20Testing"
        if currentresult == expectedresult:
            print("TestCase TC004: Pass")
        else:
            print("TestCase TC004: Fail")

        """TestCase TC005; Click Author Button and select Let's kode it button """

        sc.author_all()
        sc.letskodeitbutton()

        element = driver.find_element_by_xpath("//div[contains(text(),'Author:')]")
        if element.is_enabled():
            print("TestCase TC005: Pass")
        else:
            print("TestCase TC005: Fail")

        """TestCase TC006; Click Selenium WebDriver With Python 3 Course and go to next page"""

        ##Click Selenium Webdriver with Python Course button
        sc.seleniumpythoncourse()

        ##Check expected result
        currentresult = driver.current_url
        expectedresult = "https://learn.letskodeit.com/p/selenium-webdriver-with-python3"

        if currentresult == expectedresult:
            print("TestCase TC006: Pass")
        else:
            print("TestCase TC006: Fail")

        """TestCase TC007; Click Watch Promo Video"""

        sc.watchpromo()

        element = driver.find_element_by_xpath("//button[@class='close']")
        if element.is_enabled():
            print("TestCase TC007: Pass")
        else:
            print("TestCase TC007: Fail")


        """TestCase TC008; Close Promo video """
        ##Close promo video
        sc.closepromovideo()

        element = driver.find_element_by_xpath("//a[@id='watchpromo']")

        if element.is_enabled():
            print("TestCase TC008: Pass")
        else:
            print("TestCase TC008: Fail")

        """TestCase TC009; Click Enroll course button and go to payment page"""

        ## Click Enroll in Course Button
        sc.enrollcourse()

        ##Check expected result
        currentresult = driver.current_url
        expectedresult = "https://sso.teachable.com/secure/42299/checkout/342638/selenium-webdriver-with-python3"

        if currentresult == expectedresult:
            print("TestCase TC009: Pass")
        else:
            print("TestCase TC009: Fail")





cc=CourseTests()
cc.testingcourse()