# -*- coding: utf-8 -*-
import scrapy


class PokedexSpider(scrapy.Spider):
    name = 'pokedex'
    allowed_domains = ["pokemon.com"]
    start_urls = ['https://www.pokemon.com/us/pokedex/bulbasaur']

    def parse(self, response):
        
        yield {

            'name': response.css("div.pokedex-pokemon-pagination-title > div::text").extract_first().strip(),
            'types': response.css("div.dtm-type a::text").extract()
        }

        next_page_url = response.css("a.next::attr('href')").extract_first()
        yield scrapy.Request(response.urljoin(next_page_url))

