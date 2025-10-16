import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def analyze_sentiment():
    df = pd.read_csv("data/news.csv")
    df["sentiment"] = df["headline"].apply(get_sentiment)
    df.to_csv("data/news_sentiment.csv", index=False)
    print("Sentiment analysis completed!")

if __name__ == "__main__":
    analyze_sentiment()
