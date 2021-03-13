#!/usr/bin/python3

from googlesearch import search, get_page
from sys import argv
import webbrowser

if __name__ == "__main__":

    words, num, o = [], 10, False
    
    for i in range(1, len(argv)):
        arg = argv[i]
        if arg == "-n":
            i += 1
            num = int(argv[i])
        elif arg == "-o":
            o = True
        elif not arg.startswith("-"):
            words.append(argv[i])
    
    print("wie wäre es mit einem dieser Links?")
    for res in search("Geschenk " + " ".join(words), tld="co.in", num=num, stop=num, pause=2):
        print(res)
        if o: webbrowser.open(res, new=2)

