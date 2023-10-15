#program to convert a matrix in row echelon form
#author Saifullah
#october 06,2023
#venue Home Sweet Home
"""
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
    return i+row#in case of zero row


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
    for x in range(current_row+1,r,1):
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
    
    for x in range(r-1):
        arr=arranging(arr,x)
        arr=makingOne(arr,x)
        arr=making_0(arr,x)
    arr=makingOne(arr,r-1)           
    return arr
    

arr=np.array([[0,0,0],[0,2,6],[8,0,0]], dtype='f')

arr=making_ref(arr)
print(arr)

#if you find any error feel comfortable to tell             

