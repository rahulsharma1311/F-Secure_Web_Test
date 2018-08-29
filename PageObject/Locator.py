__author__ = "Rahul Sharma"


class Locator(object):

    """To define xpath variable for each pages."""

# Home page locators.
    home_page_url = "https://www.f-secure.com/en/welcome"
    fsec_logo = '//*[@id="frontpage_nav"]/nav/div/div[1]/a/img'
    careers_link = '//*[@id="about"]/li[4]/a'

# Careers page locator.
    job_openings_link = '//*[@id="p4-section-subnav"]/li[3]/a'
    job_openings_link_2 = '//*[@id="p4-section-subnav"]/li[3]/ul/li[2]/a'

# job_opening page locator.
    city_dropdown = '//*[@id="job-city"]'
    job_ad_list = '//*[@id="job-ads"]'