import os
import subprocess
import urllib.request
import shutil

def download_and_install_chrome():
    # URL do arquivo RPM do Google Chrome para Linux
    chrome_rpm_url = 'https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm'

    # Nome do arquivo RPM a ser baixado
    rpm_filename = 'google-chrome.rpm'

    try:
        # Baixar o arquivo RPM do Google Chrome
        print(f"Baixando Google Chrome de: {chrome_rpm_url}")
        urllib.request.urlretrieve(chrome_rpm_url, rpm_filename)
        print("Download concluído.")

        # Extrair o conteúdo do RPM para o diretório atual
        print("Instalando Google Chrome localmente...")
        subprocess.run(['rpm2cpio', rpm_filename], check=True, stdout=subprocess.PIPE)
        subprocess.run(['cpio', '-idmv'], check=True, stdin=open('google-chrome.rpm', 'rb'))

        # Limpar arquivo RPM após a instalação
        os.remove(rpm_filename)

        print("Google Chrome foi instalado com sucesso localmente.")
    except Exception as e:
        print(f"Erro durante o processo de instalação do Google Chrome: {e}")

if __name__ == "__main__":
    download_and_install_chrome()
