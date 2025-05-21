#!/usr/bin/python3
"""Module 7-rectangle: Rectangle avec symbole personnalisé et compteur d’instances."""


class Rectangle:
    """Classe qui définit un rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec largeur et hauteur."""
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
        """Retourne l’aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne le rectangle sous forme de chaîne avec print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        # ✅ Utilisation correcte de print_symbol (par instance ou classe)
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Retourne une chaîne pour recréer l'objet avec eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Affiche un message lors de la suppression et décrémente le compteur."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
