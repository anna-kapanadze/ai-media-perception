import csv
import matplotlib.pyplot as plt

author_ratings = {}

with open('goodreads_library_export.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        author = row['Author']
        rating = row['My Rating']
        
        # Only count books actually rated
        if rating and int(rating) > 0:
            if author not in author_ratings:
                author_ratings[author] = []
            author_ratings[author].append(int(rating))

authors = []
avg_ratings = []

for author in author_ratings:
    ratings = author_ratings[author]
    avg = sum(ratings) / len(ratings)
    authors.append(author)
    avg_ratings.append(avg)

# Sort highest rated authors at the top
sorted_data = sorted(zip(avg_ratings, authors))
avg_ratings, authors = zip(*sorted_data)

# Color code: Green for high ratings (4-5), Yellow for mid (3), Red for low (1-2)
colors = []
for r in avg_ratings:
    if r >= 4: colors.append('green')
    elif r >= 3: colors.append('gold')
    else: colors.append('red')

plt.figure(figsize=(10, 8))
plt.barh(authors, avg_ratings, color=colors)
plt.xlabel('Average Star Rating (1-5)')
plt.title('Author Mood Map (Based on Star Ratings)')
plt.tight_layout()

plt.savefig('mood_map.png')
print("Graph saved as mood_map.png")
