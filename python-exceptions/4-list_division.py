#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                print("wrong type")
                division = 0
            else:
                division = val1 / val2
        except IndexError:
            print("out of range")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        finally:
            result.append(division)
    return result
