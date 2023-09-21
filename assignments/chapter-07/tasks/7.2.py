##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/??/2023                   #
# Filename: 7.2.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

class Stock:
    def __init__(self, name, symbol, previousClosingPrice, currentPrice):
        self.__name: str = name
        self.__symbol: str = symbol
        self.__previousClosingPrice: float = previousClosingPrice
        self.__currentPrice: float = currentPrice

    def get_name(self):
        return self.__name
    def get_symbol(self):
        return self.__symbol
    def get_previousClosingPrice(self):
        return self.__previousClosingPrice
    def get_currentPrice(self):
        return self.__currentPrice
    def set_previousClosingPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice
    def set_currentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):
        return (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice * 100

    def __str__(self):
        return (f"Stock: {self.__name} ({self.__symbol})\n"
                f"Previous Closing Price: {self.__previousClosingPrice}\n"
                f"Current Price: {self.__currentPrice}\n"
                f"Change: {self.getChangePercent()}%")


stock = Stock("Intel Corporation", "INTC", 20.5, 20.35)
print(stock)