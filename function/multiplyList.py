# Write a Python function to multiply all the numbers in a list.




def multiplyNumbers(listing):
    result = 1
    for i in listing:
        result = result * i
    return result

numbers = [3,4,5,2,5]
print(multiplyNumbers(numbers))


        

