#program to check a matrix wheter it is in echelon form if not convert it into echelon form 
#author Saifullah
#october 06,2023
#venue Home Sweet Home
"""
process for converting a matrix in echeloon form
There are basically four steps in creating a row echelon matrix
Step 1: Finding pivot entry index of rows
Step 2: Arranging them according to their index
Step 3: Make leading entry 1
Step 4: making 0 below if there is any nonzero entry  
"""
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


#function for arranging matrix according to pivot index
def arranging(A,row):
    r=A.shape[0] #counting rows
    current_row=row
    for next_row in range(row+1,r,1):
        index1=get_index(A[current_row,],current_row)#getting index of current row
        index2=get_index(A[next_row,],next_row)#getting index of next row
        if index1>index2:#replacing if pivot of first is on right
                  replacing=np.copy(A[current_row])
                  A[current_row]=A[next_row]
                  A[next_row]=replacing
                  
    return A #returning matrix after arranging


#for making leading entry 1
def makingOne(arr,row):
    A=arr[row,]#row whose leading entry is make to be 1
    colum=len(A)#counting total colum 
    for x in range(colum):
        if A[x]!=0:    #finding non zero entry 
            A=A/A[x]      #making leading entry 1 by dividing whole row by it
            arr[row,]=A   #replacing row in real matrix
            return arr  #returning matrix      
    return arr#returning orignal matrix in case of zero row     

#for making 0 in next row below 1 
def making_0(arr,current_row):
    r=arr.shape[0]
    for x in range(current_row+1,r,1):#for traversing through next rows
         index1=get_index(arr[current_row,],current_row)
         index2=get_index(arr[x,],x)
         if index1==index2:# if there is a non zero entry below one
            arr[x,]=arr[x,]-arr[current_row,]*arr[x,index2] 
    return arr


#sum of total oprations that to be perform on matrix       
def making_ref(arr):
    r=arr.shape[0]
    if r==0 or r==1: #for null and row marix
        return arr
    
    for x in range(r):
        arr=arranging(arr,x)
        arr=makingOne(arr,x)
        arr=making_0(arr,x)
    return arr
    
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

#main function    
A=isEchelon(matrix)
if A==0:#if matrix is no in echelon
    print("The Echelon of matrix is as follow")
    matrix=making_ref(matrix)
    print(matrix)


             

