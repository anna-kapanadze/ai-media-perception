import csv
from textblob import TextBlob

print("SENTIMENT AUDIT")

with open('goodreads_library_export.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        review = row['Body']
        
        if review:
            analysis = TextBlob(review)
            score = analysis.sentiment.polarity
            
            if score > 0.1:
                status = "Positive"
            elif score < -0.1:
                status = "Negative"
            else:
                status = "Neutral"
            
            print("Book: " + row['Title'])
            print("Sentiment: " + status + " " + str(round(score, 2)))
