C = [[111,22,33,44],  
       [44,55,56,1],  
       [47,86,19, 2],
       [1,2,22,3]
       ]  
 
D = [[11,22,3,4],  
      [4,5,6,1],  
      [7,6,19,2] ,
      [1,2,22,3]
]
 
result = [[0,0,0,0],  
               [0,0,0,0],  
              [0,0,0,0],
              [0,0,0,0]
              ]  
 
# iterate through rows of X  
for i in range(len(C)):  
   for j in range(len(C[0])):  
       for k in range(len(C)):  
           result[i][j] += C[i][k] * D[k][j]  
for r in result:  
   print(r)  