from bs4 import BeautifulSoup
import requests


total = 0

with open('lista.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        total = total+1
        percentual = total / (1606) * 100

        print(f"{percentual:.2f}% ")

        session = requests.Session()
        response = session.get(linha)
        soup = BeautifulSoup(response.content, 'html.parser')

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            divsPai = soup.find_all('div', {"class": "search-result-item"})
