from scripts.scrape_news import scrape_news
from scripts.sentiment_analysis import analyze_sentiment
from scripts.fetch_prices import fetch_prices
from scripts.merge_data import merge_data
from scripts.visualize import visualize

def run_all():
    scrape_news()
    analyze_sentiment()
    fetch_prices()
    merge_data()
    visualize()

if __name__ == "__main__":
    run_all()
