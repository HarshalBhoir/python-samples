# !/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program095:
# Define a class Person and its two child classes: Male and Female. All
# classes have a method "getGender" which can print "Male" for Male class
# and "Female" for Female class.

# Hints:
# Use Subclass(Parentclass) to define a child class.


class Person(object):

    def getGender(self):
        return "Unknown"


class Male(Person):

    def getGender(self):
        return "Male"


class Female(Person):

    def getGender(self):
        return "Female"


def main():
    male = Male()
    female = Female()
    print "male.getGender():", male.getGender()
    print "female.getGender():", female.getGender()


if __name__ == '__main__':
    main()
