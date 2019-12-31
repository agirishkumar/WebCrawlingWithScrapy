import scrapy
from scrapy.http import FormRequest
from ..items import QuotetutItem
from scrapy.utils.response import open_in_browser
class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):

        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={

            'csrf_token': token,
            'username': 'girish@gmail.com',
            'password': 'hello123'
        },callback = self.start_scraping)

    def start_scraping(self,response):
        open_in_browser(response)
        items = QuotetutItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items