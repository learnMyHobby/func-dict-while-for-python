# Dream Vacation: Write a program that polls users about their dream vacation. Write 
# a prompt similar to If you could visit one place in the world, where would you go?
#  Include a block of code that prints the results of the poll.

poll = {}
while True:
    name = input('What is your name? ')
    choice = input('If you could visit one place in the world, where would you go? ') 
    another_choice = input("Would you like to ask more people? ")
    poll[name.title()] = choice.title()
    if another_choice == 'no':
       break
    
print("-----Poll Results----")   
for x, y in poll.items():
    print("{}'s favorite destination is {} ".format(x, y))
    