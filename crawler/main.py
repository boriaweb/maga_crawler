import re, os, yaml, json, unidecode, pprint
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from MagaItem import MagaItem

settings_file_path = 'settings'
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)

class MagaSpider(scrapy.Spider):
    name = 'MagaCrawler'
    url_maga = 'https://www.magazineluiza.com.br/aquecedor-eletrico/ar-e-ventilacao/s/ar/arae/brand---mondial/'
    page = 1
    start_urls = [
        url_maga
    ]
    def clean_json(self, json_str):
        #remove comentarios
        json_str = re.sub(re.compile(",\s//(.*)" ) ,"," ,json_str)
        
        json_str = json_str.strip()[:-1]
        t = yaml.safe_load(json_str)
        return t         
    def format_string(self, dirty_str):
        clean_str = unidecode.unidecode(dirty_str)
        clean_str = clean_str.upper()
        return clean_str
    def parse_interna(self, response):
        full_json = response.xpath("//script[contains(., 'digitalData')]/text()").extract()
        full_json = ''.join(full_json).replace('digitalData = ', '')

        full_json = self.clean_json(full_json)
        page = full_json['page']
        
        variantions = page['productData']['variantions'][0]
        
        p_departamento = self.format_string(page['nameDepartment'])
        p_subcategoria = self.format_string(page['nameLine'])
        p_categoria = self.format_string(variantions['categories'][0]['subcategories'][-1]['name'])
        p_ean = variantions['ean']
        p_marca = self.format_string(page['productData']['brand'])
        p_preco = page['productData']['price']
        p_attributesTypes = page['productData']['attributesTypes']
        p_attributesValues = page['productData']['attributesValues']
        p_attributes = []
        for key, attribute in enumerate(p_attributesTypes):
            p_attributes.append({ 'tipo': self.format_string(attribute), 'atributo': p_attributesValues[key] })

        p_produto = page['product']['fullName']
        p_produto = ''.join(p_produto)
        p_produto = p_produto.replace("encodeURIComponent(", '').replace("'", '').replace(')', '')
        p_produto = self.format_string(p_produto)
        
        p_sku = page['product']['idSku']
        p_imagem = page['product']['imageUrl']
        p_qtd_parcelas = page['productData']['seller']['best_installment_plan']['installment_quantity']
        p_parcelas = page['productData']['seller']['best_installment_plan']['installment_amount']
        p_estoque = page['productData']['seller']['stock_count']
        p_url = response.request.url

        maga_item = MagaItem({
                'ean': p_ean,
                'sku': p_sku,
                'produto': p_produto,
                'departamento': p_departamento,
                'categoria': p_categoria,
                'subcategoria': p_subcategoria,
                'marca': p_marca,
                'atributos': p_attributes,
                'estoque': p_estoque,
                'preco': p_preco,
                'parcelas': p_parcelas,
                'valor_parcela': p_qtd_parcelas,
                'taxa_juros': '',
                'url': p_url,
                'imagem': p_imagem
            })


        yield maga_item
        

    def parse(self, response):
        links = response.css('a[name=linkToProduct]::attr(href)')
        for p_link in links:
            link = p_link.extract()
            print(link)
            yield scrapy.Request(link, callback=self.parse_interna)

        page = self.page + 1
        next_page = self.url_maga + '?page=' + str(page)

        if len(links) > 0:
            yield response.follow(next_page, self.parse)

process = CrawlerProcess(get_project_settings())

process.crawl(MagaSpider)
process.start()