class Product:

    def __init__(self, name, price, maxPrice, minPrice):
        self.name = name
        self.price = price
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.listPrices = [self.price]
        self.listQuantitySolded = [0]

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price

    def getMinPrice(self):
        return self.minPrice
    
    def getMaxPrice(self):
        return self.maxPrice

    def getListPrices(self):
        return self.listPrices


    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def setMinPrice(self, minPrice):
        self.minPrice = minPrice
    
    def setMaxPrice(self, maxPrice):
        self.maxPrice = maxPrice


    #V1
    #A finir erreur ? (oui, faire augm const 5% de max-min)
    '''
    def newPrice(self):

        if len(self.listPrices) >= 2:
            lastEarn = self.listPrices[len(self.listPrices) - 1] * self.listQuantitySolded[len(self.listQuantitySolded) - 1]
            last2Earn = self.listPrices[len(self.listPrices) - 2] * self.listQuantitySolded[len(self.listQuantitySolded) - 2]
            earn = lastEarn - last2Earn
            
            if earn > 0:
                if round(self.price - ((self.maxPrice - self.minPrice) * 0.05), 2) >= self.minPrice:
                    self.price = round(self.price - ((self.maxPrice - self.minPrice) * 0.05), 2)
            if earn < 0:
                if round(self.price + ((self.maxPrice - self.minPrice) * 0.05), 2) <= self.maxPrice:
                    self.price = round(self.price + ((self.maxPrice - self.minPrice) * 0.05), 2)

        self.listPrices.append(self.price)
        self.listQuantitySolded.append(0)
    '''
    def newPriceNormalTradingDelay(self):

        if len(self.listPrices) >= 2:
            obj = 10
            if len(self.listPrices) < obj:
                nbIter = len(self.listPrices)
            else:
                nbIter = 10

            #nbIter = len(self.listPrices)

            lastEarn = 0
            for i in range(nbIter):
                lastEarn += self.listPrices[len(self.listPrices)-i-1] * self.listQuantitySolded[len(self.listQuantitySolded)-i-1]
            lastEarn = lastEarn/nbIter

            last2Earn = 0
            for i in range(nbIter-1):
                last2Earn += self.listPrices[len(self.listPrices)-i-2] * self.listQuantitySolded[len(self.listQuantitySolded)-i-2]
            last2Earn = last2Earn/(nbIter-1)

            earn = lastEarn - last2Earn
            print(lastEarn)
            print(last2Earn)
            print(earn)
            
            if earn > 0:
                if round(self.price + ((self.maxPrice - self.minPrice) * 0.05), 3) >= self.minPrice:
                    self.price = round(self.price + ((self.maxPrice - self.minPrice) * 0.05), 3)
                    
            else:
                if round(self.price - ((self.maxPrice - self.minPrice) * 0.05), 3) <= self.maxPrice:
                    self.price = round(self.price - ((self.maxPrice - self.minPrice) * 0.05), 3)
                    
        self.listPrices.append(self.price)
        self.listQuantitySolded.append(0)

    
    def newPriceNormalTradingRealTime(self):

        if len(self.listPrices) >= 2:
            obj = 10
            if len(self.listPrices) < obj:
                nbIter = len(self.listPrices)
            else:
                nbIter = 10

            #nbIter = len(self.listPrices)

            lastEarn = 0
            for i in range(nbIter):
                lastEarn += self.listPrices[len(self.listPrices)-i-1] * self.listQuantitySolded[len(self.listQuantitySolded)-i-1]
            lastEarn = lastEarn/nbIter

            last2Earn = 0
            for i in range(nbIter-1):
                last2Earn += self.listPrices[len(self.listPrices)-i-2] * self.listQuantitySolded[len(self.listQuantitySolded)-i-2]
            last2Earn = last2Earn/(nbIter-1)

            earn = lastEarn - last2Earn
            print(lastEarn)
            print(last2Earn)
            print(earn)
            
            if earn > 0:
                if round(self.price + ((self.maxPrice - self.minPrice) * 0.05), 3) >= self.minPrice:
                    self.price = round(self.price + ((self.maxPrice - self.minPrice) * 0.05), 3)
                    
            else:
                if round(self.price - ((self.maxPrice - self.minPrice) * 0.05), 3) <= self.maxPrice:
                    self.price = round(self.price - ((self.maxPrice - self.minPrice) * 0.05), 3)
                    
        self.listPrices.append(self.price)
        self.listQuantitySolded.append(0)


    #V2
    def newPriceInverseTradingDelay(self):

        if len(self.listPrices) >= 2:
            obj = 10
            if len(self.listPrices) < obj:
                nbIter = len(self.listPrices)
            else:
                nbIter = 10

            #nbIter = len(self.listPrices)

            lastEarn = 0
            for i in range(nbIter):
                lastEarn += self.listPrices[len(self.listPrices)-i-1] * self.listQuantitySolded[len(self.listQuantitySolded)-i-1]
            lastEarn = lastEarn/nbIter

            last2Earn = 0
            for i in range(nbIter-1):
                last2Earn += self.listPrices[len(self.listPrices)-i-2] * self.listQuantitySolded[len(self.listQuantitySolded)-i-2]
            last2Earn = last2Earn/(nbIter-1)

            earn = lastEarn - last2Earn
            print(lastEarn)
            print(last2Earn)
            print(earn)
            
            if earn > 0:
                if round(self.price - ((self.maxPrice - self.minPrice) * 0.05), 3) >= self.minPrice:
                    self.price = round(self.price - ((self.maxPrice - self.minPrice) * 0.05), 3)
                    
            else:
                if round(self.price + ((self.maxPrice - self.minPrice) * 0.05), 3) <= self.maxPrice:
                    self.price = round(self.price + ((self.maxPrice - self.minPrice) * 0.05), 3)
                    
        self.listPrices.append(self.price)
        self.listQuantitySolded.append(0)
        

    def buy(self, quantity):
        self.listQuantitySolded[len(self.listQuantitySolded)-1] += quantity

    
    def __str__(self):
        res = "name:" + self.name + " | Price:" + str(self.price) + " | minPrice:" + str(self.minPrice)
        res += "\n" + "listPrices:" + str(self.listPrices)
        res += "\n" + "listQuantitySolded:" + str(self.listQuantitySolded)
        
        benef = 0
        for i in range(len(self.listPrices)):
            benef += (self.listPrices[i] - self.minPrice) * self.listQuantitySolded[i]
        
        res += "\n" + "benefices:" + str(benef)
        
        return res


'''
if __name__ == "__main__":
	test = Product("test", 8, 5)
	print(str(test))
	test.newPrice()
	print(str(test))
'''
