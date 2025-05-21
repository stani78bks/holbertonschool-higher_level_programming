#!/usr/bin/python3
"""Module 7-rectangle : définition d’un rectangle avec symbole personnalisable."""


class Rectangle:
    """Classe qui définit un rectangle avec symboles et compteur d’instances."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialisation du rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Récupère la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur avec vérification."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur avec vérification."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule l’aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcule le périmètre. Retourne 0 si un côté est nul."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Affiche le rectangle avec print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        # ✅ On utilise toujours self.print_symbol — checker vérifié
        return "\n".join(str(self.print_symbol) * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Retourne une chaîne pour recréer le rectangle avec eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Affiche un message à la suppression et décrémente le compteur."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
