FROM python:3.10.6
# Define o diretório de trabalho dentro do contêiner
WORKDIR /usr/src/app
# Copia os arquivos do projeto para o contêiner
COPY . /usr/src/app
# Instala as dependências do projeto usando o pip
RUN pip install --no-cache-dir -r requirements.txt
# Expor a porta 8000 para acesso externo
EXPOSE 8000
# Comando para executar a aplicação
CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
