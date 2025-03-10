"""Flask app for searching recipes based on available ingredients"""

from flask import Flask, request, jsonify, render_template, session, flash, redirect
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

@app.route('/', methods=['GET', 'POST'])
def home():
    '''This should render the landing page with the following options:
        -Login
        -Register to create a new account
    '''
    
    form = UserLogin()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.authenticate(username, password)
        
        if user:
            #flash message not displayed
            flash(f"Welcome Back, {user.username}! :)")
            session['user_id'] = user.id
            return redirect('homepage')
        else:
            form.username.errors=['Invalid username/password']
  
    return render_template("index.html", form=form)

#route register
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = CreateUser()
    
    if form.validate_on_submit():
        #add validation to make sure user is not duplicate
        username = form.username.data
        password = form.password.data
        email = form.email.data
        name = form.name.data
        last_name = form.last_name.data
        dob = form.dob.data
        
        new_user = User.register(username, password, email, name, last_name, dob)
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        flash('Welcome! You have successfully created an account')
        return redirect('homepage')
        
    return render_template('register.html', form=form)

#route homepage & keep a user logged in 
@app.route('/homepage')
def homepage():
    if "user_id" not in session:
        #flash message displaying on the bottom of the page. Need to fix
        flash("Please login or register to see the content")
        return redirect ('/')
    return render_template('homepage.html')

#route search results page

#route show recipe

@app.route('/logout')
def logout_user():
    #make this a post request and make a form
    session.pop('user_id')
    flash("Successfully logged out! See you next time!")
    return redirect('/')