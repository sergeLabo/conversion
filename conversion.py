#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from sys import argv

from bs4 import BeautifulSoup

from httpdownload import HttpDownload

TIMEOUT = 60


class LinkConversion:

    def __init__(self, link):
        self.link = link
        self.bad_link = 0
        self.no_title = 0

        self.new_text = self.get_new_text()
        print(self.new_text)

    def get_new_text(self):
        # http://fing.org/?Le-succes-de-la-Montre-verte
        try:
            site = self.link.split("/")[2]
        except:
            site = "Pas de site"

        # Création d'un texte propre équivalent au self.link
        alt_text = self.get_alt_text()

        new_text =  "[[" + self.link + "|" + site + ": " + alt_text + "]]"

        return new_text

    def get_alt_text(self):

        if ".pdf" not in self.link:
            self.link = self.link.replace("\\", "")
            text = HttpDownload().get_response(self.link, timeout=TIMEOUT)

            bad_link, no_title = 0, 0

            try:
                soup = BeautifulSoup(text, features="lxml")
            except:
                bad = "<title>Mauvaise url</title>"
                self.bad_link = 1
                soup = BeautifulSoup(bad, features="lxml")

            try:
                alt_text = soup.title.string
            except:
                self.no_title = 1
                alt_text = "Pas de titre"

        else:
            alt_text = self.link.split("/")[-1]

        # TODO: pourquoi parfois None ?
        if not alt_text:
            alt_text = "Pas de titre: None"

        return alt_text


if __name__ == "__main__":

    error = """
Usage:
Ouvrir un terminal dans le dossier de ce script:

python3 conversion.py url

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

    LinkConversion(url)
