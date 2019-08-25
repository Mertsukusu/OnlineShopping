from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import time
import utilities

class LoginPage(SeleniumDriver):
    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver

    #locators
    _login_tab="//a[@class='navbar-link fedora-navbar-link']"
    _email_tab="#user_email"
    _password_tab=" #user_password"
    _logIn_button="//input[@name='commit']"

    #action
    def clicklogin(self):
        return self.elementClick(self._login_tab, locatorType="xpath")
    def sendkeysemail(self, _email_tab):
        return self.sendKeys(_email_tab,self._email_tab, locatorType="css")
    def sendkeyspassword(self,_password_tab):
        return self.sendKeys(_password_tab,self._password_tab,locatorType="css")
    def clicklogInbutton(self):
        return self.elementClick(self._logIn_button, locatorType="xpath")

    def login(self,email,password):
        self.clicklogin()
        time.sleep(2)

        self.sendkeysemail(email)
        time.sleep(2)

        self.sendkeyspassword(password)
        time.sleep(2)

        self.clicklogInbutton()
        time.sleep(2)



