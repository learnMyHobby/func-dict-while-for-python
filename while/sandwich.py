# Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches . Loop through the list of sandwich
#  orders and print a message for each order, such as I made your tuna sandwich. As each 
# sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

#made a list with various sandwiches
sandwich_orders = ['Pork Roll','Chacarero','Ham Biscuits','Barros Luco']
number_0f_sandwiches = len(sandwich_orders)

#created the empty list
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made a " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich + " is done\n")



