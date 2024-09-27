from apscheduler.schedulers.background import BackgroundScheduler
import os
import shutil
import time
from datetime import datetime

def limpar_pasta(pasta):
    """Remove todos os arquivos e subpastas em um diretório específico."""
    try:
        for item in os.listdir(pasta):
            item_path = os.path.join(pasta, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Remove diretórios
            else:
                os.remove(item_path)  # Remove arquivos
        print(f"{datetime.now()}: Pasta {pasta} limpa com sucesso.")
    except Exception as e:
        print(f"{datetime.now()}: Ocorreu um erro ao limpar a pasta: {e}")

def a():
    # Implementação da função a
    while True:
        time.sleep(1)
        print("Executando a...")

def b():
    # Implementação da função b
    while True:
        time.sleep(1)
        print("Executando b...")

if __name__ == '__main__':
    pasta_chrome = "/app/tmp/chrome_user_data"

    # Cria e inicia o agendador
    scheduler = BackgroundScheduler()
    scheduler.add_job(limpar_pasta, 'cron', args=[pasta_chrome], hour=0, minute=0)

    # Inicia o agendador
    scheduler.start()

    # Cria threads para as funções a e b
    thread_a = threading.Thread(target=a)
    thread_b = threading.Thread(target=b)

    # Inicia as threads
    thread_a.start()
    thread_b.start()

    # Aguarda as threads terminarem (se necessário)
    thread_a.join()
    thread_b.join()
