from selenium import webdriver
import time
# from Login1.BrowserUp import Browser1


class Tc001():
    def test1(self):
        """Enter Valid mail address and password"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()

        time.sleep(4)
        myaccount = driver.find_element_by_xpath(
            "//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')]").click()
        time.sleep(2)

        #Step-2 Click MyAccount Button and SignIn
        signinbutton = driver.find_element_by_xpath("/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[2]/ul[1]/li[1]/ul[1]/li[2]/a[1]").click()
        time.sleep(8)

        #Step-3 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        driver.implicitly_wait(5)

        #Step-4 Enter valid phone number
        phonenumber = driver.find_element_by_xpath("//input[@placeholder='Mobile Number']").send_keys("8571231212")
        time.sleep(2)

        #Step-5 Enter valid username
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)

        #Step-6 Enter valid password with 8 characters
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        ## Scroll down page
        driver.execute_script("window.scrollBy(0,500);")
        time.sleep(3)

        #Step-7 Enter valid confirm password
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASdf1234")
        time.sleep(2)

        #Step-8 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(7)

        actualUrl = " Email Already Exists. "
        warningmessage = driver.find_element_by_xpath("/html[1]/body[1]/div[5]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/form[1]/div[2]/div[1]")
        expectedmessage = " Email Already Exists. "

        warningmessage.text
        if expectedmessage != warningmessage:
            print("Testcase Tc001 is Passed.")
        elif expectedmessage == warningmessage:
            print("Testcase Tc001 is failed.")
        else:
            print("Unexpected Error..")

        print("Complete Sign In. Thank you Andersonnn..")


class Tc002():

    """Leave to empty eMail """

    def test2(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)


        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        #Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']")
        time.sleep(2)
        # Step-3 Enter valid password with 8 characters
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-4 Enter valid confirm password
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASdf1234")
        time.sleep(2)

        ## Scroll down page
        driver.execute_script("window.scrollBy(0,500);")
        time.sleep(3)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

        # User will see warning message
        expectedmessage = " The Email field is required. "
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'The Email field is required.')]")

        if expectedmessage==warningmessage:
            print("Testcase Tc002 is failed.")
        elif expectedmessage != warningmessage:
            print("Testcase Tc002 is Passed.")
        else:
            print("Unexpected Error..")

class Tc003():

    """Leave to empty Password"""

    def test3(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)


        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Leave to empty Password
        password = driver.find_element_by_xpath("//input[@placeholder='Password']")
        time.sleep(2)

        # Step-4 Enter valid confirm password
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASdf1234")
        time.sleep(2)

        ## Scroll down page
        driver.execute_script("window.scrollBy(0,500);")
        time.sleep(3)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(7)

        # User will see warning message
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'The Password field is required.')]").text
        expectedmessage = "The Password field is required."

        if expectedmessage==warningmessage:
            print("Testcase Tc003 is Passed.")
        elif expectedmessage != warningmessage:
            print("Testcase Tc003 is failed.")
        else:
            print("Unexpected Error..")



class Tc004():

    """Password between 1-7 characters"""

    def test4(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)


        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Enter password 3 characters.
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("asd")
        time.sleep(2)

        # Step-4 Enter valid 3 characters confirm passwords.
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("asd")
        time.sleep(2)

        ## Scroll down page
        driver.execute_script("window.scrollBy(0,500);")
        time.sleep(3)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(8)
        warningmessage=driver.find_element_by_xpath("//p[contains(text(),'The Password field must be at least 6 characters in length.')]")
        warningmessage.text
        expectedmessage = "The Password field must be at least 6 characters in length."

        if expectedmessage != warningmessage:
            print("Testcase Tc004 is Passed.")
        elif expectedmessage == warningmessage:
            print("Testcase Tc004 is failed.")
        else:
            print("Unexpected Error..")

class Tc005():

    """Password contains at 4 capital letters  and 4 digit characters"""

    def test5(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Password contains at 4 capital letters  and 4 digit characters
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASDF1234")
        time.sleep(2)

        # Step-4 Enter valid confirm password
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASDF1234")
        time.sleep(2)

        ## Scroll down page
        driver.execute_script("window.scrollBy(0,500);")
        time.sleep(3)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

        actualresults = driver.find_element_by_xpath("//div[contains(text(),' Email Already Exists. ')]")
        actualresults.text
        expectedresults = " Email Already Exists. "

        if actualresults!=expectedresults:
            print("Testcase Tc005 is Passed.")
        elif actualresults == expectedresults :
            print("Testcase Tc005 is failed.")
        else:
            print("Unexpected Error..")

class Tc006():

    """Password contains at 8 letters characters"""

    def test6(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Enter 8 l
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("asdfzxcv")
        time.sleep(2)

        # Step-4 Enter valid confirm password
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("asdfzxcv")
        time.sleep(2)

        ## Scroll down page
        driver.execute_script("window.scrollBy(0,500);")
        time.sleep(3)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(8)

        actualresults = driver.find_element_by_xpath("//div[contains(text(),' Email Already Exists. ')]")
        actualresults.text
        expectedresults = " Password should be contain at least two digits "

        if actualresults==expectedresults:
            print("Testcase Tc006 is Passed.")
        elif actualresults != expectedresults :
            print("Testcase Tc006 is failed.")
        else:
            print("Testcase Tc006, Unexpected Error..")

class Tc007():
    """
    Try available username or mail address
    """

    def test7(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)


        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Enter password 3 characters.
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-4 Enter valid 3 characters confirm passwords.
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASdf1234")
        time.sleep(2)

        ## Scroll down page
        driver.execute_script("window.scrollBy(0,500);")
        time.sleep(3)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(8)

        # User will see warning message "eMail already exist"

        expectedmessage = " Email Already Exists. "
        warningmessage = driver.find_element_by_xpath("//div[@class='alert alert-danger']")
        warningmessage.text
        if expectedmessage!=warningmessage:
            print("Testcase Tc007 is Passed.")
        elif expectedmessage == warningmessage:
            print("Testcase Tc007 is failed.")
        else:
            print("Unexpected Error..")


class Tc008():
    """
    Empty Confirm Password
    """
    def test8(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Enter valid password
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-4 Empty confirm passwords.
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']")
        time.sleep(2)

        ## Scroll down page
        driver.execute_script("window.scrollBy(0,500);")
        time.sleep(3)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath(
            "//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(8)

        # User will see warning message

        expectedmessage = 'The Password field is required.'
        warningmessage = driver.find_element_by_xpath("// p[contains(text(), 'The Password field is required.')]").text

        if expectedmessage != warningmessage:
            print("Testcase Tc008 is Fail.")
        elif expectedmessage == warningmessage:
            print("Testcase Tc008 is Passed. ")
        else:
            print("Unexpected Error..")


class Tc009():
    """
    Enter different confirm password
    """
    def test9(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Enter password 3 characters.
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-4 Enter valid 3 characters confirm passwords.
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ZXcv8900")
        time.sleep(2)

        ## Scroll down page
        driver.execute_script("window.scrollBy(0,500);")
        time.sleep(3)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath(
            "//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(8)

        # User will see warning message "eMail already exist"

        expectedmessage = "Password not matching with confirm password."
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'Password not matching with confirm password.')]").text
        if expectedmessage == warningmessage:
            print("As expected Warning message is : ", expectedmessage , "Testcase Tc009 is passed. ")
        elif expectedmessage != warningmessage:
            print("Testcase Tc009 is fail.")
        else:
            print("Unexpected Error..")


Tc1 = Tc001()
Tc1.test1()

Tc2=Tc002()
Tc2.test2()

Tc3=Tc003()
Tc3.test3()

Tc4=Tc004()
Tc4.test4()

Tc5 = Tc005()
Tc5.test5()

Tc6=Tc006()
Tc6.test6()

Tc7 = Tc007()
Tc7.test7()

Tc8 = Tc008()
Tc8.test8()

Tc9 = Tc009()
Tc9.test9()


