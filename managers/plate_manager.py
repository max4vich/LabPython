from models.dessert_plate import DessertPlate
from models.dinner_plate import DinnerPlate
from models.salad_plate import SaladPlate
from models.soup_plate import SoupPlate


class PlateManager:
    plates = []

    def add_plate(self, plate):
        self.plates.append(plate)

    def find_all_plates_with_diameter_greater_than(self, diameter):
        return [plate for plate in self.plates if plate.diameter > diameter]

    def find_all_plates_made_from_glass(self):
        return [plate for plate in self.plates if plate.material == "glass"]

    @staticmethod
    def main():
        manager = PlateManager()

        manager.add_plate(SaladPlate(8, "porcelain", "white", True, False, "round", True))
        manager.add_plate(SaladPlate(9, "glass", "black", True, True, "oval", False))

        manager.add_plate(SoupPlate(12, "glass", "white", True, False, 5, "Tomato Soup"))
        manager.add_plate(SoupPlate(10, "ceramic", "green", True, False, 5, "Tomato Soup"))

        manager.add_plate(DinnerPlate(11, "porcelain", "pink", True, False))
        manager.add_plate(DinnerPlate(9, "glass", "black", True, True))

        manager.add_plate(DessertPlate(6, "porcelain", "pink", False, False))
        manager.add_plate(DessertPlate(7, "ceramic", "white", False, True))

        for plate in manager.plates:
            print(str(plate))

        print("\nDef: find_all_plates_with_diameter_greater_than(10)\n")
        filtered_plates = manager.find_all_plates_with_diameter_greater_than(10)
        for plate in filtered_plates:
            print(str(plate))

        print("\nDef: find_all_plates_made_from_glass\n")
        filtered_plates = manager.find_all_plates_made_from_glass()
        for plate in filtered_plates:
            print(str(plate))


PlateManager.main()
