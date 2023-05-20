from abc import ABC

from models.plate import Plate


class DinnerPlate(Plate, ABC):
    def getMaxFoodWeight(self):
        pass

    def __str__(self):
        return f"Diameter: {self.diameter}\n" \
               f"Material: {self.material}\n" \
               f"Color: {self.color}\n" \
               f"is_clean: {self.is_clean}\n" \
               f"has_food: {self.has_food}\n"

