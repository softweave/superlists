__author__ = 'janee'

from selenium import webdriver
import unittest

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
        self.fail('Finish the test!')

        # see invitation to enter a to-do item

        # type "buy peacock featuers" into a text box

        # hit enter, page updates and the page lists here entry as an item in a to-do list

        # text box invites adding another item

        # type use peacock feathers to make fan for dancing

        # page updates and shows both items

        # see unique url for page and visit that url -- to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
