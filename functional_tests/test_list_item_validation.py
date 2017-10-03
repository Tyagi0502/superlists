from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

import time


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        time.sleep(2)

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        input_field = self.get_item_input_box()
        input_field.send_keys('Buy milk')
        input_field.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        time.sleep(2)
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        self.check_for_row_in_list_table('1: Buy milk')
        input_field = self.get_item_input_box()
        input_field.send_keys("Make tea")
        input_field.send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_list_table('2: Make tea')