import twilio
import requests
import os

import News
import Stock

# ENV variable for keys,tokens, etc
ALPHA_API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')

# Test ticker
TICKER = "BGCP"
COMPANY_NAME = "BGC Partners"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
my_ticker = Stock.Stock(TICKER, COMPANY_NAME)
my_ticker.get_intraday()
my_ticker.parse_data()

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# https://newsapi.org/v2/everything?q=tesla&from=2023-02-01&sortBy=publishedAt&apiKey=API_KEY

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
