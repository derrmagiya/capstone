from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
import uuid 
from datetime import datetime 


# Adding Flask Security for passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Import Secrets Module
import secrets

# import for LoginManager & UserMixin
# helps us login our usere & store their credentials
from flask_login import UserMixin, LoginManager

# import from Flask-Marshmallow
from flask_marshmallow import Marshmallow 

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) 


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = False, default = '')
    username = db.Column(db.String, nullable = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    fitness_activities = db.relationship('Fitness', backref='owner', lazy=True)

    def __init__(self, email, username, password, first_name = '', last_name = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token()
        self.username = username 


    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        return generate_password_hash(password)
    
    def set_token(self):
        return secrets.token_hex(24)
    

    def __repr__(self):
        return f"User {self.email} has been added to the database! Woohoo!"
    

class Fitness(db.Model):
    id = db.Column(db.String, primary_key=True)
    exercise_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    duration_minutes = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    random_joke = db.Column(db.String, nullable=True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)

    def __init__(self, exercise_name, description, duration_minutes, calories_burned, date_created, random_joke, user_token):
        self.id = self.set_id()
        self.exercise_name = exercise_name
        self.description = description
        self.duration_minutes = duration_minutes
        self.calories_burned = calories_burned
        self.date_created = datetime.utcnow()  # Initialize the date_created attribute with the current time
        self.random_joke = random_joke
        self.user_token = user_token

    def set_id(self):
        return str(uuid.uuid4())
    
    def __repr__(self):
        return f"Fitness {self.exercise_name} has been added to the database! Woohoo!"
    
class FitnessSchema(ma.Schema):
    class Meta:
        fields = ['id', 'exercise_name', 'description', 'duration_minutes', 'calories_burned', 'date_created', 'random_joke']

fitness_schema = FitnessSchema()
fitnesses_schema = FitnessSchema(many = True)