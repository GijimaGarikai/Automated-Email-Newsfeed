import yagmail
import pandas
from news import NewsFeed
import time
import datetime

while True:
    if datetime.datetime.now().hour == 16 and datetime.datetime.now().minute == 6:

        # Could add current date/time functionality but its not that interesting really
        email = yagmail.SMTP(user="pythondummymail3@gmail.com", password='jsugpsdnmedmvvqj')
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



