import twilio.rest
import os

ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
class Alert:
    def __init__(self,ticker,up_or_down,title,description,news_date):
        self.my_twillio = twilio.rest.Client(ACCOUNT_SID, AUTH_TOKEN)
        self.news_title = title
        self.article_decription = description
        self.news_posted_on = news_date
        self.up_down = up_or_down
        self.ticker = ticker

        # x['title'], x['description'], self.from_date

    def send_alert(self):
        message = self.my_twillio.messages.create(
            body=f"\n{self.ticker} is {self.up_down} \nDate: {self.news_posted_on} - {self.news_title}\n{self.article_decription}",
            from_=os.environ.get('TWILIO_NUMBER'),
            to=os.environ.get('TARGET_PHONE_NUMBER'))
