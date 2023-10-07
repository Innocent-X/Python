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
def arranging(A):
    r=A.shape[0] #counting rows
    for i in range(r):
         current_row=0
         for next_row in range(1,r,1):
                index1=get_index(A[current_row, :],current_row)#getting index of current row
                index2=get_index(A[next_row, :],next_row)#getting index of next
                if index1>index2:#replacing if pivot of first is on right
                  replacing=np.copy(A[current_row])
                  A[current_row]=A[next_row]
                  A[next_row]=replacing
                  current_row=next_row#when row is replace its number is change
    
    return A #returning matrix after arranging


#for making leading entry 1
def makingOne(arr,row):
    A=arr[row, :]#row whose leading entry is make to be 1
    colum=len(A)#counting total colum or total entries in a row
    for x in range(colum):
        if A[x]!=0:#making non zero entry 1
            for i in range(colum-1,x-1,-1):#dividing whole row with leading non zero entry
                A[i]=A[i]/A[x]
                arr[ row, : ]=A#changing row in matrix
            return arr #returning matrix      
    return arr#returning orignal matrix in case of zero row     

#for making 0 in next row below 1 
def making_0(arr,current_row):
    r=arr.shape[0]
    c=arr.shape[1]
    for x in range(current_row+1,r,1):
         index1=get_index(arr[current_row,  :],current_row)
         index2=get_index(arr[ x,  :],x)
         if index1==index2:# if there is a non zero entry below one
             for j in range(c-1,-1,-1):#iterating in reverse because the leading entry reamin same till end
                 
                 arr[x,j]=arr[x,j]-arr[current_row,j]*arr[x,index2]#subtracting next row with multiple of their leading entry 
                 
    return arr


#sum of total oprations that to be perform on matrix       
def making_ref(arr):
    r=arr.shape[0]
    for x in range(r-1):
        arr=arranging(arr)
        arr=makingOne(arr,x)
        arr=making_0(arr,x)
    arr=makingOne(arr,r-1)           
    print(arr)
    

arr=np.array([[0,0,3,4],[3,0,0,4]], dtype='f')
making_ref(arr)
              

