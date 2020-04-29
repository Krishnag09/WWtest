# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import page


class Weightwatchers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
        #1. Navigate to https://www.weightwatchers.com/us/
        self.driver.get("https://www.weightwatchers.com/us/")

    def test_weightwatchers(self):

        main_page = page.MainPage(self.driver)
        #2. Verify loaded page title matches “WW (Weight Watchers): Weight Loss & Wellness Help”
        assert main_page.title_matches(), "Weight Loss & Wellness Help, does not match"
        #3. On the right corner of the page, click on “Find a Studio”
        main_page.click_find_workshop()
        #4. Verify loaded page title contains “Find WW Studios & Meetings Near You | WW USA”
        searchworkshoppage = page.SearchWorkshopPage(self.driver)
        assert searchworkshoppage.title_matches, "Find WW Studios & Meetings Near You | WW USA"

        self.driver.implicitly_wait(3)
        #5. In the search field, search for meetings for zip code: 10011
        searchworkshoppage.type_seach_term("10001")
        searchworkshoppage.click_on_search()
        # 6. Print the title of the first result and the distance (located on the right of location title/name)
        search_results_page = page.SearchResultsPage(self.driver)
        #7. Click on the first search result and then, verify displayed location name/title matches with the name of the first searched result that was clicked.
        location_on_search_result = search_results_page.return_location_name()
        search_results_page.click_on_first_location()
        location_details_page = page.LocationDetailsPage(self.driver)
        location_details_locationname = location_details_page.assert_location_is_same()
        assert (location_on_search_result ==location_details_locationname)
        # 8. From this location page, print TODAY’s hours of operation (located towards the bottom of the page) - This is missing in page right now
        #9. Create a method to print the number of meeting the each person(under the scheduled time) has a particular day of the week
        print ("test")
    	day = raw_input("Enter the Day: Mon Tue Wed Thur Fri Sat Sun ")
    	location_details_page.printmeetings(day)





    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


