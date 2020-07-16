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

https://localhost:5000/

Lista de todos os produtos crawleados juntamente com o total

https://localhost:5000/clean

Limpa a base de dados

## TODO

- Checagem de índices
- Relatórios (market share e ruptura)
