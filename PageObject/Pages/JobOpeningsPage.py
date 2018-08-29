__author__ = "Rahul Sharma"

from PageObject.Locator import Locator
from selenium.webdriver.common.by import By


class JobOpeningsPage(object):
    """ F-Secure web portal's JobOpening page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.city_drop_link = driver.find_element(By.XPATH, Locator.city_dropdown)
        self.job_ad_link = driver.find_element(By.XPATH, Locator.job_ad_list)

    def getCityDropDownLink(self):
        return self.city_drop_link

    def getJobAdListLink(self):
        return self.job_ad_link
