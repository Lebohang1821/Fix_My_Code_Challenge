#!/usr/bin/python3

class Square():
    
    def __init__(self, width=0, height=0, *args, **kwargs):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Area of the square."""
        return self.width * self.width

    def perimeter_of_my_square(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
