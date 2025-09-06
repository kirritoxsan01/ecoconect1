from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import mongo

events_bp = Blueprint("events", __name__)

# Récupérer tous les événements
@events_bp.route("/", methods=["GET"])
def get_events():
    events = list(mongo.db.events.find({}, {"_id": 0}))
    return jsonify(events), 200


# Ajouter un événement (protégé)
@events_bp.route("/", methods=["POST"])
@jwt_required()
def add_event():
    data = request.get_json()
    if not data or not data.get("title") or not data.get("date"):
        return jsonify({"msg": "Titre et date requis"}), 400

    mongo.db.events.insert_one(data)
    return jsonify({"msg": "Événement ajouté"}), 201
