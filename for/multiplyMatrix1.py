# Using for loops and print the result.

A = [[1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [111,22,33],
    [44,55,56],
    [47,86,19]
]

result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

 
# iterate through rows of X  
for i in range(len(A)):  
   for j in range(len(B[0])):  
       for k in range(len(B)):  
           result[i][j] += A[i][k] * B[k][j]  
for r in result:  
   print(r)  