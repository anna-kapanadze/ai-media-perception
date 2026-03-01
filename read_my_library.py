import csv

def show_my_books(filename):
    print(f"\n--- 📚 DATA FROM: {filename} ---")
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # This neatly prints each book from your list
            print(f"[{row['Status']}] {row['Title']} by {row['Author']} - ⭐ {row['Rating']}/5")

# Run the function for your non-fiction list
show_my_books('non_fiction_list.csv')
