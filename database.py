from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_tables()
