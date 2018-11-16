from __future__ import print_function

import codecs
import json
from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')

def get_titles(doc):
    titles = doc.find_all('div', class_="title")
    return [title.string for title in titles]

def main():
    with codecs.open("../data/10000.html", "r", encoding="utf-8") as fp:
        soup = BeautifulSoup(fp, 'lxml')

    titles = get_titles(soup)

    with codecs.open("../data/titles.txt", "w", encoding="utf-8") as fp:
        for title in titles:
            fp.write(title + "\n")

if __name__ == "__main__":
    main()

