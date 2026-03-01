import csv

def search_books(keyword):
    print(f"\n--- Searching for: '{keyword}' ---")
    count = 0
    
    with open('goodreads_library_export.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            
            if keyword.lower() in row['Title'].lower() or keyword.lower() in row['Author'].lower():
                print(f"📖 {row['Title']} by {row['Author']} (Rating: {row['My Rating']}/5)")
                count += 1
    
    print(f"\nFound {count} matches.")

search_books('Robot')
