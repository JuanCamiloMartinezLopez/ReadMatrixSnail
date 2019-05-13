import numpy as np

def printFirstNumber(matrix):
    print matrix[0]

def printNumber(matrix):
    printFirstNumber(matrix)

    if len(matrix[1:,:]) is not 0:
        printNumber(np.rot90(matrix[1:, :]))

if __name__=="__main__":
    printNumber(np.array([x.split() for x in open("fichero.txt").readlines()]))
    


