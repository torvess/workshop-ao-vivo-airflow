from time import sleep
from loguru import logger
from libcst import While

logger.add('execution_logs.log', format="{time} - {level} - {message}", level="INFO")

def primeira_atividade():
    logger.info("Primeira atividade")
    sleep(2)

def segunda_atividade():
    logger.info("Segunda atividade")
    sleep(2)

def terceira_atividade():
    logger.info("Terceira atividade")
    sleep(2)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline concluída")

if __name__ == "__main__":
    while True:
        pipeline()
        sleep(5)