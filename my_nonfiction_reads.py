import csv

print("FINISHED NON-FICTION & AI")

with open('goodreads_library_export.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        # Only include it if it's on the 'read' shelf AND has 'ai' or 'non-fiction' tags
        if row['Exclusive Shelf'] == 'read':
            if 'non-fiction' in row['Bookshelves'].lower() or 'ai' in row['Bookshelves'].lower():
                print(f"✔️ {row['Title']}")
                count += 1

print(f"\nTotal Finished Non-Fiction: {count}")
