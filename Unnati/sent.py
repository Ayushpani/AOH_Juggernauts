from textblob import TextBlob

def perform_sentiment_analysis(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    # Define sentiment labels based on polarity score
    if sentiment_score >= 0.5:
        sentiment_label = 'Very Happy'
    elif 0.2 <= sentiment_score < 0.5:
        sentiment_label = 'Happy'
    elif -0.2 <= sentiment_score < 0.2:
        sentiment_label = 'Neutral'
    elif -0.5 <= sentiment_score < -0.2:
        sentiment_label = 'Sad'
    else:
        sentiment_label = 'Angry'

    return sentiment_score, sentiment_label

# Input file path (the translated English text file)
input_file_path = 'translated_english.txt'

# Perform sentiment analysis
sentiment_score, sentiment_label = perform_sentiment_analysis(input_file_path)

print("Sentiment Score:", sentiment_score)
print("Sentiment Label:", sentiment_label)
