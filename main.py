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
    print("Example: main.py raw www.target.com")
    print("Example: main.py hint python")
    print("Example: main.py prettify python")
    print("----------------------------------")
    print("""
    Comands:
            raw: Display the text of a site(s).
            hint: Display some info about the site(s).
            url: Display the url of the site(s).
            prettify: Display the text of a site(s), with prettify.
            pause<int>: Determine pause interval between searches.
                        E.g: main.py url pause3 python # to pause for
                        3 seconds, each search.
            stop<int>: The last result to retrieve. You can set it to 
                        None to keep searching forever.
                        E.g: main.py url stop3 python .
            num<int>: The number of searches we want to retrive.
                        E.g: main.py url num5 python # to display
                        10 search results only.
            tld:<str>: This refers to the top level domain
                        E.g: main.py url tld:co.in # to search usigng
                        google.
    """)


def terminaleBrowser():
    if len(sys.argv) == 1:
        print(f"Command Usage: [<script>, <arg>, <search>]")
        print("Type --help: to show the usage...")
        quit()
    # to search
    
    if "raw" in sys.argv:
        r = requests.get(str(sys.argv[2]))
        soup = BeautifulSoup(r.text, "html.parser")
        soup = soup.get_text()
        # soup = soup.replace("\n\n", "\n")
        soup = re.sub(r'\n\s*\n', '\n\n', soup)
        # print(soup.get_text())
        print(soup)

    elif "prettify" in sys.argv:
        r = requests.get(str(sys.argv[2]))
        soup = BeautifulSoup(r.text, "html.parser")
        with open("index.html", "w") as f:
            f.write(soup.prettify())
        # print(soup.prettify())

    elif "hint" in sys.argv:
        pass
        print("------------------------------------------------------------")
        print(f"SEARCH RESULTS FOR: {sys.argv[2]}")
        print("-----------------------------------------------------------")

        query = str(sys.argv[2])
        for j in search(query, tld="co.in", num=10, stop=20, pause=3):
            try:
                print(f"WEBSITE: {j}\n")
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
        print(True)
        print(True)
        query = str(sys.argv[1])
        print(query)
        print("------------------------------------------------------------")
        print(f"SEARCH RESULTS FOR: {sys.argv[1]}")
        print("-----------------------------------------------------------")
        for j in search(query, tld="co.in", num=10, stop=20, pause=2):
            print(j)

    else:
        print(f"Unknown command...")
        print("Type --help: to show the usage...")
        quit()
terminaleBrowser()