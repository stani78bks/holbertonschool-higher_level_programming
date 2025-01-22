#!/usr/bin/env 
def fizzbuzz():
    for number in range (1, 101):
        if number % 3 == 0 and number % 5 == 0:
            if number != 100:
                print ("FizzBuzz",end=" ")
            else:
                print ("FizzBuzz",end="")

        elif number % 3 == 0:
            if number != 100:
                print ("Fizz", end=" ")
            else:
                print ("Fizz", end="")

        elif number % 5 == 0:
            if number != 100:
                print ("Buzz", end=" ")
            else:
                print ("Buzz", end="")

        else:
            if number != 100:
                print (number, end=" ")
            else:
                print (number, end="")
