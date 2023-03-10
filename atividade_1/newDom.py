import urllib.request
from bs4 import BeautifulSoup
import html

print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<meta charset='UTF-8' />")
print(" <meta http-equiv='X-UA-Compatible' content='IE=edge' />")
print("<meta name='viewport' content='width=device-width, initial-scale=1.0' />")
print("<title>Atividade 5</title>")
print("</head>")
print("<body>")

with open("C:\\Users\\jader\\Documents\\GitHub\\exa844\\atividade_1\\seeds.txt") as file:
  for line in file:

    page = urllib.request.urlopen(line)

    html = str(page.read().decode('utf-8'))

    soup = BeautifulSoup(html, 'lxml')

    # # print("++++++++++++++++++++++++++++++++++++++") 
    # for img in soup.find_all('img'):
    #   # print("src: ", img.attrs.get("src"))
    #   # print("++++++++++++++++++++++++++++++++++++++")
    #   # print("")
    #   break

    for img in soup.find_all('img'):
      img = img.attrs.get("src")
      if "https://" in img:
        print("<img width='500px' src='" + img + "'/>")
      else:
        print(f"<img width='500px' src='{line[:-1]+img}'/>")

