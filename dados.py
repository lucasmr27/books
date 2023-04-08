from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import os

driver = webdriver.Firefox()

# Ler links de um arquivo txt
with open('arquivos/links.txt', 'r') as file:
    links = file.readlines()

for link in links:
    driver.get(link)
    dados = []
    soup = BeautifulSoup(driver.page_source, "html.parser")
    dados.append(soup.find("div", class_="col-sm-6 product_main").h1.string)
    dados.append(soup.find("p", class_="instock availability").text.strip())
    print(dados)

driver.quit()