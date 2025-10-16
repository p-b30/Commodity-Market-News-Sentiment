import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_news():
    url = "https://www.marketwatch.com/latest-news?mod=top_nav"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    headlines = [item.text for item in soup.select(".article__headline")]
    dates = [item.text for item in soup.select(".article__timestamp")]

    news_df = pd.DataFrame({"date": dates, "headline": headlines})
    news_df.to_csv("data/news.csv", index=False)
    print("News scraped successfully!")

if __name__ == "__main__":
    scrape_news()
