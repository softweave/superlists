from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):
    # def test_bad_maths(self):
    #     self.assertEquals(1+1, 3)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_url(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertIn('A new list item', response.content.decode())

        expected_html = render_to_string(
            'home.html',
            {'new_item_text': "A new list item"}
        )
        self.assertEqual(response.content.decode(), expected_html)


        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do Lists</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))



