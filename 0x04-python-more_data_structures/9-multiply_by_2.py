#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    r = a_dictionary.copy()
    lists = list(r.keys())
    for i in lists:
        r[i] *= 2
    return (r)
