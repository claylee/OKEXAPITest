#! /usr/bin/env python
#
# @brief XCoin API-call sample script (for Python 2.x, 3.x)
#
# @author btckorea
# @date 2017-04-14
#
# @details
# First, Build and install pycurl with the following commands::
# (if necessary, become root)
#
# https://pypi.python.org/pypi/pycurl/7.43.0#downloads
#
# tar xvfz pycurl-7.43.0.tar.gz
# cd pycurl-7.43.0
# python setup.py --libcurl-dll=libcurl.so install
# python setup.py --with-openssl install
# python setup.py install
#
# @note
# Make sure current system time is correct.
# If current system time is not correct, API request will not be processed normally.
#
# rdate -s time.nist.gov
#

import sys
from xcoin_api_client import *
import pprint
import time
import JsonlizeData
import SerialDataDb

api_key = "api_connect_key";
api_secret = "api_secret_key";

api = XCoinAPI(api_key, api_secret);

rgParams = {
	"order_currency" : "BTC",
	"payment_currency" : "KRW"
};

serialDataFile = SerialDataDb.SerialDataDb("../../html/Data/bithumb/")

def ScrapTicket():
	#
	# Public API
	#
	# /public/ticker
	# /public/recent_ticker
	# /public/orderbook
	# /public/recent_transactions
	print("Bithumb Public API URI('/public/ticker') Request...");
	result = api.xcoinApiCall("/public/ticker", rgParams);
	print("- Status Code: " + result["status"]);
	print("- Opening Price: " + result["data"]["opening_price"]);
	print("- Closing Price: " + result["data"]["closing_price"]);
	print("- Sell Price: " + result["data"]["sell_price"]);
	print("- Buy Price: " + result["data"]["buy_price"]);
	print("");

	for i in range(30000):
		try:
			time.sleep(1)
			print(">>",i)
			result = api.xcoinApiCall("/public/ticker", rgParams);
			print("- Buy Price: " + result["data"]["date"]);
			print("- Buy Price: " + result["data"]["buy_price"]);
			serialDataFile.SerialMessage(result)
			if(i%50==0):
				serialDataFile.storeToFile()
		except Exception as ExArgument:
			print('Main loop Error:', ExArgument)
	#
	# Private API
	#
	# endpoint => parameters
	# /info/current
	# /info/account
	# /info/balance
	# /info/wallet_address

	#print("Bithumb Private API URI('/info/account') Request...");
	#result = api.xcoinApiCall("/info/account", rgParams);
	#print("- Status Code: " + result["status"]);
	#print("- Created: " + result["data"]["created"]);
	#print("- Account ID: " + result["data"]["account_id"]);
	#print("- Trade Fee: " + result["data"]["trade_fee"]);
	#print("- Balance: " + result["data"]["balance"]);

def SerialCurDataToFile():
	serialDataFile.storeToFile()

commandKey = input("input command number:\n\
1:Scarp Data from BitHumb\n\
2:Serial data to file\n")

if(commandKey == "2"):
	SerialCurDataToFile()
else:
	ScrapTicket()


sys.exit(0);
