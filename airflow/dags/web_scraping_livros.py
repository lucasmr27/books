from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define a DAG com nome 'scraping_books', data de início em 09 de abril de 2023,
# e com intervalo de execução semanal (a cada segunda-feira).
with DAG('scraping_books', start_date=datetime(2023, 4, 9),
         schedule_interval='0 0 * * 1', catchup=True) as dag:
    
    # Define a primeira tarefa, que será responsável por capturar os links dos livros a serem raspados.
    captura_links = PythonOperator(
        task_id='captura_links',
        python_callable=exec(open('C:/Users/lucas/OneDrive/Documentos/Estudos/books/captura_links.py').read())
    )

    # Define a segunda tarefa, que será responsável por extrair os dados dos livros a partir dos links coletados.
    extrai_dados = PythonOperator(
        task_id='extrai_dados',
        python_callable=exec(open('C:/Users/lucas/OneDrive/Documentos/Estudos/books/extrai_dados.py').read())
    )

    # Define a terceira tarefa, que será responsável por inserir os dados dos livros no banco de dados.
    insere_bd = PythonOperator(
        task_id='insere_bd',
        python_callable=exec(open('C:/Users/lucas/OneDrive/Documentos/Estudos/books/insere_bd.py').read())
    )
    
    # Define que as tarefas devem ser executadas em sequência, na ordem em que foram definidas.
    captura_links >> extrai_dados >> insere_bd