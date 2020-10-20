# Simple Flask Login Application

## Uses Bootstrap for styling
## Uses jQuery on profile page for logout event listener

### This is not intended to be a secure login form
### This is intended to mini test app to test functionality

# Demo

![Landing Page (Login Form) On first load](/assets/images/on_load.jpg "Index Page on load")
## The index page on load. Contains a bootstrap card with a form for username and password.
![Landing Page (Login Form) if username taken and password invalid](/assets/images/username_taken.jpg "Index Page for taken username")
## The index page after an unsuccessful login attempt. If username exists but password does not match the password on file, will display "Username Taken" text.
![Landing Page (Login Form) with username or password includes ":"](/assets/invalid_character.jpg "Index Page for invalid input")
## The index page if a user attempts to create a username or password that includes the ":" character.
![Landing Page (Login Form) if password invalid](/assets/images/invalid_password.jpg "Index Page for invalid password")
## The index page if a user attempts to create a password that is not 8+ characters with 1+ uppercase and 1+ lowercase letters
![Profile Page](/assets/images/profile.jpg "Profile Page")
## The profile page on load. The logout button will redirect the user to the index page


# Future Updates:

### v2 will include doctests for class methods 
### v3 will include tests for view functions