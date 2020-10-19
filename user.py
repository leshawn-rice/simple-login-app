from datetime import datetime

# Generate a token for users for auth

# Add doctests


class UserList(object):
    '''
    Class that holds a set of User instances
    '''

    def __init__(self):
        '''
        Initializes the users attribute to a new set
        '''
        self.users = set()

    def __repr__(self):
        return f'UserList()'

    def get_users_from_file(self, filename):
        '''
        str:
            filename
        iterates through lines in a file, setting
        each line to a new User instance and adding
        it to the users attribute
        '''
        file = open(filename, 'r')
        for line in file:
            user_info = line.split(':')
            user = User(user_info[0], user_info[1])
            self.users.add(user)
        file.close()

    def write_users_to_file(self, filename):
        '''
        str:
            filename
        writes each user stored in the users attribute
        to the given file. Useful for recreating a user file
        '''
        for user in self.users:
            user.write_to_file(filename)

    def check_user_in_list(self, username):
        '''
        str:
            username
        checks if the given username matches a user
        in the users attribute. 
        Returns the user if so, otherwise
        Returns None
        '''
        for user in self.users:
            if user.username == username:
                return user
        return None

    def add_user_to_list(self, username, password):
        '''
        str:
            username
        str:
            password
        creates a new User instance and adds it to 
        the users attribute
        '''
        user = User(username, password)
        self.users.add(user)
        return user


class User(object):
    '''
    Class that stores user information
    '''

    def __init__(self, username, password):
        '''
        str:
            username
        str:
            password
        Strips whitespace from the username and
        password and sets them as attributes.
        Gets the time the user was created
        '''
        self.username = username.strip()
        self.password = password.strip()
        self.created_at = self.get_created_time()

    def __repr__(self):
        return f'User(username={self.username}, password={self.password})'

    def get_created_time(self):
        '''
        Gets the current raw time data from
        the now method on datetime, and parses
        it into a readable string.
        '''
        raw_time = datetime.now()
        return raw_time.strftime('%m/%d/%Y at %H:%M:%S')

    def write_to_file(self, filename):
        '''
        str:
            filename
        Appends the username and password
        attributes to the given file.
        '''
        file = open(filename, 'a')
        file.write(f'{self.username}:{self.password}\n')
        file.close()
