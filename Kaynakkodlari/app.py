from flask import Flask
from routes.lost_pet_routes import lost_pet_bp
from routes.found_pet_routes import found_pet_bp

app = Flask(__name__)

app.register_blueprint(lost_pet_bp, url_prefix="/api/lostpets")
app.register_blueprint(found_pet_bp, url_prefix="/api/foundpets")

if __name__ == "__main__":
    app.run(debug=True)
