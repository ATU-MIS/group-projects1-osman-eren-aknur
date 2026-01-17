from flask import Blueprint, request, jsonify
from models.found_pet import FoundPet
from services.matching_service import match_found_pet
from services.notification_service import send_notification
import time

found_pet_bp = Blueprint("found_pet_bp", __name__)
found_pets = []
lost_pets = []  # simülasyon amaçlı

@found_pet_bp.route("/", methods=["POST"])
def create_found_pet():
    data = request.json
    found_pet = FoundPet(
        pet_id=int(time.time()),
        species=data["species"],
        description=data["description"],
        found_location=data["location"],
        finder_id=data["finder_id"]
    )

    matches = match_found_pet(found_pet, lost_pets)

    if matches:
        send_notification(matches[0].owner_id, "Your pet may have been found!")
        return jsonify({"message": "Match found"}), 200
    else:
        found_pets.append(found_pet)
        return jsonify({"message": "No match found, saved as found pet"}), 200
