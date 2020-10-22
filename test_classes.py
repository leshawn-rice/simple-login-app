from user_classes import UserList, User
from unittest import TestCase


class UserListTestCase(TestCase):

    def setUp(self):
        self.test_list = UserList()
        self.test_filename = 'static/test_users.txt'
        self.test_users = ['username', 'leshawnrice', 'kellieconnors']
        self.test_passwords = ['Password1', 'Louis123', 'Kellie321']
        self.test_created_ats = ['01/01/0001 at 00.00.00',
                                 '10/22/2020 at 15.17.28',
                                 '10/20/2020 at 08.39.11']

    def test_instantiation(self):
        self.assertIsInstance(self.test_list, UserList)
        self.assertIsInstance(self.test_list.users, set)

    def test_get_users_from_file(self):
        self.test_list.get_users_from_file(self.test_filename)
        self.assertRaises(FileNotFoundError,
                          self.test_list.get_users_from_file, 'unexistingFile')
        self.assertEqual(len(self.test_list.users), 3)

        for user in self.test_list.users:
            self.assertIn(user.username, self.test_users)
            self.assertIn(user.password, self.test_passwords)
            self.assertIn(user.created_at, self.test_created_ats)
