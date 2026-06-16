from time import sleep

def primeira_atividade():
    print("Primeira atividade")
    sleep(2)

def segunda_atividade():
    print("Segunda atividade")
    sleep(2)

def terceira_atividade():
    print("Terceira atividade")
    sleep(2)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print("Pipeline concluída")

if __name__ == "__main__":
    pipeline()