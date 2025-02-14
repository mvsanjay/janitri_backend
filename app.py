from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate

# Import Blueprints
from routes.users import users_bp
from routes.patients import patients_bp
from routes.heart_rate import heart_rate_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprints
app.register_blueprint(users_bp)
app.register_blueprint(patients_bp)
app.register_blueprint(heart_rate_bp)

@app.route("/")  # Test route to check if the app is running
def home():
    return "Welcome to the Janitri Backend API!"

if __name__ == "__main__":
    app.run(debug=True)
