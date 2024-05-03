import os
import shutil
import tkinter as tk
from tkinter import filedialog
from typing import Union
import traceback
import requests

def select_file_deployment():
    root = tk.Tk()
    # Ocultar a janela principal
    root.withdraw()  

    # Abrir a janela de seleção de arquivos
    files_selected = filedialog.askopenfilenames(title="DEPLOYMENT EVA - Selecione os arquivos para implantar")
    return files_selected


def deployment_files(machine_source: str, files_source: Union[tuple, str], machines_target: list, directory_target: str):
    for machine_target in machines_target:
        path_target = f"{machine_target}\\{directory_target}"

        try:
            # Verificar se o destino remoto é acessível
            if os.path.exists(path_target):
                # Verificar se há arquivos para copiar
                if files_source:
                    for path_source in files_source:
                        filename = os.path.basename(path_source)
                        full_path_target = os.path.join(path_target, filename)
                        
                        # Copiar o arquivo da pasta de origem para a pasta de destino remota
                        shutil.copy2(path_source, full_path_target)
                    
                    print(f"Arquivos copiados de {machine_source} para maquina {machine_target} com sucesso para o destino remoto.")
                else:
                    print(f"Nenhum arquivo selecionado para cópia. Deployment não realizado na maquina {machine_target}")
            else:
                print(f"Destino remoto '{machine_target}\\{directory_target}' não está acessível.")
        
        except Exception as e:
            print(f"Erro durante a cópia de arquivos: {str(traceback.format_exc())}")


def main():
    # Abrir janela de seleção de arquivos
    files_selected = select_file_deployment()

    if not files_selected:
        print("Nenhum arquivo selecionado. Deployment cancelado.")
        return

    # Definir informações do destino remoto (máquina e pasta)
    machines_target_remote = [
        "\\SGXTP0027CLD\\MotorV2\\Configs",
        "\\SGXTP0028CLD\\MotorV2\\Configs",
        "\\SGXTP0029CLD\\MotorV2\\Configs",
        "\\SGXTP0030CLD\\MotorV2\\Configs",
        "\\SGXTP0031CLD\\MotorV2\\Configs",
        "\\SGXTP0032CLD\\MotorV2\\Configs",
        "\\SGXTP0033CLD\\MotorV2\\Configs",
        "\\SGXTP0034CLD\\MotorV2\\Configs",
        "\\SGXTP0041CLD\\MotorV2\\Configs",
        "\\SGXTP0042CLD\\MotorV2\\Configs",
        "\\SGXTP0043CLD\\MotorV2\\Configs",
        "\\SGXTP0045CLD\\MotorV2\\Configs"
    ]
    directory_target_remote = "\\Parametros"

    # Copiar os arquivos selecionados para a pasta de destino remota na máquina remota
    deployment_files("SGXTP0035CLD", files_selected, machines_target_remote, directory_target_remote)


if __name__ == "__main__":
    main()

    message_end =  "\n=============================================================================\n"
    message_end += "                                  Encerrado\n"
    message_end += "                         Aperte qualquer tecla para sair                "
    message_end += "\n============================================================================="
    input(message_end)