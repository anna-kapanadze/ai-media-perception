import csv

print("--- FINISHED FICTION ---")

with open('goodreads_export.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        # Check if it's 'read' and NOT 'non-fiction'
        if row['Exclusive Shelf'] == 'read':
            if 'non-fiction' not in row['Bookshelves'].lower():
                print(f"✨ {row['Title']}")
                count += 1

print(f"\nTotal Finished Fiction: {count}")
