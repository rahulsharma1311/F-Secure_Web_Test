from selenium import webdriver
from Scripts.SearchForJob import SearchJob
from PageObject.Pages.HomePage import Home
import re
import datetime


with open("TestCases.txt") as TC:
    for line in TC:
        if re.match("^#.+",line):
            continue
        tc_details = line.split()
        tc_id = tc_details[0].strip(":")
        testcase = tc_details[1].lower()
        browser = tc_details[2].lower()
        driver = None
        if browser == "chrome":
            driver = webdriver.Chrome("chromedriver.exe")
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path="geckodriver.exe")
        else:
            assert driver is not "", "Browser not in list."
            print("TestCase_ID: " + tc_id + " failed. Reason: Browser not supported.")
            continue
        keyword_to_search = ' '.join(tc_details[3:]).lower()
        print("\n## " + tc_id + ": started at: " + str(datetime.datetime.now()))
        if testcase in ('searchjob', 'searchproduct'):
            if testcase == 'searchjob':
                try:
                    run = SearchJob(driver)
                    run.searchCareerClick()
                    run.searchJobOpeningClick()
                    run.searchJobAdClick(keyword_to_search)
                except AssertionError as error:
                    print("## " + tc_id + ": TestCase Failed. Error: " + str(error))
                    continue
                #except Exception as error:
                    #print("## " + tc_id + ": TestCase Failed. Error: " + str(error))
                    #continue
                else:
                    print("## " + tc_id + " : TestCase Passed. endtime: " + str(datetime.datetime.now()))
                finally:
                    print("## " + tc_id + " execution done.", end='\n\n')

            elif testcase == 'searchproduct':
                print("TestCase not implemented.")
        else:
            print("TestCase Script not supported. Write script in Scripts module.")
            continue
        driver.quit()
