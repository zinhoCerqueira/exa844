import re
import json
import requests
import unicodedata
from bs4 import BeautifulSoup

import time

# Função para formatar corretamente os nomes das cidades.
def non_ascii_to_ascii(string: str) -> str:
    ascii_only = unicodedata.normalize('NFKD', string)\
        .encode('ascii', 'ignore')\
        .decode('ascii')
    return ascii_only


def checaEstado(estado, cidades_nordeste):
    url = "https://www.clickbus.com.br/onibus"

    passagens  = []

    for i in range(len(estado)):
        for j in range(i+1 ,len(cidades_nordeste)):

            origin = estado[i]
            destination = cidades_nordeste[j]

            urlFinal = url + "/"+ origin + "/" + destination
            print(url + "/"+ origin + "/" + destination)

            session = requests.Session()
            response = session.get(urlFinal)
            soup = BeautifulSoup(response.content, 'html.parser')

            divsPai = soup.find_all('div', {"class": "search-result-item"})

            for divFilho in divsPai:
                elemento = divFilho.find("div",{"class":"company"})
                empresa = elemento['content']

                elemento = divFilho.find("div", {"class": "hour"})
                elemento = elemento.find("time", {"class": "departure-time"})
                hrr_saida = elemento['data-time']

                elemento = divFilho.find("div", {"class": "hour"})
                elemento = elemento.find("time", {"class": "return-time"})
                hrr_chegada = elemento['data-time']

                elemento = divFilho.find("div", {"class": "route-type"})
                elemento = elemento.find("div", {"class": "duration"})
                elemento = elemento.find("time")
                tempo_de_viagem = elemento.text

                elemento = divFilho.find("div", {"class": "service-class"})
                elemento = elemento.find("span")
                tipo = elemento.text

                elemento = divFilho.find("div", {"class": "price"})
                preco = elemento['data-price']

                elemento = divFilho.find("div", {"class": "bus-stations"})
                elemento = elemento.find("p", {"class": "station-departure"})
                origem = elemento.text

                elemento = divFilho.find("div", {"class": "bus-stations"})
                elemento = elemento.find("p", {"class": "station-arrival"})
                destino = elemento.text
                

                dados = {
                    "empresa": empresa,
                    "saida": hrr_saida,
                    "chegada": hrr_chegada,
                    "tempo_de_viagem": tempo_de_viagem,
                    "tipo": tipo,
                    "preco": preco,
                    "origem": origem,
                    "destino": destino
                }

                passagens.append(dados)

                with open("dados.json", "a") as arquivo:
                    arquivo.write(json.dumps(passagens, indent=2))
                    

                print(dados)
                print("")
                print("-----------------------------------")
                dados = {}


# START ------------------------------------------------------------------------------------------------------------------ START #
# START ------------------------------------------------------------------------------------------------------------------ START #
# START ------------------------------------------------------------------------------------------------------------------ START #

# Para este caso inicial, foi optado por escolher apenas as cidades dos nordestes, mas é uma opção facilmente modificavel.

cidades_nordeste = []

BA = []
PI = []
MA = []
CE = []
RN = []
PB = []
PE = []
AL = []
SE = []

x= []

url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
response = requests.get(url)

# Aqui vamos formatar cada nome da cidade para poder concatenar com a url e fazer a pesquisa de forma correta.

# deixar todas as letras minusculas
# retirar acentos e caracteres especiais
# retirar espaços e mudar para traços


if response.status_code == 200:
    data = json.loads(response.content)
    for city in data:
        if(city["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"] == "Nordeste"):

            revisada = city["nome"]
            revisada = revisada.lower()
            revisada = non_ascii_to_ascii(revisada)
            revisada = re.sub(r"\s+", "-", revisada)

            # Adiciona a cidade no conjunto de cidades do Nordeste, e noconjunto de cidades referentes a estado.
            sigla = city["microrregiao"]["mesorregiao"]["UF"]["sigla"]
            sigla = sigla.lower()

            revisada = revisada + "-" + sigla
            cidades_nordeste.append(revisada)

            if(sigla == "ba"):
                BA.append(revisada)
            elif(sigla == "pi"):
                PI.append(revisada)
            elif(sigla == "ma"):
                MA.append(revisada)
            elif(sigla == "ce"):
                CE.append(revisada)
            elif(sigla == "rn"):
                RN.append(revisada)
            elif(sigla == "pb"):
                PB.append(revisada)
            elif(sigla == "pe"):
                PE.append(revisada)
            elif(sigla == "al"):
                AL.append(revisada)
            elif(sigla == "se"):
                SE.append(revisada)

else:
    print("Erro ao acessar a API do IBGE")

checaEstado(BA, cidades_nordeste)
# checaEstado(PI, cidades_nordeste)
# checaEstado(MA, cidades_nordeste)
# checaEstado(CE, cidades_nordeste)
# checaEstado(RN, cidades_nordeste)
# checaEstado(PB, cidades_nordeste)
# checaEstado(PE, cidades_nordeste)
# checaEstado(AL, cidades_nordeste)
# checaEstado(SE, cidades_nordeste)