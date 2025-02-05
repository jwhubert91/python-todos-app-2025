import webbrowser

user_term = input("Enter a search term: ")
url = f"https://duckduckgo.com/?t=h_&q={user_term}"

webbrowser.open(url)