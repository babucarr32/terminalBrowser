try:
    import sys
    import os
    import requests
    from bs4 import BeautifulSoup
    from googlesearch import search
    import banner
except ImportError:
	print("No module named 'google' found")

print(banner.banner)
def helper():
    print("-----------------------------------")
    print("Example: main.py o www.target.com")
    print("Example: main.py sV python")
    print("Example: main.py python")
    print("----------------------------------")
    print("""
    Comands:
            raw: Display the text of a site(s).
            hint: Display some info about the site(s).
            prettify: Display the text of a site(s), with prettify.

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
        print(soup.get_text())

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
    else:
        print(True)
        print(True)
        query = str(sys.argv[1])
        print(query)
        print("------------------------------------------------------------")
        print(f"SEARCH RESULTS FOR: {sys.argv[1]}")
        print("-----------------------------------------------------------")
        for j in search(query, tld="co.in", num=10, stop=20, pause=2):
            print(j)

terminaleBrowser()