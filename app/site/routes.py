from flask import Blueprint, render_template

# create variable site (instead of app) because it will relate to how the website renders
# and instantiate the Blueprint() class, tying __name__ that's on the __init__.py
# creating variable template_folder and tying the site_templates folder
# won't create the website but will hand the blueprint over to the __init__.py to actually create it
site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')






