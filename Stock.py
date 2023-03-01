import os
import requests
import News
import datetime

ALPHA_API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')


class Stock:
    def __init__(self, ticker, companyName):
        self.STOCK = ticker
        self.ticker_history = {}
        self.price_history = {}
        self.company_name = companyName
        self.from_Date = ''

    def get_intraday(self):
        parameters = {"function": "TIME_SERIES_INTRADAY", "symbol": self.STOCK, "interval": "60min",
                      "apikey": ALPHA_API_KEY}
        url = 'https://www.alphavantage.co/query'
        r = requests.get(url, params=parameters)
        self.ticker_history = r.json()

    def parse_data(self):
        ticker_history = {}
        for x in self.ticker_history.values():
            ticker_history = x
        for key in ticker_history:
            self.price_history[key] = ticker_history[key]['4. close']
        self.find_changes()

    def find_changes(self):
        ## STEP 1: Use https://www.alphavantage.co
        # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

        temp_prices = list(self.price_history.values())
        # print(temp_prices)
        try:
            for k, i in self.price_history.items():
                percentage_diff = (float(i) * 100) / float(temp_prices[temp_prices.index(i) + 1]) - 100
                if percentage_diff >= 5 or percentage_diff <= -5:
                    print("GET NEWS!!")
                    # print(k)
                    temp_date = str.split(k, ' ')
                    my_date = datetime.datetime.strptime(temp_date[0], '%Y-%m-%d')
                    # print (my_date.strftime('%Y-%m-%d'))
                    self.from_Date = my_date.strftime('%Y-%m-%d')
                    my_news = News.News(self.company_name, self.from_Date)
                    my_news.get_news()
#TODO make it where the news doesnt get called everytime a hit is returned for the 5% iff statement above
                    # print(f"Hour and Value: {k} {i}")
                    # print(f"Previous Hour's Value= {temp_prices[temp_prices.index(i) + 1]}")
                    # print ("percentage_diff = " , percentage_diff)

        except IndexError:
            # print("\n\nReached the end of the list")

            return
