#users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
  #      'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
  #      'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}
#Generate a list of usernames, name, age and poison from the above dictionary.


users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
     'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
      'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}


firstDic = users["g91"]
secondDic = users["twir56"]
thirdDic = users["jsdl8"]


# created the keys and values
convertToList = firstDic.keys()
convertedToList = list(convertToList)
print(convertedToList)

#for values
valueList = firstDic.values()
valueToList = list(valueList)
print(valueList)

# created second list
secondConvert = secondDic.keys()
converted = list(secondConvert)
#for values
valueConvert = secondDic.values()
convert = list(valueConvert)

#printing the keys, values
print(converted)
print(convert)

# created third list 
thirdConvert = thirdDic.keys()
thirdConveted = list(thirdConvert)
print(thirdConveted)
# for values
thirdList = thirdDic.values()
thirdListConverted = list(thirdList)
print(thirdListConverted)


