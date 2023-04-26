# Web Scraping de livros com Python e PostgreSQL

Este projeto consiste em um conjunto de scripts Python para realizar web scraping de uma livraria online, armazenar os dados coletados em um banco de dados PostgreSQL e automatizar esse processo com o Airflow.

## Objetivo do projeto e por que ele é importante

O objetivo deste projeto é demonstrar habilidades em web scraping, banco de dados e automação com Airflow. A realização de web scraping é uma técnica importante para coletar dados de fontes online para análise e uso em vários projetos. O uso de um banco de dados permite armazenar grandes quantidades de dados de maneira organizada e eficiente para análise futura. A automação do processo com o Airflow aumenta a eficiência e a escalabilidade do projeto.

## Tecnologias utilizadas

-   Python
-   Selenium
-   Beautiful Soup
-   PostgreSQL
-   Airflow

## Funcionamento do projeto

O projeto consiste em três scripts Python. O primeiro script faz a coleta de links para cada livro na livraria online. O segundo script acessa cada link e extrai os dados de cada livro, salvando-os em um arquivo CSV. O terceiro script lê o arquivo CSV e insere os dados em uma tabela do banco de dados PostgreSQL.

Para automatizar o processo, o Airflow é usado para agendar e executar os scripts em ordem uma vez por semana. O primeiro script é executado na segunda-feira, o segundo na terça-feira e o terceiro na quarta-feira.

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

`pip install -r requirements.txt`

Certifique-se de configurar o banco de dados PostgreSQL de acordo com o arquivo `config.py`.

## Como usar

Para executar o projeto manualmente, execute os seguintes comandos em ordem:

~~~ 
python captura_links.py
~~~
~~~
python extrai_dados.py
~~~
~~~
python insere_bd.py
~~~

Para executar o projeto com o Airflow, inicie o webserver do Airflow e adicione a dag `web.py` na pasta `dags`.



### Referencias
* [Proposta](https://medium.com/@meigarom/o-projeto-de-data-engineering-para-o-seu-portf%C3%B3lio-c186c7191823)