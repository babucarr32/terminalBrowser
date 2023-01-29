try:
    import sys
    import os
    import requests
    from bs4 import BeautifulSoup
    from googlesearch import search
    import banner
    import re
except ImportError:
	print("No module named 'google' found")

print(banner.banner)
def helper():
    print("-----------------------------------")
    print("Example: main.py raw https://www.python.com")
    print("Example: main.py hint python limit=20")
    print("Example: main.py url limit=20 python")
    print("----------------------------------")
    print("""
    Comands:
            raw: Display the text of a site(s).
            hint: Display some info about the site(s).
            url: Display the url of the site(s).
            limit=<int>: The number of searches to retrive.
                        E.g: main.py url python limit=20
                        # to display 20 search results only.
            
    """)


def terminaleBrowser():
    if len(sys.argv) == 1:
        print(f"Command Usage: [<script>, <arg>, <search>]")
        print("Type --help: to show the usage...")
        quit()
    # to search
    
    if "raw" in sys.argv:
        r = requests.get(str(sys.argv[2]))
        soup = BeautifulSoup(r.text, "lxml")
        soup = soup.get_text()
        soup = re.sub(r'\n\s*\n', '\n\n', soup)
        print(soup)

    elif "hint" in sys.argv:
        searchCount = 0
        query = str(sys.argv[2])
        for arg in sys.argv:
            if "limit=" in arg:
                limit = arg.split("=")[1]
                print("------------------------------------------------------------")
                print(f"{limit} SEARCH RESULTS FOR: {sys.argv[2]}")
                print("-----------------------------------------------------------")
        
        for j in search(query, tld="co.in", num=10, stop=int(limit), pause=3):
            searchCount += 1
            try:
                print(f"WEBSITE {searchCount}: {j}\n")
                r = requests.get(str(j))
                soup = BeautifulSoup(r.text, "html.parser")
                print(soup.get_text().replace("\n", '')[:300] + "...")
                print("\n")
                print("-----------------------------------------------------------------\n")
            except Exception as e:
                continue

    elif "--help" in sys.argv:
        helper()
    
    elif "url" in sys.argv:
        query = str(sys.argv[2])
        searchCount = 0

        for arg in sys.argv:
            if "limit=" in arg:
                limit = arg.split("=")[1]
                print("------------------------------------------------------------")
                print(f"{limit} SEARCH RESULTS FOR: {sys.argv[2]}")
                print("-----------------------------------------------------------")
        
        for j in search(query, tld="co.in", num=10, stop=int(limit), pause=2):
            searchCount+=1
            print(f"Website {searchCount}: {j}")

    else:
        print(f"Unknown command...")
        print("Type --help: to show the usage...")
        quit()
terminaleBrowser()