import csv
import sys
import yfinance as yf
from dataclasses import dataclass


@dataclass
class Position:
    fund: str
    buy_sell: str
    ticker: str
    name: str
    percent_of_etf: str


# Main loop to read CSV file and make function calls
def readFile(filename):
    listoftrades = []
    with open(filename) as fd:
        reader = csv.reader(fd)
        for row in reader:
            info = Position(row[0], row[1], row[2], row[3], row[4])

            # if stock was bought
            if info.buy_sell == "Buy" and int(row[4]) >= .01:  # .01 critical val
                # compare to holdings
                position_held = compare_to_holdings(info.ticker)
                # if currently held
                if position_held:
                    position_object = get_ticker_info(info.ticker)
                    # Check amount bought -- (add alerting function for stock)
                else:
                    pass

            # if stock was sold
            elif info.buy_sell == "Sell" and int(row[4]) >= .03:  # .03 critical val
                # compare to holdings
                position_held = compare_to_holdings(info.ticker)
                if position_held:
                    position_object = get_ticker_info(info.ticker)
                    # Check amount bought -- (add alerting function for stock)
                else:
                    pass


# Returns Yahoo Finance object of certain ticker
def get_ticker_info(tickername):
    tickerdata = yf.Ticker(tickername)
    tickerinfo = tickerdata.info
    return tickerinfo


# Compares alerted stock to list of holdings
def compare_to_holdings(alerted):
    position_held = None
    holdings = []
    for x in holdings:
        if x == alerted:
            position_held = True
        else:
            position_held = False
    return position_held


# Main method
def main():
    filename = sys.argv[1]
    readFile(filename)


main()
