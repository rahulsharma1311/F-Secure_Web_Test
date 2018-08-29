__author__ = "Rahul Sharma"

from PageObject.Locator import Locator
from selenium.webdriver.common.by import By


class CareerPage(object):
    """ F-Secure web portal's CareerPage objects."""

    def __init__(self, driver):
        self.driver = driver
        self.job_opening_link = driver.find_element(By.XPATH, Locator.job_openings_link)
        self.job_opening_link_2 = driver.find_element(By.XPATH, Locator.job_openings_link_2)

    def getJobOpeningsLink(self):
        return self.job_opening_link

    def getJobOpeningsLink_2(self):
        return self.job_opening_link_2

