from flask_wtf import FlaskForm
from wtforms import StringField, DateField, EmailField
from wtforms.validators import InputRequired, Length


#Class Name that inherits from FlaskForm
class CreateUser(FlaskForm):
    '''Form to Register to the site'''
    
    username = StringField('Username',
                       validators=[InputRequired(message='Field cannot be empty'),
                                   Length(8)])
    
    password = StringField('Password',
                       validators=[InputRequired(message='Field cannot be empty'),
                                   Length(12)])
    
    #email not mandatory on the db
    email = EmailField('Email', 
                       validators=[InputRequired(message='Field cannot be empty')])
    
    name = StringField('Name',
                       validators=[InputRequired(message='Field cannot be empty'),
                                   Length(30)])
    
    last_name = StringField('Last Name',
                       validators=[InputRequired(message='Field cannot be empty'),
                                   Length(30)])
    
    dob = DateField('Date of Birth',
                       validators=[InputRequired(message='Field cannot be empty')])
    

    
class UserLogin(FlaskForm):
    '''Form to Login to the site'''
    
    username = StringField('Username',
                       validators=[InputRequired(message='Field cannot be empty'),
                                   Length(8)])
    
    password = StringField('Password',
                       validators=[InputRequired(message='Field cannot be empty'),
                                   Length(12)])