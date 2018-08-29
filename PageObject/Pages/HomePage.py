__author__ = "Rahul Sharma"

from PageObject.Locator import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Home(object):
    """ F-Secure web portal's Homepage objects."""

    def __init__(self, driver):
        self.driver = driver
        self.home_url = Locator.home_page_url

    def browseFsecHome(self):
        self.driver.maximize_window()
        self.driver.get(self.home_url)
        time.sleep(5)
        assert "Cyber" in self.driver.title, "Home page not loaded within 5 sec."

    def getCareers(self):
        self.career_page_link = self.driver.find_element(By.XPATH, Locator.careers_link)
        return self.career_page_link


if __name__ == "__main__":
    driver = webdriver.Chrome("C:\\Users\\rahul_sharma4\\PycharmProjects\\F-Secure_job\\chromedriver.exe")
    h = Home(driver)
    h.browseFsecHome()
    driver.quit()
    driver = webdriver.Firefox(executable_path="geckodriver.exe")
    h = Home(driver)
    h.browseFsecHome()
    driver.quit()
