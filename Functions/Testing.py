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

#######################################################################

'''This function testing graphs function with txt files in folder Graphs/dir dir - is given as argument of 
this function. Function returns name of file and result of test True if passed False otherwise.Graph in txt nead
to have correct answer in the first line. Example txt file is graphs/flow/simple.txt
'''


def testing(function, dir):
    directory = argv
    directory = str(directory)
    directory = directory[2:-14] + "graphs/" + dir + "/"
    print(directory)
    result = True
    for i in os.listdir(directory):
        print(i, end=" ")
        actual = int(function(directory + i))
        if int(good_solution(directory + i)) != actual:
            print("correct", good_solution(directory + i), "yours",actual,end=" ")
            print(False)
            result = False
        else:
            print(True)
    return result
