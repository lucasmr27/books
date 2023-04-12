# Web Scraping de livros utilizando Selenium e BeautifulSoup

Este projeto tem como objetivo realizar a extração de dados de livros do website [books.toscrape.com](http://books.toscrape.com/) utilizando a biblioteca Selenium em conjunto com o BeautifulSoup. Os dados extraídos são salvos em um arquivo CSV e posteriormente inseridos em um banco de dados PostgresSQL.

## Pré-requisitos

Para executar o projeto, é necessário ter o seguinte software instalado:

-   [Python 3](https://www.python.org/downloads/)
-   [Selenium](https://selenium-python.readthedocs.io/installation.html)
-   [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
-   [Psycopg2](https://pypi.org/project/psycopg2/)

Além disso, é necessário ter um banco de dados PostgresSQL configurado.

## Executando o projeto

1.  Clone o repositório em sua máquina:
        
    `git clone https://github.com/lucasmr27/books.git`
    
2.  Instale as bibliotecas necessárias:
    
    `pip install -r requirements.txt`
    
3.  Configure as informações do banco de dados no arquivo `config.py`.
    
4.  Execute o primeiro script `captura_links.py` para capturar todos os links dos livros:
    
    `python captura_links.py`
    
5.  Execute o segundo script `extrai_dados.py` para extrair os dados dos livros e salvar em um arquivo CSV:
    
    `python extrai_dados.py`
    
6.  Execute o terceiro script `insere_bd.py` para inserir os dados no banco de dados PostgresSQL:
    
    `python insere_bd.py`


### Referencias
* [Proposta](https://medium.com/@meigarom/o-projeto-de-data-engineering-para-o-seu-portf%C3%B3lio-c186c7191823)