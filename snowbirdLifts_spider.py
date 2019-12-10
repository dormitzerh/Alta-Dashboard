import scrapy


class SnowbirdSpider(scrapy.Spider):
    name = "SnowbirdLifts"
    start_urls = ['http://www.snowbird.com/mountain-report/']

    def parse(self, response):
    	Snowbird_Lifts_Closed = response.xpath('//*[@id="lifts-anchor"]/div/div')

        for Lifts in Snowbird_Lifts_Closed:
            Status = Lifts.xpath('.//div[1]/text()').extract()
            Name = Lifts.css('div.title::text').extract()
        
            yield {
            'Status' : Status,
            'Name' : Name
            }
