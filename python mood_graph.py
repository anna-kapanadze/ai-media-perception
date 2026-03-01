import csv
import matplotlib.pyplot as plt
from textblob import TextBlob

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

authors = []
avg_scores = []

for author in author_scores:
    scores = author_scores[author]
    avg = sum(scores) / len(scores)
    authors.append(author)
    avg_scores.append(avg)

sorted_data = sorted(zip(avg_scores, authors))
avg_scores, authors = zip(*sorted_data)

colors = []
for s in avg_scores:
    if s > 0:
        colors.append('green')
    else:
        colors.append('red')

plt.barh(authors, avg_scores, color=colors)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('Sentiment Score')
plt.title('Author Mood Map')
plt.tight_layout()

plt.savefig('mood_map.png')
print("Graph saved as mood_map.png")
