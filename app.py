import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit app configuration
st.set_page_config(page_title="Commodity Market Sentiment", layout="wide")

# Custom CSS for UI colors

st.markdown("""
    <style>
    /* Animated gradient background */
    @keyframes waveBackground {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stApp {
        background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1E3A8A);
        background-size: 400% 400%;
        animation: waveBackground 15s ease infinite;
        color: white;
    }

    /* Headings */
    h1, h2, h3 {
        color: #FFD700;
    }

    /* Buttons */
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff1c1c;
    }

    /* Dataframe table */
    .stDataFrame {
        background-color: #ffffff10;
        border-radius: 10px;
        padding: 10px;
    }

    /* File uploader */
    .stFileUploader {
        background-color: #ffffff20;
        border-radius: 10px;
        padding: 10px;
    }
            
    /* Glow animation for icons */
   /* Icon-only glow animation */
    @keyframes iconGlow {
        0% { text-shadow: 0 0 5px #03346E, 0 0 10px #03346E, 0 0 20px #03346E; }
        50% { text-shadow: 0 0 15px #78B9B5, 0 0 25px #78B9B5, 0 0 35px #78B9B5; }
        100% { text-shadow: 0 0 5px #03346E, 0 0 10px #03346E, 0 0 20px #03346E; }
    }
    .glow-icon {
        display: inline-block;
        color: #03346E;
        animation: iconGlow 2s infinite alternate;
    }
    
            
    </style>
""", unsafe_allow_html=True)



# title
st.title("Commodity Market News Sentiment Visualization")





# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Load data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File loaded successfully!")
else:
    st.info("Using default sample data.")
    df = pd.read_csv("data/merged_data.csv")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# Ensure numeric columns
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
for col in ['Positive', 'Negative', 'Neutral']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

df = df.sort_values(by='Date')

# Show dataframe
st.markdown("<h2><span class='glow-icon'>🔍</span> Data Preview</h2>", unsafe_allow_html=True)



st.dataframe(df)


# Plot
st.markdown("<h2><span class='glow-icon'>📈</span> Visualization</h2>", unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(14,6))
sns.lineplot(x="Date", y="Close", data=df, label="Crude Oil Price", marker='o', ax=ax)
if 'Positive' in df.columns:
    sns.lineplot(x="Date", y="Positive", data=df, label="Positive News", marker='o', ax=ax)
if 'Negative' in df.columns:
    sns.lineplot(x="Date", y="Negative", data=df, label="Negative News", marker='o', ax=ax)
if 'Neutral' in df.columns:
    sns.lineplot(x="Date", y="Neutral", data=df, label="Neutral News", marker='o', ax=ax)

plt.xticks(rotation=45)
plt.title("Commodity Price vs Market News Sentiment")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
st.pyplot(fig)




st.download_button(
    label="Download Data as CSV",
    data=df.to_csv(index=False),
    file_name="commodity_sentiment_data.csv",
    mime="text/csv"
)