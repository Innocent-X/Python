#program to check a matrix wheter it is in echelon form 
#author Saifullah
#october Oct 17,2023
#venue  Home
import numpy as np#for working with arrays

# function for getting pivot entry index
def get_index(a,row):
    for i in range (len(a)):
        if a[i]!=0:
            return i
    return i+row+1#in case of zero row and adding 1 in case if it is a colum matrix

#for getting array of idexes of rows
def get_index_array(A):
    r=A.shape[0]
    array=np.zeros(r)
    for x in range(r):
        array[x]=get_index(A[x,],x)
    return array

#function for finding wheter the given matix is in echelon form
def isEchelon(matrix):
    A=get_index_array(matrix)
    for x in range(len(A)-1):
        if A[x+1]<=A[x]:
            print("Matrix is not in echelon form.")
            return 0
        
    print("Matrix is in echelon form.")
    return 1     

#main function
#taking input from user
while(1):#for user input validation 
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    if rows == 0 and cols == 0:#for null matrix
          break
    if rows > 0 and cols > 0:
          break
    else:
        print("Invalid matrix dimensions. Rows and columns must be greater than zero or both 0")  
matrix = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        element = float(input("Enter the value for element at (" + str(i) + ", " + str(j) + "): "))
        matrix[i, j] = element

isEchelon(matrix)#calling function