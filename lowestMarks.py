# Students = [‘jack’,’jill’,’david’,’silva’,’ronaldo’]
# Marks = [‘55’,’56’,’57’,’66’,’76’]
# Make a dictionary using lists above and delete the key-value (students:marks) pairs with lowest marks. 

# making a  dictionary

myDict = {
    'jack' : '55',
    'jill' : '56',
    'david': '57',
    'silva' : '66',
    'ronaldo': '76'
}

del myDict['jack']
print(myDict)

