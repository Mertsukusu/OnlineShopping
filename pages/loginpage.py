from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ###Locator###
    _getaccount = "//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')]"
    _Signinbutton = "/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[2]/ul[1]/li[1]/ul[1]/li[2]/a[1]"
    _Firstname ="//input[@placeholder='First Name']"
    _Lastname = "//input[@placeholder='Last Name']"
    _Phonenumber = "//input[@placeholder='Mobile Number']"
    _getusername = "//input[@placeholder='Email']"
    _getpassword = "//input[@placeholder='Password']"
    _ConfirmPassword ="//input[@placeholder='Confirm Password']"
    _SubmitButton = "//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']"


    def getaccount(self):
        return self.driver.find_element_by_xpath(self._getaccount)
    def getsigninbutton(self):
        return self.driver.find_element_by_xpath(self._Signinbutton)
    def getfirstname(self):
        return self.driver.find_element_by_xpath(self._Firstname)
    def getlastname(self):
        return self.driver.find_element_by_xpath(self._Lastname)
    def getphonenumber(self):
        return self.driver.find_element_by_xpath(self._Phonenumber)
    def getusername(self):
        return self.driver.find_element_by_xpath(self._getusername)
    def getpassword(self):
        return self.driver.find_element_by_xpath(self._getpassword)
    def getconfirmpassword(self):
        return self.driver.find_element_by_xpath(self._ConfirmPassword)
    def getsubmitbutton(self):
        return self.driver.find_element_by_xpath(self._SubmitButton)


    def clickaccount(self):
        return self.getaccount().click()
    def clicksignin(self):
        return self.getsigninbutton().click()
    def enterfirstname(self,firstname):
        return self.getfirstname().send_keys(firstname)
    def enterlastname(self,lastname):
        return self.getlastname().send_keys(lastname)
    def enterphonenumber(self,phonenumber):
        return self.getphonenumber().send_keys(phonenumber)
    def enterusername(self,username):
        return self.getusername().send_keys(username)
    def enterpassword(self,password):
        return self.getpassword().send_keys(password)
    def enterconfirmpassword(self,confirmpassword):
        return self.getconfirmpassword().send_keys(confirmpassword)
    def clicksubmitbutton(self):
        return self.getsubmitbutton().click()
    def scrolldown(self):
        return self.driver.execute_script("window.scrollBy(0,500);")


    def signup(self,firstname,lastname,phonenumber,username,password,confirmpassword):
        # self.getaccount()
        self.clickaccount()

        # self.getsigninbutton()
        self.clicksignin()

        # self.getfirstname()
        self.enterfirstname(firstname)

        # self.getlastname()
        self.enterlastname(lastname)

        # self.getphonenumber()
        self.enterphonenumber(phonenumber)

        # self.getusername()
        self.enterusername(username)

        self.getpassword()
        self.enterpassword(password)

        self.getconfirmpassword()
        self.enterconfirmpassword(confirmpassword)

        self.getsubmitbutton()
        self.clicksubmitbutton()

        self.scrolldown()
