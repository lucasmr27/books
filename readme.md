# Web Scraping de Catálogo de Livros usando Selenium e BeautifulSoup

Este é um exemplo simples de como fazer web scraping de um catálogo de livros utilizando as bibliotecas Selenium e BeautifulSoup em Python.

O código faz a extração dos links de produtos do catálogo de livros do site [http://books.toscrape.com](http://books.toscrape.com/), navegando pelas páginas do catálogo e coletando os links de cada livro. Os links são armazenados em uma lista e, em seguida, são salvos em um arquivo de texto na pasta "arquivos" do projeto.


## Como utilizar

Para utilizar o código, é necessário ter o Python 3 instalado, juntamente com as bibliotecas Selenium e BeautifulSoup.


### Instalando as bibliotecas

Para instalar as bibliotecas, abra um terminal ou prompt de comando e execute os seguintes comandos:

```
pip install selenium
```
```
pip install beautifulsoup4
```


### Executando o código

Para executar o código, basta abrir o terminal ou prompt de comando e navegar até a pasta onde o arquivo `main.py` está localizado. Em seguida, execute o seguinte comando:

```
python main.py
```

O código irá iniciar a extração dos links e salvá-los em um arquivo de texto na pasta "arquivos".