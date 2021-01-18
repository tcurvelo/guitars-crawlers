import json

import scrapy


class OlxSpider(scrapy.Spider):
    name = 'olx'
    allowed_domains = ['olx.com.br']
    start_urls = ['https://olx.com.br/instrumentos-musicais/guitarras']

    def parse(self, response):
        raw_data = response.css("#initial-data::attr(data-json)").get()
        data = json.loads(raw_data)
        for ad in data['listingProps']['adList']:
            yield {
                "title": ad.get("subject"),
                "image": ad.get("images", [{"original": None}])[0].get("original"),
                "price": ad.get("price"),
                "url": ad.get("url"),
            }
