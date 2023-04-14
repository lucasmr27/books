from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# Abre o navegador Firefox
driver = webdriver.Firefox()

# Abre o arquivo com os links a serem extraídos
with open('arquivos/links.txt', 'r') as file:
    links = file.readlines()

# Cria o arquivo CSV para salvar os dados
with open('arquivos/dados.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Loop pelos links
    for link in links:
        driver.get(link.strip())  # Acessa o link e remove os espaços em branco no início e fim da string
        dados = []

        # Utiliza o BeautifulSoup para extrair as informações da página
        soup = BeautifulSoup(driver.page_source, "html.parser")
        dados.append(soup.find("div", class_="col-sm-6 product_main").h1.string)  # Título do livro
        dados.append(soup.select_one("ul.breadcrumb > li:nth-of-type(3) > a").text) # Categoria do livro
        nota = soup("p")[2]['class'][1]  # Nota do livro

        notas_dict = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        
        dados.append(notas_dict[nota])

        dados += [dado.text for dado in soup.select("tr > td")]  # Informações do livro em uma lista
        dados[8] = dados[8][10:12].strip() # Remove o texto deixando apenas a quantidade na coluna de estoque
        for i in range(5, 8):
            dados[i] = dados[i][1:]

        writer.writerow(dados)  # Salva os dados no arquivo CSV

# Fecha o navegador Firefox
driver.quit()
