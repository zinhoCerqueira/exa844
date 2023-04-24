import json
from bs4 import BeautifulSoup
import requests

dados = []
total = 0

with open("py\listafiltrada_BA.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        total = total + 1
        percentual = total / 1606 * 100
        print(f"{percentual:.2f}% ")

        session = requests.Session()
        response = session.get(linha)
        soup = BeautifulSoup(response.content, 'html.parser')

        divsPai = soup.find_all('div', {"class": "search-result-item"})

        if (divsPai and response.status_code == 200):

            divsPai = soup.find_all('div', {"class": "search-result-item"})

            for divFilho in divsPai:
                elemento = divFilho.find("div", {"class": "company"})
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

                dados_viagem = {
                    "empresa": empresa,
                    "saida": hrr_saida,
                    "chegada": hrr_chegada,
                    "tempo_de_viagem": tempo_de_viagem,
                    "tipo": tipo,
                    "preco": preco,
                    "origem": origem,
                    "destino": destino
                }

                dados.append(dados_viagem)
        else:
            print("O PIOR")
            print(response.status_code)
            print(linha)

json_string = json.dumps(dados)
with open("dadosViagens_BA.txt", "w") as arquivo:
    # Escreve a string no arquivo
    arquivo.write(json_string)

with open("dadosjson.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)
