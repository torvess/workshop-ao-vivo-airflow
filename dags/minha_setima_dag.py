from time import sleep
from airflow.decorators import dag, task
from datetime import datetime
from airflow.sdk import chain

@dag(
    dag_id='minha_setima_dag',
    start_date=datetime(2021, 1, 1),
    schedule='@daily',
    catchup=False
)
def pipeline():

    @task
    def primeira_atividade():
        return "ElyFlow nao precisa de XCOM"

    @task
    def segunda_atividade(response):
        print(response)
        sleep(2)
    
    @task
    def terceira_atividade():
        print("minha terceira atividade - Hello World")
        sleep(2)

    @task
    def quarta_atividade():
        print("pipeline finalizou")   

    t1 = primeira_atividade()
    t2 = segunda_atividade(t1)
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    chain(t1,t2,t3,t4)

pipeline()