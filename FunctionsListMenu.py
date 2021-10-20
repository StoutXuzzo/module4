msjNumber = "Insert a number:"
msjPosition = "Insert a position:"
msjError = "You have to insert a number."
list = []

def showMenu():
    print("\nMENU")
    print("---------------------------------------------------------")
    print("1.- Add a number to the list.")
    print("2.- Add a number in a position in the list.")
    print("3.- Show the length of the list.")
    print("4.- Delete the last number in the list.")
    print("5.- Delete a number in the list.")
    print("6.- Count numbers.")
    print("7.- Positions of a numbers.")
    print("8.- Show the list.")
    print("9.- Exit.")
    print("---------------------------------------------------------")
    return input("\nSelect an option: ")


def insertNumber(msj = ""):
    num = input(msj)
    if num.isdigit():
        num = int(num)
        return num
    else:
        return False

def option7(list = []):
    postList = []
    num = insertNumber(msjNumber)

    if num == False:
        print(msjError)
    else:
        for i in range(len(list)):
            if num == list[i]:
                postList.append(i+1)
        return postList

while True:
    
    option = showMenu()

    if option == "1":

        num = insertNumber(msjNumber)
        if num == False:
            print(msjError)
        else:
            list.append(num)


    elif option == "2":

        num = insertNumber(msjNumber)
        pos = insertNumber(msjPosition)

        if num == False:
            print(msjError)
        else:
            list.insert(pos-1, num)
            if pos - 1 > len(list):
                print("That position dosn't exist, the number was added to the last position.")

    elif option == "3":

        print("The list is", len(list), "numbers long.")

    elif option == "4":

        if len(list) > 0:
            print("The last element in the list:", list[-1])
            del list[-1]
        else:
            print("The list is empty.")

    elif option == "5":

        pos = insertNumber(msjPosition)

        if pos == False:
            print(msjError)
        else:
            if num > len(list):
                print("This position does not exist.")
            else:
                print("The deleted value is", list[num-1])
                del list[num-1]
    
    elif option == "6":
        
        num = insertNumber(msjNumber)
        if num == False:
            print(msjError)
        else:
            cont = 0
            for listNum in list:
                if listNum == num:
                    cont += 1
            print("Your number is", cont, "times in the list.")

    elif option == "7":

        postList = option7(list)
        if len(postList) > 0:
            print("The number is in the next positions:", postList)
        else:
            print("The number isn't in the list.")

    elif option == "8":

        print("Values of the list:", list)

    elif option == "9":

        print("That's All Folks!")
        break

    else:
        print("Please, select a valid option.")