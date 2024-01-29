#!/usr/bin/python3
""" This the module for square class"""


class Square():
    """ The square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ The nstantiation of class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of my square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Printable representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ It creates square object """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
