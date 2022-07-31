################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import urllib.request
import time
import json
import random

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
  stock = quote['stock']
  bid_price = float(quote['top_bid']['price'])
  ask_price = float(quote['top_ask']['price'])
  sum = bid_price + ask_price
  avg = sum/2
  price = avg
  return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
  # to avoid nonReturnZero
  if (price_b == 0):
    return
  return price_a/price_b
	

# Main
if __name__ == "__main__":
  for _ in range(N):
    quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
    stockPrices = {}
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      stockPrices[stock] = price
      print ("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
    price_a = stockPrices['ABC']
    price_b = stockPrices['DEF']
    print ("Ratio %s" % getRatio(price_a,price_b))

		