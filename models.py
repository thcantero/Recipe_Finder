from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

bcrypt = Bcrypt()

class User(db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    
    username = db.Column(db.String(80), 
                         unique=True, 
                         nullable=False)
    
    password_hash = db.Column(db.String(256), 
                              nullable=False)
    
    email = db.Column(db.String(120), 
                      unique=True)
    
    name = db.Column(db.String(20),
                         nullable=False)
    
    last_name = db.Column(db.String(20),
                         nullable=False)
    
    dob = db.Column(db.Date,
                    nullable=False)
        
    @classmethod
    def register(cls, username, pwd, email, name, last_name, dob):
            '''Register user with hashed password and return user'''
            
            hashed = bcrypt.generate_password_hash(pwd)
            
            #turn bytestrung into normal string (unicode utf8)
            hashed_utf8 = hashed.decode("utf8")
            
            return cls(
                username=username,
                password_hash=hashed_utf8,
                email=email,
                name=name,
                last_name=last_name,
                dob=dob)
            
    @classmethod
    def authenticate(cls, username, pwd):
        '''Validate that user exists & password is correct.
        
        Return user if valid, else return False'''
        
        u = User.query.filter_by(username=username).first()
        
        if u and bcrypt.check_password_hash(u.password_hash, pwd):
            #return user instance
            return u
        else:
            return False
    

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)

class Recipe(db.Model):
    
    __tablename_ = 'recipes'
    
    id = db.Column(db.Integer, 
                   primary_key=True)
    
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.id'), 
                        nullable=False)
    
    recipe_id = db.Column(db.String(100), 
                          nullable=False)
    
    recipe_name = db.Column(db.String(200), 
                            nullable=False)
    
    timestamp = db.Column(db.DateTime, 
                          default=db.func.current_timestamp())
    
    
def connect_db(app):
    '''Connect db to Flask App'''
    db.app = app
    db.init_app(app)
    
    
    #Search by ingredient get recipe ID and save all recipe in the db
    #cache
    #recipe has multiple ingredients: Recipe saves the recipes the user has searched / saved / add a field for favs