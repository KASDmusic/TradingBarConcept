import sys

sys.path.append('../src')

from Product import *


def testNewPriceNormalTradingDelay():
    return True


def testNewPriceNormalTradingRealTime():
    return True


def testNewPriceInverseTradingDelay():
    return True


def testNewPriceInverseTradingRealTime():
    return True



print("testNewPriceNormalTradingDelay : " + str(testNewPriceNormalTradingDelay()))
print("testNewPriceInverseTradingDelay : " + str(testNewPriceInverseTradingDelay()))

print("testNewPriceNormalTradingRealTime : " + str(testNewPriceNormalTradingRealTime()))
print("testNewPriceInverseTradingRealTime : " + str(testNewPriceInverseTradingRealTime()))