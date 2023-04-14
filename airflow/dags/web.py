from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 5),
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'executa_scripts',
    default_args=default_args,
    description='Executa os três scripts em ordem',
    schedule='0 9 * * 1',
    catchup=True
) as dag:

    t1 = BashOperator(
        task_id='captura_links',
        bash_command='python /home/lucas/projetos/books/captura_links.py',
    )

    t2 = BashOperator(
        task_id='extrai_dados',
        bash_command='python /home/lucas/projetos/books/extrai_dados.py',
    )

    t3 = BashOperator(
        task_id='insere_bd',
        bash_command='python /home/lucas/projetos/books/insere_bd.py',
    )

    t1 >> t2 >> t3