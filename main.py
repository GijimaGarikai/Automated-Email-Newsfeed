import yagmail
import pandas
from news import NewsFeed
import time
import datetime

while True:
    if datetime.datetime.now().hour == 16 and datetime.datetime.now().minute == 6:
        email = yagmail.SMTP(user="email goes here", password='google app password goes here')
        df = pandas.read_excel('people.xlsx')
        for index, row in df.iterrows():
            try:
                feed = NewsFeed(row['interest'])
                email.send(to=row['email'],
                           subject=f'Your {row["interest"]} newsfeed for today!',
                           contents=f'{feed.get()}')
            except:
                print(row['email'], ' is invalid')
    time.sleep(60)
    # As long as program is ruuning it will execute once everyday



