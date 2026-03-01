import csv
from textblob import TextBlob

print("AUTHOR MOOD MAP")

author_scores = {}

with open('goodreads_export.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        review = row['Body']
        author = row['Author']
        
        if review:
            analysis = TextBlob(review)
            score = analysis.sentiment.polarity
            
            if author not in author_scores:
                author_scores[author] = []
            
            author_scores[author].append(score)

print("AVERAGE SENTIMENT BY AUTHOR")

for author in author_scores:
    scores = author_scores[author]
    avg_score = sum(scores) / len(scores)
    
    if avg_score > 0.1:
        mood = "Happy"
    elif avg_score < -0.1:
        mood = "Critical"
    else:
        mood = "Neutral"
        
    print("Author: " + author)
    print("Average Mood: " + mood + " (" + str(round(avg_score, 2)) + ")")
    print("------------------------------")
