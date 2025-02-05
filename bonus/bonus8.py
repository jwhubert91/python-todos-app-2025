journal_date = input("Enter today's date: ")
journal_mood = input("How is your mood from 1 to 10? ")
journal_entry = input("Let your thoughts flow: ")

filename = f"{str(journal_date)}.txt"

with open(f"../journals/{filename}", "w") as file:
    date_string = "Date: " + journal_date + "\n"
    mood_string = "Mood: " + journal_mood + "\n"
    entry_string = "Entry: " + journal_entry + "\n"
    journal = [date_string, mood_string, entry_string]
    file.writelines(journal)

with open(f"../journals/{filename}", "r") as file:
    entry = file.read()
    print(f"Entry complete:")
    print(entry)