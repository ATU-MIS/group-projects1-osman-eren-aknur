class LostPet:
    def __init__(self, pet_id, name, species, description, last_seen_location, owner_id):
        self.pet_id = pet_id
        self.name = name
        self.species = species
        self.description = description
        self.last_seen_location = last_seen_location
        self.owner_id = owner_id
        self.status = "lost"
