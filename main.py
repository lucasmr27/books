from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


url = "http://books.toscrape.com/catalogue/page-1.html"

driver = webdriver.Firefox()
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")

links = []

while True:
    # Extrair todos os links de livro da página
    product_links = soup.select('article > div > a')
    for link in product_links:
        links.append(link['href'])
    
    # Verificar se há mais páginas
    next_links = driver.find_elements(By.LINK_TEXT, 'next')
    if len(next_links) == 0:
        break
    
    # Navegar para a próxima página
    next_links[0].click()
    soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()

# Imprimir a lista de links
for link in links:
    print(link)
