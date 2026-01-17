def match_found_pet(found_pet, lost_pets):
    matches = []

    for pet in lost_pets:
        if pet.species == found_pet.species and \
           found_pet.description.lower() in pet.description.lower():
            matches.append(pet)

    return matches
