#Write a Python program that accepts a hyphen-separated sequence of
#  words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow


items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
