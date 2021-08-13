from flask_sqlalchemy import SQLALchemy 

BASE_IMG = "https://unsplash.com/photos/MVIqwQvkwG4"

db = SQLALchemy

class Pet(db.Model):
    """pet for adoption"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """return pet image"""
        return self.photo_url or BASE_IMG

def connect_db(app):
    """Connect the database to app.py"""
    db.app = app
    db.init_app(app)
