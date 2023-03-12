import urllib.request
from bs4 import BeautifulSoup
import html
import io

soup1 = BeautifulSoup("", "html.parser")

html_tag = soup1.new_tag("html")
soup1.append(html_tag)
body_tag = soup1.new_tag("body")
html_tag.append(body_tag)

with open("C:\\Users\\jader\\Documents\\GitHub\\exa844\\atividade_1\\seeds.txt", "r") as file:
  for line in file:

    page = urllib.request.urlopen(line)
    html = str(page.read().decode('utf-8'))
    soup = BeautifulSoup(html, 'lxml')
    titulo = soup.title.string
    img = soup.find('img')

    if img is not None:
      if "https://" in img.attrs.get("src"):
        src1 = img.attrs.get("src")
      else:
        src1 = line[:-1]+img.attrs.get("src")

      print(titulo)
      print(src1)
      print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

      title_tag = soup1.new_tag("h1")
      title_tag.string = titulo
      body_tag.append(title_tag)
    
      # Crie uma tag 'img' para a imagem e adicione-a ao objeto 'body'
      img_tag = soup1.new_tag("img", src=src1)
      body_tag.append(img_tag)
      with io.open("galera.html", "w", encoding="utf-8") as file:
        file.write(soup1.prettify())

