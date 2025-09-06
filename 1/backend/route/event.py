from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extention import mongo

events_bp = Blueprint("events", __name__)

@events_bp.route("/", methods=["GET"])
def get_events():
    events = list(mongo.db.events.find({}, {"_id": 0}))
    return jsonify(events)

@events_bp.route("/", methods=["POST"])
@jwt_required()
def add_event():
    data = request.get_json()
    title = data.get("title")
    date = data.get("date")

    if not title or not date:
        return jsonify({"msg": "Champs manquants"}), 400

    mongo.db.events.insert_one({"title": title, "date": date})
    return jsonify({"msg": "Événement ajouté avec succès!"})
