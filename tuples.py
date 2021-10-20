myTuple = (1, 2, 3, 4, 5)

print("A tuple is like a list, but you can not change the values:\n")
print("You can print it directly:")
print(myTuple, "\n")

print("You also can print it with a loop: ")
for i in myTuple:
    print(i, " ")
print()

print("And you can use \"[]\" to print a position:")
print(myTuple[1])
print(myTuple[-1])
print()

print("This is the resulta of: 'myTuple * 3' ")
print(myTuple * 3)
# myTuple[0] = 200 --> Error, you cant change the values of a tuple.

