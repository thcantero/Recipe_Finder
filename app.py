"""Flask app for searching recipes based on available ingredients"""

from flask import Flask, request, jsonify, render_template, session, flash
from models import db, connect_db, User, Recipe
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from forms import UserLogin, CreateUser

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///recipefinder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    '''This should render the landing page with the following options:
        -Login
        -Register to create a new account
    '''
    
    form = UserLogin()
    
    return render_template("index.html", form=form)