import csv

# This is the 'Librarian' function
def search_books(keyword):
    print(f"\n--- 🔍 Searching for: '{keyword}' ---")
    count = 0
    
    # Opening your Goodreads export
    with open('goodreads_export.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check if the keyword is in the Title or the Author's name
            if keyword.lower() in row['Title'].lower() or keyword.lower() in row['Author'].lower():
                print(f"📖 {row['Title']} by {row['Author']} (Rating: {row['My Rating']}/5)")
                count += 1
    
    print(f"\nFound {count} matches.")

# Try searching for 'AI', 'Robot', or a specific author like 'Ishiguro'
search_books('Robot')
