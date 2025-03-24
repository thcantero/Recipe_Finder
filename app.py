"""Flask app for searching recipes based on available ingredients"""

import os, requests
from flask import Flask, request, jsonify, render_template, session, flash, redirect
from models import db, connect_db, User, Recipe
from flask_debugtoolbar import DebugToolbarExtension
from dotenv import load_dotenv
from flask_cors import CORS
from forms import UserLogin, CreateUser

app = Flask(__name__)
CORS(app)

#Load Keys
load_dotenv()

SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///recipefinder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

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
    result = validate_login()
    
    return render_template('homepage.html')

@app.route('/logout')
def logout_user():
    #make this a post request and make a form
    session.pop('user_id')
    flash("Successfully logged out! See you next time!")
    return redirect('/')

# Create a function to check if the user is logged in (Directive)
def validate_login():
    '''
    Checks if a user is logged in by looking at the session.
    Returns True if logged in, otherwise redirects to '/'
    '''
    
    if 'user_id' not in session:
        flash("Please login or register to see the content")
        return redirect('/')
    
    #If user is logged in, return True
    return True
    
@app.route('/search-ingredients')
def choose_ingredients():
    '''
    Search and choose ingredients to look for recipes
    '''
    
    # query = request.args.get('q')
    # if not query:
    #     return jsonify([]) #Return empty list if no query
    
    # url = 'https://api.spoonacular.com/food/ingredients/autocomplete'
    # params = {
    #     'apiKey': SPOONACULAR_API_KEY,
    #     'query': query,
    #     'number': 10 #number of suggestions showed
    # }
    
    #resp = request.get(url, params)
    
    return render_template('ingredients-search.html')


@app.route('/recipe/<ingredients>')
def show_recipes(ingredients):
    '''
    Show the possible recipes that could be cooked with the available ingredients.
    URL: https://api.spoonacular.com/recipes/findByIngredients
    
    Parameters:
    ingredients: string. A comma-separated list of ingredients that the recipes should contain.
    number: int. The maximum number of recipes to return (1 - 100)
    ranking : int. Whether to maximize user ingredients (1) or minimize missing ingredients (2) first.
    ignorePantry: boolean. Whether to ignore typical pantry items, such as water, salt, flour, etc.
    '''

    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    #ingredients = ['apples','flour','sugar']
    
    params = {
        'apiKey': SPOONACULAR_API_KEY,
        'ingredients': ingredients,
        'number': 15,
        'ranking': 1,
        'ignorePantry': 'true'
    }
    
    resp = requests.get(url, params=params)
    
    data = resp.json() #list of recipes
    return render_template('show-recipes.html', recipes=data, ingredients=ingredients)
    
    
    
    

@app.route('/recipe/<int:id>')
def display_recipe(id):
    '''
    Display the recipe details according to the id received
    '''
    
    