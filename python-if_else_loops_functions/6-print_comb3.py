#!/usr/bin/python3


for number in range(0, 10):
    for second_number in range(number + 1, 10):
        if number == 8 and second_number == 9:
            print("{}{}".format(number, second_number))
        else:
            print("{}{}".format(number, second_number), end=", ")
