#!/usr/bin/python2
# -*- coding: UTF-8 -*-


from bs4 import BeautifulSoup
import urllib2


def prettylink(someurl):

    # Est-ce un fichier à télécharger ?
    fichier = False
    for ext in [".pdf", ".zip", ".gz", ".iso"]:
        if ext in someurl:
            fichier = True

    # Je cache toutes les erreurs
    try:
        site = someurl.split("/")[2]

        # Ce n'est pas un fichier
        if not fichier:
            try:
                response = urllib2.urlopen(someurl, timeout=5).read()
            except urllib2.URLError, e:
                response = None

            soup = BeautifulSoup(response, features="lxml")
            alt_text = soup.title.string

        # C'est un fichier
        else:
            alt_text = someurl.split("/")[-1]

        # Le texte complet
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
