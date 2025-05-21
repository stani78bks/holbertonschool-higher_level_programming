#!/usr/bin/python3
"""Module 7-rectangle : définition d'un rectangle avec print_symbol personnalisable."""


class Rectangle:
    """Classe qui définit un rectangle avec symbole personnalisable."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise un rectangle et incrémente le nombre d’instances."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter de la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter de la largeur avec vérification."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter de la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter de la hauteur avec vérification."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle.
        Si la largeur ou la hauteur est 0, retourne 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Affiche le rectangle avec print_symbol.
        Retourne une chaîne vide si largeur ou hauteur vaut 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Retourne une chaîne permettant de recréer l'objet avec eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Affiche un message à la suppression de l'objet et décrémente le compteur."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
