from app import app
from unittest import TestCase
from flask import request

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class LoginViewsTestCase(TestCase):

    def tearDown(self):
        with open('users.txt', 'w') as file:
            file.write('username:Password1:01/01/0001 at 00.00.00\n')

    def test_login_form(self):
        with app.test_client() as client:
            response = client.get('/')
            response_html = response.get_data(as_text=True)

            self.assertEqual(request.path, '/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                '<form action="/authenticate-login" method="POST">', response_html)
            self.assertIn('</form>', response_html)

    def test_authenticate_login(self):
        with app.test_client() as client:
            # New username
            response = client.post(
                '/authenticate-login', data={'username': 'testusername', 'password': 'testpassword'})
            response_html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 302)
            self.assertIn('/show-profile', response.location)

            # Existing username & incorrect password
            response = client.post(
                '/authenticate-login', data={'username': 'username', 'password': 'password'})
            self.assertEqual(response.status_code, 302)
            self.assertIn('/?username_taken=True', response.location)

            # Existing username & correct password
            response = client.post(
                '/authenticate-login', data={'username': 'username', 'password': 'Password1'})
            response_html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 302)
            self.assertIn('/show-profile', response.location)

    def test_show_profile(self):
        with app.test_client() as client:
            response = client.post(
                '/authenticate-login', data={'username': 'testusername', 'password': 'testpassword'}, follow_redirects=True)
            response_html = response.get_data(as_text=True)

            self.assertEqual('/show-profile', request.path)
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                '<div class="card-title text-center">testusername</div>', response_html)
            self.assertIn(
                '<div class="card-footer text-center">Profile Created on ', response_html)
