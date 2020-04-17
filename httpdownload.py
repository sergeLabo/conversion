#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from urllib.request import Request, urlopen
from urllib.error import URLError
import socket


class HttpDownload:

    def request(self, someurl, timeout=2):
        """
        Télécharge une url.
        Retourne des bytes: https://bit.ly/2wau8j1 ou string vide
        """

        # Error with https://amipo.fr[requ
        try:
            req = Request(someurl)
        except:
            req = None

        response = None

        if req:
            # Simulation d'un navigateur
            req.add_header('User-agent', 'Multi lame 1.0')

            try:
                response = urlopen(req, timeout=timeout)
                response = response.read()
            except URLError as e:
                if hasattr(e, 'reason'):
                    print('Server is unreachable. Reason: ', e.reason)
                elif hasattr(e, 'code'):
                    print('The server couldn\'t fulfill the request.')
                    print('Error code: ', e.code)
            except socket.timeout as e:
                print('Request connection timeout, no response from server ')
            except:
                print("Final Error with", someurl, "Response None")

        return response

    def get_response(self, someurl, timeout=2):
        """
        Retourne la réponse de la requête, decodée si str
        """

        response = self.request(someurl, timeout=timeout)
        response = self.decode_or_not(response)
        return response

    def decode_or_not(self, response):
        """
        Decode utf-8 si text, rien si fichier.
        Donc text = utf-8, fichier = bytes
        """

        try:
            response = response.decode("utf-8")
        except:
            response = response

        return response


if __name__ == "__main__":
    hd = HttpDownload()
    hd.get_response("https://amipo.fr[requ")
