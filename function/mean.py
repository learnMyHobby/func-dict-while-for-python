#Write three different functions to calculate the mean, variance
#  and standard deviation of the following data.You need to call your
#  mean function to within your variance and standard deviation functions.

import math
import statistics

myDict = {
    'Richard' : 24,
    'Lara' : 36,
    'Prava' :  45,
    'Peter' : 45,
    'Judas' : 96,
    'Jimmy' : 56,
    'Jimi' : 89,
    'Ronaldo' : 12,
    'Messi'  : 10,
    'Pogba' : 100
}

totalNumbers = myDict.values()
sumOfNumbers = sum(totalNumbers)  # this statement adds all the marks of the student
countValues = len(myDict) # this counts the total number of students

print(f"There are {countValues} students  in the list ")  
print("The sum of the marks of all the students is ", sumOfNumbers) 

def mean():
    addNumbers = sumOfNumbers / countValues
    print("The mean of the all the student is {}".format(addNumbers))
mean()

def toVariance():
    findVariance = statistics.variance(totalNumbers)
    print("The variance of the numbers are", findVariance)
toVariance()


def forStanDev():
    findStanDev = statistics.stdev(totalNumbers)
    print("The standard deviation of the numbers is ", findStanDev)
forStanDev()



