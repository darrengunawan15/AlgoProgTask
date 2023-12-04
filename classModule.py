class FancyShoppingDG:
    def __init__(self, foodName, amtFood):
        self.__foodName = foodName
        self.__amtFood = amtFood 
        self.__stdFoodPrice = 0
        self.__calcFoodPrice = 0
        self.__priceList()
        self.calculateFood()

    def getFoodName(self):
        return self.__foodName
    
    def getAmtFood(self):
        return self.__amtFood

    def getStdPrice(self):
        return self.__stdFoodPrice

    def getCalcPrice(self):
        return self.__calcFoodPrice

    def __priceList(self):
        match self.__foodName:
            case 'Dry Cured Iberian Ham':
                self.__stdFoodPrice = 177.80

            case  'Wagyu Steaks':
                self.__stdFoodPrice = 450.00

            case  'Matsutake Mushrooms':
                self.__stdFoodPrice = 272.00

            case  'Kopi Luwak Coffee':
                self.__stdFoodPrice = 306.50

            case  'Moose Cheese':
                self.__stdFoodPrice = 487.20

            case  'White Truffles':
                self.__stdFoodPrice = 3600.00

            case  'Blue Fin Tuna':
                self.__stdFoodPrice = 3603.00

            case  'Le Bonnotte Potatoes':
                self.__stdFoodPrice = 270.81

            case _:
                self.__stdFoodPrice = 0.00
    
    def calculateFood(self):
        total = self.__amtFood * self.__stdFoodPrice
        self.__calcFoodPrice = total
        return self.__calcFoodPrice
    
    def __str__(self):
        print("This is not my food?")