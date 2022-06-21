#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)

    lengthy = len(my_list)

    if idx > lengthy - 1:
        return (None)

    return(my_list[idx])
