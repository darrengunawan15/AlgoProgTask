from classModule import FancyShoppingDG

def createList():
    itemList = list()

    numFlag = True
    while numFlag == True:
        numOfItems = eval(input("How many items will you order today? "))
        if numOfItems >= 1:
            numFlag = False
        else:
            print("Number of items must be at least 1.")

    # For Loop
    for x in range(numOfItems):
        print(f"Item #{x + 1}-")
        itemName = input("Enter food: ")
        
        qtyFlag = True
        while qtyFlag == True:
            quantity = eval(input("Enter amount of pounds: "))
            if quantity > 0:
                qtyFlag = False
            else:
                print("Amount of pounds must be greater than 0.")

        print("\n")
        buyList = FancyShoppingDG(itemName, quantity)
        itemList.append(buyList)
    return itemList

def displayContent(itemList):
    print("Here's a summary of the items purchased:")
    print("----------------------------------------")
    for item in itemList:
        print(f"Item: {item.getFoodName()}")
        print(f"Amount: {item.getAmtFood()}")
        print(f"Price per pound: ${"{:,.2f}".format(item.getStdPrice())} pounds")
        print(f"Price of order: ${"{:,.2f}".format(item.getCalcPrice())}")
        print("\n")

def calculateTotal(itemList):
    totalCost = 0
    for item in itemList:
        totalCost += item.getCalcPrice()
    return totalCost

def main():
    myList = createList()
    displayContent(myList)
    print(f"Total cost: ${"{:,.2f}".format(calculateTotal(myList))}")

main()