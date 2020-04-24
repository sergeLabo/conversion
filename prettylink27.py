#!/usr/bin/python2
# -*- coding: UTF-8 -*-


from bs4 import BeautifulSoup
import urllib2

def prettylink(someurl):

    try:
        response = urllib2.urlopen(someurl).read()
        site = someurl.split("/")[2]
        if ".pdf" not in someurl:
            someurl = someurl.replace("\\", "")
            soup = BeautifulSoup(response, features="lxml")
            alt_text = soup.title.string
        else:
            alt_text = someurl.split("/")[-1]
        new_text =  "[[" + someurl + "|" + site + ": " + alt_text + "]]"
    except:
        new_text =  "[[" + someurl + "|]]"

    print(new_text)
    return new_text


if __name__ == "__main__":

    import os
    from sys import argv

    error = """
Usage:
Ouvrir un terminal dans le dossier de ce script:

python2 conversion.py url

avec

url = une url complète

exemple:
url = https://labomedia.org/
"""

    try:
        url = argv[1]
    except:
        print(error)

        os._exit(0)

    prettylink(url)
