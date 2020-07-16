# Maga Crawler
Crawler para loja online da MagazineLuiza

## Instalação

```
$ docker-compose build
$ docker-compose up
```

## Inicializando o crawler

```
$ docker exec -it maga_crawler_web_1 python crawler/main.py
```

## API

http://localhost:5000/

Lista de todos os produtos crawleados juntamente com o total.

Filtrar por SKU:

- http://localhost:5000/?sku=abc

Filtrar por EAN:

- http://localhost:5000/?ean=12345


http://localhost:5000/clean

Limpa a base de dados

## TODO

- Checagem de índices
- Relatórios (market share e ruptura)
- Calculo da taxa de juros dos produtos
