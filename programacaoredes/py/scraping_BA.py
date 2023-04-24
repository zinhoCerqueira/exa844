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


def checaEstado(estado):
    url = "https://www.clickbus.com.br/onibus"

    locaisCertos = []
    total_cidade2 = 0

    for cidade1 in estado:
        for cidade2 in estado:

            total_cidade2 = total_cidade2 + 1
            percentual = total_cidade2 / (len(estado) ** 2) * 100

            print(f"{percentual:.2f}% ")

            origin = cidade1
            destination = cidade2

            urlFinal = url + "/" + origin + "-ba/" + destination + "-ba"
            print(urlFinal)

            session = requests.Session()
            response = session.get(urlFinal)
            soup = BeautifulSoup(response.content, 'html.parser')

            divsPai = soup.find_all('div', {"class": "search-result-item"})

            if(divsPai and response.status_code == 200) :
                locaisCertos.append(urlFinal)
                print(urlFinal)
            
            elif (response.status_code == 403):
                sys.exit(1)
            else:
                print(response.status_code)
            
    with open('lista.txt', 'w') as arquivo:
        for item in locaisCertos:
            arquivo.write("%s\n" % item)

                    
            

            


# START ------------------------------------------------------------------------------------------------------------------ START #
# START ------------------------------------------------------------------------------------------------------------------ START #
# START ------------------------------------------------------------------------------------------------------------------ START #

# Para este caso inicial, foi optado por escolher apenas as cidades dos nordestes, mas é uma opção facilmente modificavel.

cidades_nordeste = []

BA = []


url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
response = requests.get(url)

# Aqui vamos formatar cada nome da cidade para poder concatenar com a url e fazer a pesquisa de forma correta.

# deixar todas as letras minusculas
# retirar acentos e caracteres especiais
# retirar espaços e mudar para traços


if response.status_code == 200:
    data = json.loads(response.content)
    for city in data:
        sigla = city["microrregiao"]["mesorregiao"]["UF"]["sigla"]
        sigla = sigla.lower()
        if (sigla == "ba"):
            revisada = city["nome"]
            revisada = revisada.lower()
            revisada = non_ascii_to_ascii(revisada)
            revisada = re.sub(r"\s+", "-", revisada)
            BA.append(revisada)
            time.sleep(0.1)

else:
    print("Erro ao acessar a API do IBGE")



checaEstado(BA)

