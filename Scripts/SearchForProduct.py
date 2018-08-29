__author__ = "Rahul Sharma"

from PageObject.Locator import Locator
from PageObject.Pages.HomePage import Home
from PageObject.Pages.CareersPage import CareerPage
import time


class SearchProduct(object):

    """Script to run TestCase for a job search on fsecure portal."""

    def __init__(self, driver):
        self.driver = driver