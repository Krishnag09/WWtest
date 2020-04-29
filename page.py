# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait



class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):


    def title_matches(self):
        """Verifies that the hardcoded text ""Weight Loss & Wellness Help" " appears in page title"""
        return "Weight Loss & Wellness Help"  in self.driver.title

    def click_find_workshop(self):
        """clicks on Find a Workshop"""
        findaworkshop =  self.driver.find_element_by_link_text("Find a Workshop")
        findaworkshop.click()

class SearchWorkshopPage(BasePage):

	def title_matches(self):
		return "Find WW Studios & Meetings Near You | WW USA"  in self.driver.title

	def type_seach_term(self, zipcode):
			self.driver.find_element_by_css_selector('input[id= meetingSearch]').send_keys(zipcode)

	def click_on_search(self):
			self.driver.find_element_by_css_selector('button[spice=SEARCH_BUTTON]').click()

		
class SearchResultsPage(BasePage):
    """Search results page  methods come here"""

    def return_location_name(self):
        results_location_text = self.driver.find_elements_by_css_selector('div[class=location__name]')[0].text
        return results_location_text


    def click_on_first_location(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        results_location = self.driver.find_elements_by_css_selector('div[class=location__name]')[0]
        results_distance = self.driver.find_elements_by_css_selector('div[class=location__distance]')[0].text
        results_location.click()


class LocationDetailsPage(BasePage):
	"""docstring for ClassName"""

	def assert_location_is_same(self):
		details_location = self.driver.find_element_by_css_selector('div[class=location__name]').text
		return details_location

	def printmeetings(self,day):
		location_hrs = self.driver.find_element_by_xpath("//div[contains(text(),'"+day+"')]")
		location_hrs_days = location_hrs.find_element_by_xpath('..')
		meetings = location_hrs_days.find_elements_by_css_selector('div[class=schedule-detailed-day-meetings-item-time]')
		nameelements = location_hrs_days.find_elements_by_css_selector('div[class=schedule-detailed-day-meetings-item-leader]')
		names = []
		namefreqpairs = dict()
		for nameelement in nameelements:
			names.append(nameelement.text.encode("ascii"))
		for name in names:
			if name in namefreqpairs:
				namefreqpairs[name] += 1
			else:
				namefreqpairs[name] = 1
			# print namefreqpairs
		for name, freq in namefreqpairs.items():
			print (name+ " "+ str(freq))













