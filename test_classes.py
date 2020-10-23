from user_classes import UserList, User
from unittest import TestCase


def ftest_get_users_from_file(file):
    '''
    Puts user_info [username,password,created_at]
    into a MD list of users
    Returns users
    '''
    users = []
    for line in file:
        user_info = line.split(':')
        users.append(user_info)
    return users


class UserListTestCase(TestCase):

    def setUp(self):
        '''
        Creates instance of UserList, 
        sets test_filename & test_empty_filename attrs to correct values,
        sets test_users & test_usernames attrs to testing values
        '''
        self.test_list = UserList()
        self.test_filename = 'static/test_users.txt'
        self.test_empty_filename = 'static/test_empty_users.txt'
        self.test_users = {
            'username', 'Password1', '01/01/0001 at 00.00.00',
            'testuser', 'testpassword', '10/22/2020 at 15.17.28',
            'futureuser', 'FuturePassword1', '10/20/2020 at 08.39.11'
        }
        self.test_usernames = ['username', 'testuser', 'futureuser']

    def tearDown(self):
        '''
        Overwrites empty file with an empty string
        '''
        with open(self.test_empty_filename, 'w') as file:
            file.write('')

    def test_instantiation(self):
        '''
        Assertions:
                    self.test_list is instance of UserList
                    self.test_list.users is instance of set
        '''
        self.assertIsInstance(self.test_list, UserList)
        self.assertIsInstance(self.test_list.users, set)

    def test_get_users_from_file(self):
        '''
        Assertions:
                    Passing an invalid filename raises an error
                    self.test_users.users has a length of 3 (with current test values)
                    Each user has correct username, password, and created_at value
        '''
        self.test_list.get_users_from_file(self.test_filename)
        self.assertRaises(FileNotFoundError,
                          self.test_list.get_users_from_file, 'unexistingFile')
        self.assertEqual(len(self.test_list.users), 3)

        for user in self.test_list.users:
            self.assertIn(user.username, self.test_users)
            self.assertIn(user.password, self.test_users)
            self.assertIn(user.created_at, self.test_users)

    def test_write_users_to_file(self):
        '''
        Assertions:
                    Username for each user is in self.test_users
                    Password for each user is in self.test_users
                    CreatedAt for each user is in self.test_users
        '''
        self.test_list.get_users_from_file(self.test_filename)
        self.test_list.write_users_to_file(self.test_empty_filename)

        file = open(self.test_empty_filename, 'r')
        users = ftest_get_users_from_file(file)
        file.close()

        for user in users:
            self.assertIn(user[0].strip(), self.test_users)
            self.assertIn(user[1].strip(), self.test_users)
            self.assertIn(user[2].strip(), self.test_users)

    def test_check_user_in_list(self):
        '''
        Assertions:
                    With user that should exist, returns an instance of User
                    With user that does exist, returns user whose username is correct
                    With user that doesnt exist, returns None
        '''
        self.test_list.get_users_from_file(self.test_filename)
        for username in self.test_usernames:
            self.assertIsInstance(
                self.test_list.check_user_in_list(username), User)
            self.assertEqual(
                username, self.test_list.check_user_in_list(username).username)
        self.assertIsNone(self.test_list.check_user_in_list(
            'usernameThatDoesntExist'))

    def test_add_user_to_list(self):
        '''
        Assertions:
                    Each user added is an instance of User
                    Each user added has the correct username
                    Each user added has the correct password
        '''
        self.test_list.add_user_to_list('testuser', 'testpassword')
        for user in self.test_list.users:
            self.assertIsInstance(user, User)
            self.assertEqual('testuser', user.username)
            self.assertEqual('testpassword', user.password)


class UserTestCase(TestCase):
    def setUp(self):
        '''
        Creates new instance of User and
        sets test_filename to empty file
        '''
        self.test_user = User('testname', 'testpassword')
        self.test_filename = 'static/test_empty_users.txt'

    def tearDown(self):
        '''
        Overwrites file with an empty string
        '''
        file = open(self.test_filename, 'w')
        file.write('')
        file.close()

    def test_instantiation(self):
        '''
        Assertions:
                    test_user added is an instance of User
                    test_user has the correct username
                    test_user has the correct password
                    test_user has a string for created_at
        '''
        self.assertIsInstance(self.test_user, User)
        self.assertEqual(self.test_user.username, 'testname')
        self.assertEqual(self.test_user.password, 'testpassword')
        self.assertIsInstance(self.test_user.created_at, str)

    def test_get_created_time(self):
        '''
        Assertions:
                    Return val from get_created_time() is a string
                    Return val from get_created_time() has a length of 22 (XX/XX/XX at XX.XX.XX)
        '''
        self.assertIsInstance(self.test_user.get_created_time(), str)
        self.assertEqual(len(self.test_user.get_created_time()), 22)

    def test_write_to_file(self):
        '''
        Assertions:
                    written file username is correct
                    written file password is correct
                    written file created_at is of correct length
        '''
        self.test_user.write_to_file(self.test_filename)
        file = open(self.test_filename)
        users = ftest_get_users_from_file(file)
        file.close()
        for user in users:
            self.assertEqual(user[0].strip(), 'testname')
            self.assertEqual(user[1].strip(), 'testpassword')
            self.assertEqual(len(user[2].strip()), 22)
