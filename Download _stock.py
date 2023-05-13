

##Terminal:pip3 install yfinance

##### Import packages

import yfinance as yf
import matplotlib.pyplot as plt 

#### Download stock data from Yahoo Finance

stock = yf.download("GOOG", "2019-09-15", "2019-09-25")
stock.head()
#
#

#### Save the data as csv file in local

stock.to_csv("stock.csv")

#### Visualize the trend of the stock

fig = plt.figure(figsize = (10, 5))
plt.plot(stock["Open"], color = "red")
plt.title("Google open price")
plt.show();
#change the range of figure
#
#
#
#

##
fig = plt.figure(figsize = (10, 5))
plt.plot(stock["Open"], color = "red")
plt.plot(stock["Close"], color = "green")
plt.title("Google open price")
plt.legend()
plt.show();

