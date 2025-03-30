import pandas as pd
from textblob import TextBlob

# Load dataset
df = pd.read_csv("C:/Users/RASIRAKU/Downloads/twitter_training.csv/twitter_training.csv")  # Replace with your actual file
df["Tweet"] = df["Positive"].astype(str)  # Ensure text format

# Compute sentiment polarity
df["Polarity"] = df["Tweet"].apply(lambda text: TextBlob(text).sentiment.polarity)

# Save to Excel
df.to_excel("sentiment_analysis.xlsx", index=False)
print("Sentiment scores saved to sentiment_analysis.xlsx")
