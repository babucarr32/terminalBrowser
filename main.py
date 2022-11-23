try:
    import sys
    import os
    import requests
    from bs4 import BeautifulSoup
    from googlesearch import search
except ImportError:
	print("No module named 'google' found")

def terminaleBrowser():
    # to search
    query = "A computer science portal"

    if "o" in sys.argv:
        r = requests.get(str(sys.argv[2]))
        soup = BeautifulSoup(r.text, "lxml")
        print(soup.get_text())
    # for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        # print(j)

terminaleBrowser()
