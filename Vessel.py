class Vessel:
    def __init__(self, name, max_health, coordinates):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.coordinates = coordinates

    def move(self, new_coordinates):
      if (self.coordinates != new_coordinates):
          self.coordinates = new_coordinates
          print(f"Vessel has been moved to {self.coordinates}")


    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been destroyed!")

    def repair(self):
        self.health = self.max_health
        print(f"{self.name} has been repaired.")

    def __str__(self):
        return f"{self.name} at coordinates {self.coordinates}, health: {self.health}/{self.max_health}"




class SupportCraft(Vessel):
    SUPPORT_TYPES = ["refueling", "mechanical assistance", "cargo"]

    def __init__(self, name, max_health, coordinates, support_type):
        super().__init__(name, max_health, coordinates)
        
        if support_type.lower() not in self.SUPPORT_TYPES:
            raise ValueError(f"Invalid support_type: {support_type}. Choose from {', '.join(self.SUPPORT_TYPES)}")
        
        self.support_type = support_type
        self.medical_unit = True

    def perform_support_task(self, task):
        print(f"{self.name} is performing {task} support.") 




class OffensiveCraft(Vessel):
    VALID_TYPES = {
        "battleship": 24,
        "destroyer": 12,
        "cruiser": 6
    }

    def __init__(self, name, max_health, coordinates, craft_type):
        super().__init__(name, max_health, coordinates)
        
        if craft_type.lower() not in self.VALID_TYPES:
            raise ValueError(f"Invalid craft_type: {craft_type}. Choose from {', '.join(self.VALID_TYPES.keys())}")
        
        self.craft_type = craft_type
        self.cannon_count = self.VALID_TYPES[craft_type.lower()]
        self.shields_up = False

    def attack(self):
        if self.shields_up:
            print(f"{self.name} is attacking with {self.cannon_count} cannons, but shields are up.")
        else:
            print(f"{self.name} is attacking with {self.cannon_count} cannons!")

    def raise_shields(self):
        self.shields_up = True
        print(f"{self.name}'s shields are raised.")

    def lower_shields(self):
        self.shields_up = False
        print(f"{self.name}'s shields are lowered.")




