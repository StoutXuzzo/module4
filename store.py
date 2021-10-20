global cash
global stock

cash = 1000.

stock = {"1":{"quant": 10,"price":9.99},
        "2":{"quant": 4,"price":19.9},
        "3":{"quant": 0,"price":14.99},
        "4":{"quant": 9,"price":4.99},}

def getPriceProduct(code):
    return stock[code]["price"]

def getQuantyProduct(code):
    return stock[code]["quant"]

def getDetailProduct(code):
    return stock[code]["quant"] + ", " + stock[code]["price"]

def getCash():
    return cash

def addQuantProduct(code, quant):
    if code in stock:
        stock[code]["quant"] += quant
        return True
    else:
        return False

def setPriceProduct(code, price):
    if code in stock:
        stock[code]["price"] = price
        return True
    else:
        return False

def saleProduct(code):
    if code in stock and stock[code]["quant"] > 0:
        return True
    else:
         return False

def replaceProduct(code, quant):
    if not code in stock:
        return False
    price = quant * ((stock[code]["price"] / 100) * 80 )
    if cash >= price:
        return price
    else:
        return False

def getFullStock():
    msj = "Current store status\n==========================\n[Code - Units - Price]"
    for k in stock.keys():
        msj += "\n[" + str(k) + " - " + str(getQuantyProduct(k)) + " - " + str(getPriceProduct(k)) + "]"
    msj += "\nCash: " + str(cash)
    return msj

def menu():
    msj = "1.- Show full store detail\n2.- Sales\n3.- Replace\n4.- Change price of product\n5.- Exit\nSelect option: "
    return msj

while True:
    user = input(menu())
    print("")

    if user == "1":
        print(getFullStock())

    elif user == "2":
        code = input("Enter product code: ")
        if saleProduct(code):
            stock[code]["quant"] -= 1
            cash += stock[code]["price"]
            print("Successfull sale!")
        else:
            print("Error, item does not exist or is out of stock!")

    elif user == "3":
        code = input("Enter product code: ")
        while True:
            quant = input("Units to replace: ")
            if quant.isdigit():
                quant = int(quant)
                break
            else:
                print("This has to be a int!!")

        price = replaceProduct(code, quant)
        if  price != False:
            stock[code]["quant"] += quant
            cash -= price
        else:
            print("There is no cash in the box to replace!")

    elif user == "4":
        code = input("Enter product code: ")
        while True:
            price = input("New price for product: ")
            if price.isdigit():
                price = float(quant)
                break
            else:
                print("This has to be a number!!")
        
        setPriceProduct(code, price)
        print("Updated price!")

    elif user == "5":
        print("Have a nice day!")
        break

    print()