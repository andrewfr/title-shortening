from __future__ import print_function
import spacy
from pprint import pprint
from spacy.symbols import nsubj, dobj, VERB
import sys
import codecs
import pdb

nlp = spacy.load('en_core_web_sm')

def get_root(tokens):
    for token in tokens:
        if token.dep_ == u"ROOT":
            return token
    return None

def get_token_type(token, token_type):
    for child in token.children:
        if child.dep_ == token_type:
            return(child)
    return None

def gather(node):
    temp = []
    for child in node.children:
        temp.append(child)
        temp = temp + gather(child)
    return temp

def insertion_point(word, candidates):
    def get_first_left(word):
        w = None
        for w in word.lefts:
            break
        return w

    def get_first_right(word):
        w = None
        for w in word.rights:
            break
        return w

    left = get_first_left(word)
    right = get_first_right(word)

    for i in range(len(candidates)):
        if word.n_lefts >= 1 and word.n_rights >= 1:
            if candidates[i] == left and candidates[i+1] == right:
                return i
        elif word.n_lefts >= 1:
            if candidates[i] == left:
                return i 
        elif word.n_rights >= 1:
            if candidates[i] == right:
                return i 
    return -1

def get_root_direct_object(sentence):
    doc = nlp(sentence)

    root = get_root(doc)

    direct_object = get_token_type(root,"dobj")
    if not direct_object:
        return None

    gathered = gather(direct_object)
    i = insertion_point(direct_object, gathered)
    words = [word.text for word in gathered]
    words.insert(i + 1, direct_object.text)
    return " ".join(words)


def get_named_entities(title):
    doc = nlp(title)
    return [(ent.text, ent.label_) for ent in doc.ents]

def test_2():
    with codecs.open("../data/titles.txt",encoding="utf-8") as fp:
        titles = [ title.strip() for title in fp]
   
    for title in titles:
        print(get_named_entities(title))

def main():
    test_2()

if __name__ == "__main__":
    main()
