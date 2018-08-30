__author__ = "Rahul Sharma"

from PageObject.Pages.HomePage import Home
from PageObject.Pages.CareersPage import CareerPage
from PageObject.Pages.JobOpeningsPage import JobOpeningsPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from PageObject.Locator import Locator
import re
import time


class SearchJob(object):

    """Script to run TestCase for a job search on fsecure portal."""

    def __init__(self, driver):
        self.driver = driver

    def searchCareerClick(self):
        """ On home page search Careers link. Navigate and click on link."""
        home = Home(self.driver)
        print("   TestSteps:")
        print("     -- Browse F-Secure Home Page.")
        home.browseFsecHome()
        career = home.getCareers()
        assert career is not None, "Careers link not found in page."
        print("     -- Navigate to Careers link.")
        self.driver.execute_script("arguments[0].scrollIntoView();", home.getCareers())
        print("     -- Click on career link.")
        career.click()
        time.sleep(5)
        assert "Career" in self.driver.title, "Career page not loaded within 5 sec."
        print("     -- Career page opened successfully.")
        del home

    def searchJobOpeningClick(self):
        """ On Careers page search Job opening link. Navigate and click on link."""
        careerObj = CareerPage(self.driver)
        jobOpeningLink = careerObj.getJobOpeningsLink()
        assert jobOpeningLink is not None, "JobOpening link not found in page."
        print("     -- Navigate to job opening link.")
        self.driver.execute_script("arguments[0].scrollIntoView();", careerObj.getJobOpeningsLink())
        hover = ActionChains(self.driver).move_to_element(jobOpeningLink)
        hover.perform()
        time.sleep(2)
        jobOpeningLink_1 = careerObj.getJobOpeningsLink_2()
        print("     -- Click on Job opening link.")
        jobOpeningLink_1.click()
        time.sleep(5)
        assert "Openings" in self.driver.title, "JobOpenings page not loaded within 5 sec."
        print("     -- JobOpenings page opened successfully.")
        del careerObj

    def searchJobAdClick(self, keyword):
        """ On Job openings page search for keyword. Navigate and click on link."""
        self.keyword = keyword
        JobOpeningObj = JobOpeningsPage(self.driver)
        jobAdListLink = JobOpeningObj.getJobAdListLink()
        assert jobAdListLink is not None, "JobOpening link not found in page."
        print("     -- Job-Ad list box identified.")
        ad_list_elements = JobOpeningObj.getJobListElements()
        total_jobs = len(ad_list_elements)
        total_pages = int(total_jobs/6) + 1
        print("         Total Jobs listed: " + str(total_jobs))
        print("         Total Job Pages: " + str(total_pages))
        jobs_list = []
        for i in range(total_jobs):
            index = i+1
            element_xpath = Locator.view_job_element + str(index) +"]/a"
            element_handle = self.driver.find_element(By.XPATH, element_xpath)
            job = element_handle.get_attribute('data-track-name')
            job_name = job.split('-')
            jobs_list.append([index, job_name[1].strip()])
        print("     -- Searching for specific job on list. keyword: " + keyword, end='\n\n')
        for job in jobs_list:
            job_index = job[0]
            job_string = job[1].lower()
            if re.match(("^.*" + keyword + ".*"), job_string):
                print("          Matching Job: " + job_string)
                if job_index % 6 == 0:
                    element_page_no = int(job_index/6)
                else:
                    element_page_no = int(job_index/6) + 1
                print("          Page no.: " + str(element_page_no), end='\n\n')