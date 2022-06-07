#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_divide = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            check_divide.append(True)
        else:
            check_divide.append(False)

    return (check_divide)
