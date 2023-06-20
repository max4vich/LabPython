"""
A class that represents exceptions
"""


class ColorError(Exception):
    """
    A custom exception class for invalid colors.

    Attributes:
        color: The invalid color value that caused the exception.
        message: The error message to display. Defaults to "Color must be a valid string".

    Methods:
        __str__: Returns a string representation of the exception.
    """

    def __init__(self, color, message="Color must be a valid string"):
        self.color = color
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.color} -> {self.message}"


class MaterialError(Exception):
    """
    A custom exception class for invalid materials.

    Attributes:
        material: The invalid material value that caused the exception.
        message: The error message to display. Defaults to "Material must be 'glass'".

    Methods:
        __str__: Returns a string representation of the exception.
    """

    def __init__(self, material, message="Material must be 'glass'"):
        self.material = material
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.material} -> {self.message}"
