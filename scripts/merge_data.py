import pandas as pd

def merge_data():
    news_df = pd.read_csv("data/news_sentiment.csv")
    commodity_df = pd.read_csv("data/commodity_prices.csv")
    
    news_df['date'] = pd.to_datetime(news_df['date'])
    commodity_df['Date'] = pd.to_datetime(commodity_df['Date'])

    sentiment_daily = news_df.groupby(news_df['date'].dt.date)['sentiment'].value_counts().unstack(fill_value=0)
    merged_df = commodity_df.merge(sentiment_daily, left_on="Date", right_index=True, how="left").fillna(0)
    merged_df.to_csv("data/merged_data.csv", index=False)
    print("Data merged successfully!")

if __name__ == "__main__":
    merge_data()
