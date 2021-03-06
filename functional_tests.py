__author__ = 'janee'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser .quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # check out the homepage
        self.browser.get('http://localhost:8000')

        # check out the page title and header
        # assert 'To-Do' in browser.title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # see invitation to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # type "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # hit enter, page updates and the page lists here entry as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(10)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     'New to-do item did not appear in table -- its text was:\n%s' % (
        #         table.text
        #     )
        # )
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # text box invites adding another item
        self.fail('Finish the test!')

        # type use peacock feathers to make fan for dancing

        # page updates and shows both items

        # see unique url for page and visit that url -- to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
