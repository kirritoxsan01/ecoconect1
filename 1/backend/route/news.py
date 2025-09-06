from flask import Blueprint, request, jsonify
from extention import mongo

newsletter_bp = Blueprint("news", __name__)

@newsletter_bp.route("/", methods=["POST"])
def subscribe():
    data = request.get_json()
    email = data.get("email")
    if not email:
        return jsonify({"msg": "Email manquant"}), 400

    if mongo.db.newsletter.find_one({"email": email}):
        return jsonify({"msg": "Déjà inscrit"}), 400

    mongo.db.newsletter.insert_one({"email": email})
    return jsonify({"msg": "Inscription à la newsletter réussie!"})
