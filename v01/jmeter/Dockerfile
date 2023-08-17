# Usando a imagem base do JMeter
FROM justb4/jmeter:5.5

RUN apk add openssh

# Copiando um plugin .jar para o diretório de plugins no container
COPY ext/jmeter-prometheus-plugin-0.6.2.jar /opt/apache-jmeter-5.5/lib/ext

# Adicionando um ip pro Prometheus no arquivo de configuração do JMeter
RUN echo "prometheus.ip=nutbox-jmeter" >> /opt/apache-jmeter-5.5/bin/jmeter.properties
# Configurando formato do timestamp em arquivo csv
RUN echo "jmeter.save.saveservice.timestamp_format=yyyy/MM/dd HH:mm:ss" >> /opt/apache-jmeter-5.5/bin/jmeter.properties
# Configurando colunas extras para o arquivo csv resultante
RUN echo "sample_variables=operation,version,size" >> /opt/apache-jmeter-5.5/bin/user.properties

# Expondo a porta do JMeter
EXPOSE 9270

# Copiando scripts para diretório incluido no PATH
WORKDIR /usr/local/bin
COPY ./scripts/* .

# Criando arquivos para o teste
WORKDIR /jmeter/tests/files
RUN genfile.sh

# Definindo o diretório de trabalho padrão
WORKDIR /jmeter

# Copiando .pem file
COPY ./pem ./pem

# Definindo permissões para os arquivos .pem
RUN chmod 400 ./pem/*

# Copiando arquivos de teste para o JMeter
COPY ./tests /jmeter/tests/

# Definindo tamanho da HEAP para a JVM
ARG JVM_ARGS
ENV JVM_ARGS=${JVM_ARGS}

ENTRYPOINT run_file_size_test.sh
