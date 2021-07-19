
       #       F
        #      F F F
          #    F F F F F
          #    F F F F F F
           #   F F F F F F F F F
            #  F F F F F F F F F F F


current = "f" 
stop = 2
rows = 6  # Number of rows to print numbers
for i in range(rows):
    for j in range(1, stop):
        print(current , end=' ')
    print("")
    stop += 2

