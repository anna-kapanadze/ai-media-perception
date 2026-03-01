import csv

ratings = []

with open('goodreads_export.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert the rating from a string to a number (integer)
        rating = int(row['My Rating'])
        if rating > 0: # Ignore books you haven't rated yet
            ratings.append(rating)

if ratings:
    avg = sum(ratings) / len(ratings)
    print(f" Your average book rating is: {avg:.2f} / 5")
    print(f" Total rated books: {len(ratings)}")
