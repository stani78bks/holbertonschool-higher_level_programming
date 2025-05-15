#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # On vérifie que les deux éléments existent
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError

            # On vérifie que ce sont des nombres (int ou float)
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                raise TypeError

            # On effectue la division
            division = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)
    return result
