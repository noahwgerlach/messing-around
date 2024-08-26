#Noah Gerlach, 1A
#This code requires the packages "yfinance", "setuptools", "lxml", and "html5lib".

import yfinance as yf
import pandas as pd
from decimal import Decimal
#This while-True loop asks the user to input a Stock Ticker.
#The Ticker is then verified with the Try-Except pair.
#If the Ticker does not exist, then it will re-prompt the user to input a new Ticker
while True:
        stocknameraw = str(input("Which stock would you like to look at? (Stock Ticker) "))
        stockname = stocknameraw.upper()
        stock = yf.Ticker(stockname)
        try:
                str(stock.info.get("shortName"))
                break
        except IndexError:
                print("That is not an existing stock ticker.")
        except ValueError:
                print("That is not an existing stock ticker.")
        except KeyError:
                print("That is not an existing stock ticker.")

print("Retrieving data for "+stock.info.get("shortName")+" ("+stockname+")...")

#This block of code creates a list to check inputed dates against.
history = stock.history(period="max", actions=False)
testlist = []
for i in range(0,len(history)):
        x = history[i:(i+1)]
        y = x.index[0]
        z = y.date()
        testlist.append(z)
#This while-True loop checks the dates inputed have useable data attached.
while True:
        date2check = str(input("What date would you like to invest at? (YYYY-MM-DD) "))
        success = 0
        while success == 0:
                for i in range(0,len(history)):
                        if str(testlist[i]) == date2check:
                                date = date2check
                                success = 1
                                break
                break
        if success == 1:
                break
        else:
                print("Sorry, that is not a valid date.")
#This loop also checks for a valid date, also checking it is later than the first date inputed.
while True:
        date2check2 = str(input("What date would you like withdraw your investment? (YYYY-MM-DD) "))
        success2 = 0
        while success2 == 0:
                for i in range(0,len(history)):
                        if str(testlist[i]) == date2check2 and date2check2 > date:
                                date2 = date2check2
                                success2 = 1
                                break
                break
        if success2 == 1:
                break
        else:
                print("Sorry, that is not a valid date.")
#This loop checks if the input can be converted to a float.
while True:
        money = input("How much money would you like to invest? (USD) ")
        try:
                float(money)
                break
        except ValueError:
                print("That is not a valid value.")
#This locates the highest stock price for a given date.
def gethigh(info):
        histdata = history.loc[info]
        histdata2 = str(histdata.loc["High"])
        if histdata2 == 0:
                histdata2 += 0.01
        return float(histdata2)
#This locates the lowest stock price for a given date.
def getlow(info):
        histdata = history.loc[info]
        histdata2 = str(histdata.loc["Low"])
        #This is to make sure the program doesn't divide by zero.
        if histdata2 == 0:
                histdata += 0.01
        return float(histdata2)
#This finds the value of the investment once withdrawn.
def findreturn(yearstart, yearend, investment):
        if yearstart == 0:
                yearstart += 0.01
        growth = (yearend/yearstart)
        change = float(investment)*float(growth)
        return float(round(change, 2))
#This finds the difference between the investment and the withdrawn value.
def findprofit(yearstart, yearend, investment):
        if yearstart == 0:
                yearstart += 0.01 
        percentchange = (yearend/yearstart)
        difference = float(investment)*percentchange
        profit = abs(round(float(investment)-difference, 2))
        return profit
#This determines if there was a gain or loss in money.
def gainorloss(yearend, yearstart):
        highend = gethigh(yearend)
        highstart = gethigh(yearstart)
        if highstart == 0:
                highstart += 0.01
        percentchange = highend/highstart
        if percentchange >= 1:
                return "Gain"
        else:
                return "Loss"
#Gathering Data/Variables
yearstartmax = gethigh(date)
yearendmax = gethigh(date2)
yearstartmin = getlow(date)
yearendmin = getlow(date2)

#This organizes return and gain/loss statements into smallest first, biggest second format.
financiallist = [round(Decimal(findreturn(yearstartmax, yearendmin, money)), 2), round(Decimal(findreturn(yearstartmin, yearendmax, money)), 2)]

if financiallist[0] > financiallist[1]:
        financialmax = str(financiallist[0])
        financialmin = str(financiallist[1])
else:
        financialmax = str(financiallist[1])
        financialmin = str(financiallist[0])

print()

print("Your return would be between $"+f"{float(financialmin):,}","and $"+f"{float(financialmax):,}"+".")
#This calculates the range of profits/losses.
#Also changes the format to smallest first, biggest second.
if round(Decimal(findprofit(yearstartmax, yearendmax, money)), 2) > round(Decimal(findprofit(yearstartmin, yearendmin, money)), 2):
        maxprofitoutput = str(round(Decimal(findprofit(yearstartmax, yearendmax, money)), 2))
        minprofitoutput = str(round(Decimal(findprofit(yearstartmin, yearendmin, money)), 2))
else:
        minprofitoutput = str(round(Decimal(findprofit(yearstartmax, yearendmax, money)), 2))
        maxprofitoutput = str(round(Decimal(findprofit(yearstartmin, yearendmin, money)), 2))
indicator = gainorloss(date2, date)

print("That is a",indicator,"of $"+f"{float(minprofitoutput):,}","(Minimum) or $"+f"{float(maxprofitoutput):,}","(Maximum).")
#For more info on specific stock prices, use the line "print(history)" anywhere after line 23. 