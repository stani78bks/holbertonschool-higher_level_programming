#!/usr/bin/python3
"""Module 7-rectangle : Rectangle avec symboles et compteur d’instances."""


class Rectangle:
    """Classe qui définit un rectangle avec symbole d'affichage personnalisable."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise le rectangle et incrémente le compteur."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter de la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter avec vérification du type et de la valeur."""
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
        """Setter avec vérification du type et de la valeur."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l’aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre, ou 0 si un des côtés vaut 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Affiche le rectangle avec le caractère print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        # ✅ Accès à l’attribut print_symbol correct (checker exige ça)
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Représentation formelle recréable via eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Message lors de la suppression de l'objet."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
