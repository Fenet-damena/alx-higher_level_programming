#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    s = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            s.append(True)
        else:
            s.append(False)
    return (s)
