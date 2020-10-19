import os
from sys import argv


# this function return correct solution value from graph in txt

def good_solution(name):
    with open(name, 'r') as file:
        line = file.readline()
        return line.split()[-1]


''' in this function we give as argument function to test, and we have 
    true as result if function return the same result as we have in graph file,
    or false in other cases.'''


def testing(function):
    directory = argv
    directory = str(directory)
    directory = directory[2:-9] + "Graf"
    for i in os.listdir(directory):
        if int(good_solution("Graf/" + i)) != int(function("Graf/" + i)):
            good_solution("Graf/" + i)
            return False
    return True
