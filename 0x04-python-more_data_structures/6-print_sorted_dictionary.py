#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ = list(a_dictionary.keys())
    list_.sort()
    for i in list_:
        print("{}: {}".format(i, a_dictionary.get(i)))
