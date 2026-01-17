from flask import Blueprint, request, jsonify
from models.lost_pet import LostPet
from services.notification_service import send_notification
import time

lost_pet_bp = Blueprint("lost_pet_bp", __name__)
lost_pets = []

@lost_pet_bp.route("/", methods=["POST"])
def create_lost_pet():
    data = request.json
    pet = LostPet(
        pet_id=int(time.time()),
        name=data["name"],
        species=data["species"],
        description=data["description"],
        last_seen_location=data["location"],
        owner_id=data["owner_id"]
    )

    lost_pets.append(pet)
    send_notification("nearby-users", "Lost pet nearby!")

    return jsonify({"message": "Lost pet report created"}), 201


@lost_pet_bp.route("/", methods=["GET"])
def get_lost_pets():
    return jsonify([pet.__dict__ for pet in lost_pets])
