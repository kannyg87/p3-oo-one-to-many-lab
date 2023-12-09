class Owner:
    def __init__(self, name):
        self.name = name

    
    def pets(self):
        owner_pets = []
        for pet in Pet.all:
            if pet.owner == self:
                owner_pets.append(pet)
        return owner_pets 
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Provided object is not a Pet instance")
        pet.owner = self 


    def get_sorted_pets(self):
        return sorted(self.pets(),key=lambda pet: pet.name)
         #  (pet)=> pet.name

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)



