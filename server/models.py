from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates('name')
    def validate_name(self,key,name):
        if not name:
            raise ValueError("Author must have a name")
        return name

    @validates('phone_number')
    def validate_phonenumber(self, key, value):
        if len(value) < 10:
            raise ValueError('Phone number must be 10 digits')
        return value


    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    validates('content')
    def validate_post(self, key, content):
        if len(content) < 250:
            raise ValueError("Post content must be at least 250 words")
        return content

    @validates('summary')
    def validate_summary(self,key,summary):
        if len(summary) > 250:
            raise ValueError("Summary must be a maximum of 250 words")
        return summary

    @validates('category')
    def validate_category(self,key,category):
        if ("Fiction" or "Non-Fiction") not in category :
            raise ValueError("Category must either be Fiction or Non-Fiction")
        return category

    @validates('title')        
    def validate_title(self, key, title):
        if ("Won't believe " or  "Secret" or "Top {number}" or "Guess") not in title:
            raise ValueError("Title is not valid")
        return title


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
