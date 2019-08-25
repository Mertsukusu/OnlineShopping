from selenium import webdriver
from pages.flight_page import FlightPage
from base.webdriverfactory import WebDriverFactory

import time
import unittest

class FlightTest(unittest.TestCase):
    def test1(self):
        wd = WebDriverFactory(browser="firefox")
        driver=wd.getWebDriverInstance()

        flgt = FlightPage(driver)
        flgt.flight(" Boston"," New York")

        ExpectedResult = "https://www.expedia.com/Flights-Search?flight-type=on&starDate=07%2F25%2F2019&endDate=08%2F06%2F2019&mode=search&trip=roundtrip&leg1=from%3ABoston%2C+MA+%28BOS-Logan+Intl.%29%2Cto%3ANew+York%2C+NY+%28JFK-John+F.+Kennedy+Intl.%29%2Cdeparture%3A07%2F25%2F2019TANYT&leg2=from%3ANew+York%2C+NY+%28JFK-John+F.+Kennedy+Intl.%29%2Cto%3ABoston%2C+MA+%28BOS-Logan+Intl.%29%2Cdeparture%3A08%2F06%2F2019TANYT&passengers=children%3A0%2Cadults%3A2%2Cseniors%3A0%2Cinfantinlap%3AY"
        ActualResult = driver.current_url

        if ExpectedResult==ActualResult:
            print("test1 is PASS")
        else:
            print("test1 is FAIL")

ff= FlightTest()
ff.test1()