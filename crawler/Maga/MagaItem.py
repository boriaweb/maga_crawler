from scrapy.item import Item, Field

class MagaItem(Item):
    ean = Field()
    sku = Field()
    produto = Field()
    departamento = Field()
    categoria = Field()
    subcategoria = Field()
    marca = Field()
    atributos = Field(tipo=str, atributo=str)
    estoque = Field()
    preco = Field()
    parcelas = Field()
    valor_parcela  = Field()
    taxa_juros = Field()
    url  = Field()
    imagem  = Field()