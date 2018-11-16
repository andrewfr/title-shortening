import codecs
import json
import sys

from rules import get_root_direct_object

def main():
    with codecs.open("../data/references.json","r",encoding="utf-8") as fp:
        title_barcodes = json.load(fp)

    with codecs.open("titles.txt","w",encoding="utf-8") as fp:
        for title in get_titles(title_barcodes):
            fp.write(title + "\n")
    """
    for title in get_titles(title_barcodes):
        dobj = get_root_direct_object(title)
        if dobj:
            print title,'*', dobj, '*'
    """

def write_titles(titles):
    with codecs.open("titles.txt","w",encoding="utf-8") as fp:
        fp.write(titles + "\n")

def get_titles(title_barcodes):
    return [title for title, _ in title_barcodes]

if __name__ == "__main__":
    main()

