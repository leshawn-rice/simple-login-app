from flask import Flask, request, render_template, redirect, url_for
from user_classes import User, UserList

app = Flask(__name__)

users_filename = 'users.txt'

USER_LIST = UserList()
USER_LIST.get_users_from_file(users_filename)

logged_in_user = None


def check_auth(auth_data):
    '''
    Checks for matching user using auth_data. 
    If both, returns that user and the /show-profile path.
    If only username matches, returns None and the /?username_taken=True path. 
    If neither, creates new user and returns it and the /show-profile path
    '''
    [potential_user, username, password] = auth_data

    logged_in_user = None

    if not (potential_user):
        logged_in_user = USER_LIST.add_user_to_list(username, password)
        logged_in_user.write_to_file(users_filename)
        redirect_url = ('/show-profile')
    else:
        if potential_user.password == password:
            logged_in_user = potential_user
            redirect_url = ('/show-profile')
        else:
            redirect_url = url_for('login_form', username_taken=True)
    return logged_in_user, redirect_url


@app.route('/')
def login_form():
    '''
    Renders the login form. If returning
    from an unsuccessful request, show
    username taken text
    '''
    logged_out = request.args.get('logged_out', None)
    global logged_in_user
    if logged_out:
        logged_in_user = None
    try:
        username_taken = request.args['username_taken']
        return render_template('form.html', username_taken=bool(username_taken))
    except KeyError as exc:
        return render_template('form.html')


@app.route('/authenticate-login', methods=['POST'])
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

    auth_data = [potential_user, username, password]

    global logged_in_user
    logged_in_user, redirect_url = check_auth(auth_data)

    return redirect(redirect_url)


@app.route('/show-profile')
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
