#!/usr/bin/python3
""" The user class"""


class User():
    """ Documentations """

    def __init__(self):
        """ Documentations """
        self.__email = None

    @property
    def email(self):
        """ The doc """
        return self.__email

    @email.setter
    def email(self, value):
        """ The doc """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

  
    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
