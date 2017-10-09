import scrapy


class raphaelspider(scrapy.Spider):
    name = "raphael"

    def start_requests(self):
        urls = [
            'http://www.raphaelimoveis.com.br/pesquisa.php?busca=V'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for estate in response.xpath('//div[@class="info"]'):
            aux = estate.extract()
            aux = aux.replace("\n", "").replace("\t", "").replace("</p>", "").replace("<div>", "").replace("</div>", "").replace("<span>", "").replace("</span>", "")
            aux = aux.split("<p>")
            yield { 
                'id': int(aux[1].split(": ")[1]),
                'tipo': aux[2].split(": ")[1],
                'bairro': aux[3].split(": ")[1],
                # 'dormitorios': int(aux[4].split(": ")[1]),
                'valor':  aux[5].split(",")[0].split(" ")[3].replace(".", "")
            }
