#program to convert a matrix in reduce row echelon form
#author Saifullah
#october 16,2023
#venue Home 
"""
There are basically 5 steps in creating a row echelon matrix
Step 1: Finding pivot entry index of rows
Step 2: Arranging them according to their index
Step 3: Make leading entry 1
Step 4: making 0 below if there is any nonzero entry
Step 5: making 0 above 1 if there is any nonzero entry 
"""
import numpy as np#for working with arrays

# function for getting pivot entry index
def get_index(a,row):
    for i in range (len(a)):
        if a[i]!=0:
            return i
    return i+row+1#in case of zero row and adding 1 in case if it is a colum matrix


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

#function for making 0 aboe 1 for
def makingAbove_0(A,row):
    index1=get_index(A[row,],row)#getting colum no. in which 1 exit
    for x in range(row):#for traversing each row
       if A[x,index1]!=0:#ther is nosero element above 1
         A[x,]= A[x,]-A[row,]*A[x,index1]
        
    return A


#sum of total oprations that to be perform on matrix       
def reduce_REF(arr):
    r=arr.shape[0]
    if r==0 or r==1: #for null and row marix
        return arr
    
    for x in range(r):
        arr=arranging(arr,x)
        arr=makingOne(arr,x)
        arr=making_0(arr,x)
    for x in range(r-1,0,-1):#for making non zero enteries above 1 0 
        arr=makingAbove_0(arr,x)
    
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
        element = float(input(f"Enter element at position ({i}, {j}): "))
        matrix[i, j] = element
    

matrix=reduce_REF(matrix)
print("Matrix reduce Echelon form is as follow:")
print(matrix)

