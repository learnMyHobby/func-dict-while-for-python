# Create an empty dictionary called milk_carton. Add the following key/value pairs.You 
# can make up the values or use a real milk carton.
# Expiration_date: a tuple with day, month, year
# Vol: volume of milk 
# Cost: cost of milk
# Brand_name

milk_carton = {
    'Hiland' :{'date' : (7,21,2021), 'volume' : '5 litres', 'cost': 5}
}

#printing out the values in the dictionary
for values in milk_carton.values():
    costOfMilk = values
    print(costOfMilk)

costInDollars = int(costOfMilk['cost'])

# prints out the cost for 6 milk cartons
costOf6Cartons = 6 * costInDollars 
print(f"The costOf6Cartons is {costOf6Cartons} dollars")





