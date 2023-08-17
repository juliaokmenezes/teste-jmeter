# experimentação sprint 05

Esse experimento consiste da análise entre as versões LocalStorage e S3 do Nutbox. 

## Instruções para rodar os testes

A aplicação NutBox será estressada usando a ferramenta JMeter, as métricas serão coletadas pelo Prometheus e os dados serão visualizados usando o Grafana.

Em `grafana`, temos nossas configurações de grafana.

Em `jmeter` temos as configurações de testes .jmx e os arquivos a serem carregados.

Em `prometheus` temos os arquivos de configuração para coletar as métricas.

## Dependências
A seguinte dependência é necessária para executar os testes:

- [Docker](https://docs.docker.com/engine/).

## Testando
Para testar o NutBox, você precisa executar os contêineres que contêm os serviços JMeter, Prometheus e Grafana:
```
docker compor
```

Em seguida, você precisa entrar no container Jmeter e dar o comando para rodar o teste escolhido:
```
docker exec -it [jmeter-container-id] bash
```

Se você não conhece o ID do contêiner, pode descobrir com o seguinte comando:
```
docker ps
```

Dentro do container, basta executar este comando:
```
jmeter -n -t scripts/[script.jmx] -l ./results/[result-file-name.csv]
```

## License

--
