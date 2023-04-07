from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


url = "http://books.toscrape.com/catalogue/page-1.html"

driver = webdriver.Firefox()
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")

ultima_pagina = False

while(not ultima_pagina):
    try:
        # Extrair todos os links da página
        for heading in soup.select('h3'):
            for link in heading.select('a'):
                print(link['href'])
        # encontrar o elemento "next" pelo link de texto
        next_link = driver.find_element(By.LINK_TEXT, 'next')
        # obter o valor do atributo href do elemento "next"
        next_url = next_link.get_attribute("href")
        # navegar para a próxima página
        driver.get(next_url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
    except:
        ultima_pagina = True
