# Análise de sortimento para lojas online

Crawler para análise de sortimento de departamentos para lojas online.

Lojas implementadas:
 - Magazine Luiza

## Instalação

```
$ docker-compose build
$ docker-compose up
```

## Inicializando o Crawler

```
$ docker exec -it maga_crawler_web_1 python crawler/main.py
```

## API

### Consultas

Lista de todos os produtos crawleados juntamente com o total.

- http://localhost:5000/list

Consultar por SKU:

- http://localhost:5000/list?sku=abc

Consultar por EAN:

- http://localhost:5000/list?ean=12345

### Relatório

Relatório unificado (default: mondial):

- http://localhost:5000/report


Filtrar por marca:

- http://localhost:5000/report?marca=mondial

### Admin

Limpar a base de dados:

- http://localhost:5000/clean


## TODO

- Checagem de índices do crawler (Maga)