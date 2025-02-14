from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

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

# Swagger UI setup
SWAGGER_URL = "/api/docs"
API_URL = "/swagger.yaml"
swagger_bp = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)

@app.route("/")  # Test route to check if the app is running
def home():
    return "Welcome to the Janitri Backend API!"

if __name__ == "__main__":
    app.run(debug=True)
