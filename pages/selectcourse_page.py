from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import time
import utilities

class SelectCourse(SeleniumDriver):
    def _init_(self, driver):
        super()._init_(driver)
        self.driver = driver

    ###Locators###
    _login_tab = "//a[@class='navbar-link fedora-navbar-link']"
    _email_tab = "#user_email"
    _password_tab = " #user_password"
    _logIn_button = "//input[@name='commit']"
    _allCourse_button = "//a[contains(text(),'All Courses')]"
    _searchButton = "//input[@id='search-courses']"
    _category_all = "//div[@class='row search']//div[1]//div[2]//button[1]"
    _softwaretesting_button = "//a[contains(text(),'Software Testing (5)')]"
    _author_all = "//button[contains(text(),'All')]"
    _letkodeit_button= "//a[@href='/courses/author/154569']"
    _selenium_pythoncourse_button="//div[contains(text(),'Selenium WebDriver With Python 3.x')]"
    _watch_promo = "//a[@id='watchpromo']"
    _play_promo_video = "//img[@class='w-css-reset']"
    _close_promo_video = "//button[@class='close']"
    _enroll_in_course = "//button[@id='enroll-button-top']"

    def clicklogin(self):
        return self.elementClick(self._login_tab, locatorType="xpath")
    def sendkeysemail(self, _email_tab):
        return self.sendKeys(_email_tab,self._email_tab, locatorType="css")
    def sendkeyspassword(self,_password_tab):
        return self.sendKeys(_password_tab,self._password_tab,locatorType="css")
    def clickloginbutton(self):
        return self.elementClick(self._logIn_button, locatorType="xpath")
    def click_all_coursebutton(self):
        return self.elementClick(self._allCourse_button,locatorType="xpath")
    def sendkeysearchbutton(self,_searchButton):
        return self.sendKeys(_searchButton,self._searchButton,locatorType="xpath")
    def click_category_all(self):
        return self.elementClick(self._category_all,locatorType="xpath")
    def select_softwaretesting(self):
        return self.elementClick(self._softwaretesting_button,locatorType="xpath")
    def click_authorall(self):
        return self.elementClick(self._author_all,locatorType="xpath")
    def click_letskodeit_button(self):
        return self.elementClick(self._letkodeit_button,locatorType="xpath")
    def click_selenium_python_course(self):
        return self.elementClick(self._selenium_pythoncourse_button,locatorType="xpath")
    def click_watch_promo(self):
        return self.elementClick(self._watch_promo,locatorType="xpath")
    def click_playwatchpromovideo(self):
        return self.elementClick(self._play_promo_video,locatorType="xpath")
    def click_closepromovideo(self):
        return self.elementClick(self._close_promo_video,locatorType="xpath")
    def click_enrollcouse(self):
        return self.elementClick(self._enroll_in_course,locatorType="xpath")

    """ Login Part  """
    def login(self,email,password):
        ##Click Login
        self.clicklogin()
        time.sleep(2)
        ## Enter mail address
        self.sendkeysemail(email)
        time.sleep(2)
        ## Enter Password
        self.sendkeyspassword(password)
        time.sleep(2)
        ## Click login button
        self.clickloginbutton()
        time.sleep(2)

    """Click All courses button"""
    def allcourse(self):
        self.click_all_coursebutton()
        time.sleep(2)
    """Writting Python to search button"""
    def searchbutton(self,coursename):
        self.sendkeysearchbutton(coursename)
        time.sleep(2)
    """Click CategoryAll button"""
    def categoryall(self):
        self.click_category_all()
        time.sleep(2)
    def softwaretesting(self):
        self.select_softwaretesting()
        time.sleep(2)
    def author_all(self):
        self.click_authorall()
        time.sleep(2)
    def letskodeitbutton(self):
        self.click_letskodeit_button()
        time.sleep(2)
    def seleniumpythoncourse(self):
        self.click_selenium_python_course()
        time.sleep(2)
    def watchpromo(self):
        self.click_watch_promo()
        time.sleep(2)
    def playpromovideo(self):
        self.click_playwatchpromovideo()
        time.sleep(2)
    def closepromovideo(self):
        self.click_closepromovideo()
        time.sleep(2)
    def enrollcourse(self):
        self.click_enrollcouse()
        time.sleep(2)