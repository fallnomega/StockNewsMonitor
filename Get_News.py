import os
import requests
import TextAlerts

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# https://newsapi.org/v2/everything?q=tesla&from=2023-02-01&sortBy=publishedAt&apiKey=API_KEY

class News:
    def __init__(self, ticker,company_name, fromDate, up_or_down):
        self.NAME = company_name
        self.from_date = fromDate
        self.url = "https://newsapi.org/v2/everything"
        self.parameters = {'apiKey': NEWS_API_KEY, 'q': company_name, 'from': fromDate}
        self.up_down = up_or_down
        self.ticker = ticker
        # Example https://newsapi.org/v2/everything?q=tesla&from=2023-02-01&sortBy=publishedAt&apiKey=API_KEY

    def get_news(self):
        get_request = requests.get(url=self.url, params=self.parameters)
        get_request.raise_for_status()
        data = get_request.json()
        if len(data['articles']) >= 3:
            for x in data['articles'][0:3]:
                print(f"Title: {x['title']}")
                print(f"Description: {x['description']}")
                send_text = TextAlerts.Alert(self.ticker,self.up_down, x['title'], x['description'], self.from_date)
                send_text.send_alert()
        else:
            print(data['articles'])
