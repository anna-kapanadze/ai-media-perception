import csv

def show_my_books(goodreads_library_export.csv):
    print(f"\n--- DATA FROM: {goodreads_library_export.csv} ---")
    with open(goodreads_library_export.csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"[{row['Status']}] {row['Title']} by {row['Author']} - ⭐ {row['Rating']}/5")

show_my_books('non_fiction_list.csv')
