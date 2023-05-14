class Plate:
    instance = None

    def __init__(self, diameter=None, material=None, color=None, is_clean=None, has_food=None):
        """
        Initialize a Plate instance.

        Args:
            diameter (float): The diameter of the plate.
            material (str): The material of the plate.
            color (str): The color of the plate.
            is_clean (bool): Whether the plate is clean or not.
            has_food (bool): Whether the plate has food on it or not.
        """
        self.__diameter = diameter
        self.__material = material
        self.__color = color
        self.__is_clean = is_clean
        self.__has_food = has_food

    def wash(self):
        """Set the is_clean attribute to True."""
        self.__is_clean = True

    def dirty(self):
        """Set the is_clean attribute to False."""
        self.__is_clean = False

    def eat(self):
        """Set the has_food attribute to False and call the dirty method."""
        self.__has_food = False
        self.dirty()

    def add_food(self):
        """Set the has_food attribute to True."""
        self.__has_food = True

    def __str__(self):
        """Return a string representation of the Plate instance."""
        return f"Diameter: {self.__diameter}\n" \
               f"Material: {self.__material}\n" \
               f"Color: {self.__color}\n" \
               f"is_clean: {self.__is_clean}\n" \
               f"has_food: {self.__has_food}\n"

    @staticmethod
    def get_instance():
        """
        Get a singleton instance of the Plate class.

        Returns:
            Plate: The singleton instance of the Plate class.
        """
        if Plate.instance is None:
            Plate.instance = Plate()
        return Plate.instance


if __name__ == "__main__":
    plates = [
        Plate(),
        Plate(5, "ceramic", "white", True, False),
        Plate.get_instance(),
        Plate.get_instance()
    ]

    for i, plate in enumerate(plates):
        print(i + 1)
        print(str(plate))
