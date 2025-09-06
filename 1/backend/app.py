from flask import Flask
from flask_cors import CORS
from config import Config
from extention import mongo, bcrypt, jwt

# Créer l'application Flask
app = Flask(
    __name__,
    static_folder="frontend",
    template_folder="frontend"
)

# Charger la configuration
app.config.from_object(Config)

# Initialiser les extensions
CORS(app)
mongo.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Importer les blueprints après init_app pour éviter circular imports
from routes.auth import auth_bp
from routes.event import events_bp
from routes.newsletter import newsletter_bp

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(events_bp, url_prefix="/api/events")
app.register_blueprint(newsletter_bp, url_prefix="/api/newsletter")

# Route de test pour vérifier si le serveur tourne
@app.route("/ping")
def ping():
    return "pong", 200

# Servir le front-end
@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=Config.DEBUG, host="0.0.0.0", port=5000)
