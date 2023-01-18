from Product import Product
import random
import time

def writeInFile(productList, directoryPath):

    if not directoryPath.endswith("/"):
            directoryPath = directoryPath + "/"

    f = open("script.js", "r")
    script0 = f.read()
    f.close()

    f = open("index.html", "r")
    index0 = f.read()
    f.close()

    for i in range(len(productList)):

        script = script0.replace("[]", str(productList[i].getListPrices()))

        f2 = open(directoryPath + "script" + str(i+1) + ".js", "w")
        f2.write(script)
        f2.close()

        index = index0.replace("script.js", "script" + str(i+1) + ".js")
        index = index.replace("index.html", "index" + str(i+1) + ".html")

        f2 = open(directoryPath + "index" + str(i+1) + ".html", "w")
        f2.write(index)
        f2.close()


def launchWithHumanDecisions(productList, tradingType):

    while True:

        for i in range(len(productList)):
            if tradingType == NORMAL_TRADING_REAL_TIME:
                productList[i].newPriceNormalTradingRealTime()
            if tradingType == NORMAL_TRADING_DELAY:
                productList[i].newPriceNormalTradingDelay()
            if tradingType == INVERSE_TRADING_REAL_TIME:
                productList[i].newPriceInverseTradingRealTime()
            if tradingType == INVERSE_TRADING_DELAY:
                productList[i].newPriceInverseTradingDelay()
            
            productList[i].buy(int(input("Entrez le nombre acheté de " + productList[i].getName() + " : ")))
        
        for i in range(len(productList)):
            print(productList[i])
            print("-------------------------------")
        
        for cpt in range(5):
            print("")
        
        writeInFile(productList, "./web/")


def launchWithRandomDecisions(productList, tradingType):

    while True:
        for i in range(len(productList)):
            if tradingType == NORMAL_TRADING_REAL_TIME:
                productList[i].newPriceNormalTradingRealTime()
            if tradingType == NORMAL_TRADING_DELAY:
                productList[i].newPriceNormalTradingDelay()
            if tradingType == INVERSE_TRADING_REAL_TIME:
                productList[i].newPriceInverseTradingRealTime()
            if tradingType == INVERSE_TRADING_DELAY:
                productList[i].newPriceInverseTradingDelay()
            
            productList[i].buy(random.randint(0,30))
        
        for i in range(len(productList)):
            print(productList[i])
            print("-------------------------------")
        
        for cpt in range(5):
            print("")
        
        writeInFile(productList, "./web/")

        time.sleep(TIME_STAMP)

if __name__ == "__main__":

	TIME_STAMP = 0.2

	NORMAL_TRADING_REAL_TIME = 0
	NORMAL_TRADING_DELAY = 1
	INVERSE_TRADING_REAL_TIME = 2
	INVERSE_TRADING_DELAY = 3

	productList = []
	productList.append(Product("biere", 7, 9, 3))
	productList.append(Product("vin", 6.5, 9, 3))

	launchWithRandomDecisions(productList, INVERSE_TRADING_DELAY)
	#launchWithHumanDecisions(productList, NORMAL_TRADING_DELAY)

