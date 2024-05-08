# Use uma imagem base do Python
FROM python:3.8

# Instale as dependências necessárias
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    curl

# Adicione a chave de assinatura do Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adicione o repositório do Google Chrome ao apt
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Instale o Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Configuração do ambiente Python
WORKDIR /app
COPY requirements.txt /app

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Defina o comando padrão
CMD ["python", "app.py"]
