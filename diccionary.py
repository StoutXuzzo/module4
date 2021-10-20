dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print("Dictionaris are like objects in Java, you can asign keys and values:")

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
print()
print("You can use the key to get the value:")
print(phone_numbers["boss"])
print()
print("Ofcourse, you can do a loop to show all the dictionary:")
for e in dictionary:
    print(e, dictionary[e])
print()
print("You have diferent metods for the dictionary:")
for e in dictionary.items():
    print(e)
print("You can also do this, to get the values individualy:")
for k, v in dictionary.items():
    print(k, v)

print("You can change or add a value, with the key:")
dictionary["cat"] = "small"
print(dictionary["cat"])
print("You can also use the .update() metod:")
dictionary.update({"bear":"big mf"})
print(dictionary["bear"])

print("To delete an item, you can use 'del':")
del dictionary["horse"]
print("or you can use the .pop() metod:")
print(dictionary.pop("dog"))
