#textblob library

from textblob import TextBlob

#create a sample text

texts=[
    "I love NLP ! Its great and I'am very satisfied",
    "This is my first experience on doing sentiment analysis, Iam little bit disapointed",
    "The NLP sentiment analysis is quiet interesting it is neither good or bad",
]

#create a function to do sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

for text in texts:
    sentiment = analyze_sentiment(text)
    print("text: ", text )
    print("Sentiment: ", sentiment)

