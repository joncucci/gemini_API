'''
Author: Jonathan Cucci
'''

import requests, json
import sys
import datetime
from statistics import *
import statistics

def output(msg, variable = ""):
    print(str(datetime.datetime.now()) + msg + str(variable))

def price_dev(sym):

    output(" - AlertingTool - INFO - *** Running priceDev check on: ", sym)
    output(" - AlertingTool - INFO - Getting Price API Data for: ", sym)

    price_info = (requests.get("https://api.gemini.com/v2/ticker/" + sym).json())

    last_price = float(price_info['close'])
    output(" - AlertingTool - INFO - Last Price: ", last_price)

    float_changes = [float(i) for i in price_info['changes']]
    std_dev = statistics.stdev(float_changes)
    average = mean(float_changes)
    diff = average - last_price

    output(" - AlertingTool - INFO - Standard Deviation: ", std_dev)
    output(" - AlertingTool - INFO - Average: ", average)
    output(" - AlertingTool - INFO - Price diff: ", diff)

    if abs(diff) > std_dev:

        output(" - AlertingTool - ERROR - ****** Price Deviation")

    print("\n")

def price_change(sym):

    x = float(input("Enter your percent change value: "))

    output(" - AlertingTool - INFO - *** Running priceChange check on: ", sym)
    output(" - AlertingTool - INFO - Getting Price API Data for: ", sym)

    price_info = (requests.get("https://api.gemini.com/v2/ticker/" + sym).json())
    opening_price = float(price_info['open'])
    closing_price = float(price_info['close'])
    low = (1-(x/100)) * opening_price
    high = (1+(x/100)) * opening_price

    output(" - AlertingTool - INFO - Opening Price: ", opening_price)
    output(" - AlertingTool - INFO - Current Price: ", closing_price)
    output(" - AlertingTool - INFO - Percent Difference: ", (str(x) + "%"))
    output(" - AlertingTool - INFO - Low Threshold: ", str(low))
    output(" - AlertingTool - INFO - High Threshold: ", str(high))
    if closing_price < low or closing_price > high:
        output(" - AlertingTool - ERROR - ****** Price Change outside Percent Threshold")
    
    print("\n")

def volume_deviation(sym):

    x = float(input("Enter your percent change value: "))

    output(" - AlertingTool - INFO - *** Running volumeDeviation check on: ", sym)
    output(" - AlertingTool - INFO - Getting Volume API Data for: ", sym)

    base = (requests.get("https://api.gemini.com/v1/symbols/details/" + sym).json())['base_currency']
    volume = float((requests.get("https://api.gemini.com/v1/pubticker/" + sym).json())['volume'][base])

    output(" - AlertingTool - INFO - Base Currency: ", base)
    output(" - AlertingTool - INFO - Volume in Market: ", volume)

    trade_info = (requests.get("https://api.gemini.com/v1/trades/" + sym).json())[0]
    amount_traded = float(trade_info['amount'])

    output(" - AlertingTool - INFO - Most Recent Trade Volume: ", amount_traded)

    percent_of_volume = (amount_traded / volume) * 100

    output(" - AlertingTool - INFO - Percent of Volume Purchase: ", (str(percent_of_volume) + "%"))
    output(" - AlertingTool - INFO - Percent Threshold: ", (str(x) + "%"))

    if percent_of_volume > x:
        output(" - AlertingTool - ERROR - ****** Volume purchased outside Percent Threshold")

print("\n")

output(" - AlertingTool - INFO - Parsing args")
args = sys.argv

currencies = requests.get("https://api.gemini.com/v1/symbols").json()
functions = ["pricedev", "pricechange", "voldev", "all"]

if "-h" in args:
    print("\n")
    print("List of functions")
    print(functions)
    print("\n")
    print("List of currencies")
    print(currencies)
    exit()

try: 
    symbol = args[args.index('-c') + 1]
except ValueError:
    print("Please enter a '-c' with proper CURRENCY from below.")
    print(currencies)
    quit()

if symbol not in currencies:
    print(currencies)
    raise "Currency input not in list of currencies"

try: 
    command = args[args.index('-t') + 1].lower()
except ValueError:
    print("Please enter a '-t' with proper FUNCTION from below.")
    print(functions)
    quit()

if command not in functions:
    print(functions)
    raise "Function input not in list of functions"

output(" - AlertingTool - INFO - Running Check: ", command)
print("\n")

base_url = "https://api.gemini.com/v1"
symbol_details = (requests.get(base_url + "/symbols/details/" + symbol)).json()

if command == "pricedev":
    price_dev(symbol)

elif command == "pricechange":
    price_change(symbol)

elif command == "voldev":
    volume_deviation(symbol)

elif command == "all":
    price_dev(symbol)
    price_change(symbol)
    volume_deviation(symbol)