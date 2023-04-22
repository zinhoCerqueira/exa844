import re
import json
import requests
import unicodedata
from bs4 import BeautifulSoup
import sys

import time

# Função para formatar corretamente os nomes das cidades.
def non_ascii_to_ascii(string: str) -> str:
    ascii_only = unicodedata.normalize('NFKD', string)\
        .encode('ascii', 'ignore')\
        .decode('ascii')
    return ascii_only

def checaEstado():
    haveLine = True
    while haveLine:
        with open("exa844\programacaoredes\py\lista_BA.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            
        if(linhas):     
            session = requests.Session()
            response = session.get(linhas[0])

            print(response.status_code)
            if response.status_code == 200: 
                soup = BeautifulSoup(response.content, 'html.parser')
                divsPai = soup.find_all('div', {"class": "search-result-item"})

                print(linhas[0])
                if(divsPai):
                    print("A página tem dados.")   
                    with open("exa844\programacaoredes\py\lista_BA.txt", "a") as arquivo:
                        localCerto = linhas.pop(0)
                        arquivo.writelines(localCerto)
                    with open("exa844\programacaoredes\py\lista_BA.txt", "w") as arquivo:
                        arquivo.writelines(linhas)
                else:
                    print("A página está vazia.")
                    linhas.pop(0)
                    with open("exa844\programacaoredes\py\lista_BA.txt", "w") as arquivo:
                        arquivo.writelines(linhas)

            else:
                print("Fomos barrados")
                sys.exit(0)
        else:
            haveLine = False


# START ------------------------------------------------------------------------------------------------------------------ START #
# START ------------------------------------------------------------------------------------------------------------------ START #
# START ------------------------------------------------------------------------------------------------------------------ START #

checaEstado()