from selenium import webdriver
import time
from pages.loginpage import LoginPage
# import unittest

class Tc001():
    def test1(self):
        """Enter Valid mail address and password"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)


        sgn = LoginPage(driver)
        sgn.signup("Anderson","Talisca","1234567890","asd@hotmail.com","ASdf1234","ASdf1234",)

        expectedmessage = "Email Already Exists."

        warningmessage = driver.find_element_by_xpath("//div[@class='alert alert-danger']").text


        print(warningmessage)
        if expectedmessage == warningmessage:
            print("Testcase Tc001 is Passed.")
        else:
            print("Testcase Tc001 is failed.")

        print("Complete Sign In. Thank you Andersonnn..")


class Tc002():
    def test2(self):
        """Leave to empty Username"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)


        sgn = LoginPage(driver)
        sgn.signup("Anderson","Talisca","1234567890","","ASdf1234","ASdf1234",)
        sgn.scrolldown()

        expectedmessage = "The Email field is required."
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'The Email field is required.')]").text

        print(warningmessage)

        if expectedmessage != warningmessage:
            print("Testcase Tc002 is failed.")
        elif expectedmessage == warningmessage:
            print("Testcase Tc002 is Passed.")
        else:
            print("Unexpected Error..")

class Tc003():
    def test3(self):
        """Leave to empty Password"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        sgn = LoginPage(driver)
        sgn.signup("Anderson","Talisca","1234567890","asd@hotmail.com","","ASdf1234",)

        # User will see warning message
        expectedmessage = "The Password field is required."
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'The Password field is required.')]").text

        print(warningmessage)

        if expectedmessage == warningmessage:
            print("Testcase Tc003 is Passed.")
        elif expectedmessage != warningmessage:
            print("Testcase Tc003 is failed.")
        else:
            print("Unexpected Error..")

class Tc004():
    def test4(self):
        """Password between 1-5 characters"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)


        sgn = LoginPage(driver)
        sgn.signup("Anderson","Talisca","1234567890","asd@hotmail.com","asd","asd",)

        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'The Password field must be at least 6 characters in length.')]").text

        expectedmessage = "The Password field must be at least 6 characters in length."

        if expectedmessage == warningmessage:
            print("Testcase Tc004 is Passed.")
        elif expectedmessage != warningmessage:
            print("Testcase Tc004 is failed.")
        else:
            print("Unexpected Error..")

class Tc005():
    def test5(self):
        """Enter Valid mail address and password"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)


        sgn = LoginPage(driver)
        sgn.signup("Anderson","Talisca","1234567890","asd@hotmail.com","ASDF1234","ASDF1234",)

        expectedmessage = "Email Already Exists."

        warningmessage = driver.find_element_by_xpath("//div[@class='alert alert-danger']").text
        print(warningmessage)

        if expectedmessage == warningmessage:
            print("Testcase Tc005 is Passed.")
        else:
            print("Testcase Tc005 is failed.")

class Tc006():
    def test6(self):
        """"Password contains at 8 letters characters"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)


        sgn = LoginPage(driver)
        sgn.signup("Anderson","Talisca","1234567890","asd@hotmail.com","ASDF1234","ASDF1234",)

        actualresults = driver.find_element_by_xpath("//div[contains(text(),' Email Already Exists. ')]").text
        expectedresults = " Password should be contain at least two digits "

        if actualresults == expectedresults:
            print("Testcase Tc006 is Passed.")
        elif actualresults != expectedresults:
            print("Testcase Tc006 is failed.")
        else:
            print("Testcase Tc006, Unexpected Error..")

class Tc007():
    def test7(self):
        """Try a once-used email address and username"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)


        sgn = LoginPage(driver)
        sgn.signup("Anderson","Talisca","1234567890","asd@hotmail.com","ASdf1234","ASdf1234",)

        expectedmessage = "Email Already Exists."

        warningmessage = driver.find_element_by_xpath("//div[@class='alert alert-danger']").text


        print(warningmessage)
        if expectedmessage == warningmessage:
            print("Testcase Tc007 is Passed.")
        else:
            print("Testcase Tc007 is failed.")

class Tc008():
    def test8(self):
        """Leave to empty Confirm Password"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        sgn = LoginPage(driver)
        sgn.signup("Anderson","Talisca","1234567890","asd@hotmail.com","ASdf1234","",)

        # User will see warning message
        expectedmessage = "The Password field is required."
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'The Password field is required.')]").text

        print(warningmessage)

        if expectedmessage == warningmessage:
            print("Testcase Tc008 is Passed.")
        elif expectedmessage != warningmessage:
            print("Testcase Tc008 is failed.")
        else:
            print("Unexpected Error..")

class Tc009():
    def test9(self):
        """Enter different Confirm Password"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        sgn = LoginPage(driver)
        sgn.signup("Anderson","Talisca","1234567890","asd@hotmail.com","ASdf1234","ASdfas12",)

        # User will see warning message
        expectedmessage = "Password not matching with confirm password."
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'Password not matching with confirm password.')]").text

        print(warningmessage)

        if expectedmessage == warningmessage:
            print("As expected Warning message is : ", expectedmessage, "Testcase Tc009 is passed. ")
        elif expectedmessage != warningmessage:
            print("Testcase Tc009 is fail.")
        else:
            print("Unexpected Error..")


TT1 = Tc001()
TT1.test1()

TT2 = Tc002()
TT2.test2()

TT3 = Tc003()
TT3.test3()

TT4 = Tc004()
TT4.test4()

TT5 = Tc005()
TT5.test5()

TT6 = Tc006()
TT6.test6()

TT7 = Tc007()
TT7.test7()

TT8 = Tc008()
TT8.test8()

TT9 = Tc009()
TT9.test9()





























