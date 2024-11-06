myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
myFruitList[2] = "orange"
print(myFruitList)

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

#TUPLE
myFinalAnswerTuple = ("apple", "banana", "pineapple",4)  # tuple bisa terdiri dari data type yg berbeda
#index (+)               0        1           2      3
#index (-)              -4       -3          -2     -1
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[-2])
print(myFinalAnswerTuple[0:2])
print(myFinalAnswerTuple[1:])
print(myFinalAnswerTuple[:3])

myFinalAnswerTuple[3]="manggo"    #tuple itu imuteable, duplikat element boleh 
print(myFinalAnswerTuple)