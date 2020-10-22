from flask import Flask, request, render_template, redirect, url_for
from user_classes import User, UserList

app = Flask(__name__)

users_filename = 'users.txt'

USER_LIST = UserList()
USER_LIST.get_users_from_file(users_filename)

logged_in_user = None


@app.route('/')
def login_form():
    '''
    Renders the login form. If returning
    from an unsuccessful request, show
    username taken text
    '''
    global logged_in_user
    logged_in_user = None
    try:
        username_taken = request.args['username_taken']
        return render_template('form.html', username_taken=bool(username_taken))
    except KeyError as exc:
        return render_template('form.html')


@app.route('/authenticate_login', methods=['POST'])
def authenticate_user():
    '''
    Accepts a username and password as form data. 
    Checks for matching user. 
    If both, takes the user to their profile.
    If only username matches, returns to the form. 
    If neither, creates new user and takes them to their profile
    '''
    username = request.form['username']
    password = request.form['password']

    potential_user = USER_LIST.check_user_in_list(username)
    global logged_in_user

    if not (potential_user):
        logged_in_user = USER_LIST.add_user_to_list(username, password)
        logged_in_user.write_to_file(users_filename)
        return redirect('/show_profile')
    else:
        if potential_user.password == password:
            logged_in_user = potential_user
            return redirect('/show_profile')
        else:
            return redirect(url_for('login_form', username_taken=True))


@app.route('/show_profile')
def show_profile():
    '''
    Gets info from
    the logged in user and
    renders the profile template
    '''
    global logged_in_user
    if (logged_in_user == None):
        return redirect('/')
    else:
        username = logged_in_user.username
        created_at = logged_in_user.created_at
        return render_template('profile.html', username=username, created_at=created_at)
