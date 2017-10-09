import scrapy

class RaphaelEstate(scrapy.Spider):
    name = 'raphaelestate'
    start_urls = ['http://www.raphaelimoveis.com.br/pesquisa.php?busca=V']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

