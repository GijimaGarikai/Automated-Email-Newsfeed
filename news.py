import requests
from pprint import pprint
import time

class NewsFeed:

    def __init__(self, interest, num_articles=10):
        self.interest = interest
        self.num_articles = num_articles

    def getContent(self):
        url = "https://newsapi.org/v2/everything?" \
              f"q={self.interest}&" \
              "language=en&" \
              "apiKey=5c5c026e60bd46a3a801d095af058673"
        response = requests.get(url)
        content = response.json()
        return content

    def createFeed(self):
        articles = self.getContent()['articles']
        temp_body = []
        count = 0
        while count < self.num_articles and count < len(articles):
            temp_body.append(articles[count]['title'] + '\n' + articles[count]['url'] + '\n\n')
            count += 1
        email_body = ''.join(temp_body)
        return email_body

    def get(self):
        return self.createFeed()




