from models.dessert_plate import DessertPlate
from models.dinner_plate import DinnerPlate
from models.salad_plate import SaladPlate
from models.soup_plate import SoupPlate


class PlateManager:
    """
    A class used to manage a collection of Plate objects.

    Attributes:
        plates (list): A list of Plate objects.
    """
    plates = []

    def add_plate(self, plate):
        """
        Adds a Plate object to the plates list.

        Args:
            plate (Plate): The Plate object to be added.
        """
        self.plates.append(plate)

    def find_all_plates_with_diameter_greater_than(self, diameter):
        """
        Finds all Plate objects in the plates list with a diameter greater than the specified value.

        Args:
            diameter (float): The diameter value to compare against.

        Returns:
            list: A list of Plate objects with a diameter greater than the specified value.
        """
        return list(filter(lambda plate: plate.diameter > diameter, self.plates))

    def find_all_plates_made_from_glass(self):
        """
        Finds all Plate objects in the plates list made from glass.

        Returns:
            list: A list of Plate objects made from glass.
        """
        return list(filter(lambda plate: plate.material == "glass", self.plates))

    @staticmethod
    def main():
        """
        The main method of the PlateManager class. Demonstrates the usage of the class and its methods.
        """
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
