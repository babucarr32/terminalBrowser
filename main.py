try:
    import sys
    import os
    import requests
    from bs4 import BeautifulSoup
    from googlesearch import search
except ImportError:
	print("No module named 'google' found")

def terminaleBrowser():
    if sys.argv == 0:
        print(f"Usage: <script>, <arg>, <search>")
        quit()
    try:
        # to search
        query = str(sys.argv[2])
        if "o" in sys.argv:
            r = requests.get(str(sys.argv[2]))
            soup = BeautifulSoup(r.text, "lxml")
            print(soup.get_text())

        elif "s" in sys.argv:
            print("------------------------------------------------------------")
            print(f"SEARCH RESULTS FOR: {sys.argv[2]}")
            print("-----------------------------------------------------------")
            for j in search(query, tld="co.in", num=10, stop=20, pause=2):
                print(j)
        elif "sV" in sys.argv:
            print("------------------------------------------------------------")
            print(f"SEARCH RESULTS FOR: {sys.argv[2]}")
            print("-----------------------------------------------------------")
           
            for j in search(query, tld="co.in", num=10, stop=20, pause=3):
                try:
                    print(f"WEBSITE: {j}\n")
                    r = requests.get(str(j))
                    soup = BeautifulSoup(r.text, "lxml")
                    print(soup.get_text().replace("\n", '')[:300] + "...")
                    print("\n")
                    print("-----------------------------------------------------------------\n")
                except Exception as e:
                    continue
        else:
            r = requests.get(str(sys.argv[2]))
            soup = BeautifulSoup(r.text, "lxml")
            print(soup.prettify())
    except Exception as e:
        pass

terminaleBrowser()
