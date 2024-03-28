import re
import subprocess
def checkup_pae(ip: str):
    # Inicia o processo SSH
    ssh_process = subprocess.Popen(['ping', '-n', '4', ip],
                                stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    ssh_process.stdin.close()

    # Captura a saída padrão e a saída de erro
    stdout, stderr = ssh_process.communicate()

    # Verifica se ocorreu um erro
    error_message = stderr.strip() if stderr else None

    str_ping = stdout.decode('utf-8', errors='ignore')
    # Remove os caracteres de escape \r\n
    str_ping = str_ping.replace('\r', '')

    ping_treated = ''
    for txt in str_ping:
        ping_treated+= f"{txt}\n"

    # Ajusta a expressão regular para lidar com caracteres acentuados
    REGEX_PING_DEFAULT_WINDOWS = [
        rf"(?:Estatsticas do Ping para {ip}:\n)(.*\n.*\n.*\n.*)",
        rf"(?:Estatísticas do Ping para {ip}:\n)(.*\n.*\n.*\n.*)",
        rf"(?:Estatsticas do Ping para {ip}:\n)(.*\n.*)",
        rf"(?:Estatísticas do Ping para {ip}:\n)(.*\n.*)"
    ]
    teste = []
    # Aplica a expressão regular na string

    for index, rgx in enumerate(REGEX_PING_DEFAULT_WINDOWS):
        teste = re.findall(rgx, str_ping)
        if teste:
            break
            
    print(teste)


if __name__ == "__main__":
    ip = '192.168.100.1'
    checkup_pae(ip)
