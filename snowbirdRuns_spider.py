import scrapy


class SnowbirdSpider(scrapy.Spider):
    name = "SnowbirdRuns"
    start_urls = ['https://www.snowbird.com/lifts-trails/']

    def parse(self, response):
    	Snowbird_Runs_Closed = response.css('div.trailFilter')

        for Runs in Snowbird_Runs_Closed:
            Status = Runs.xpath('//*[@id="lifts-anchor"]/div/div/div[1]/text()').extract()
            Name = Runs.css('div.title::text')[0].extract()
        
            yield {
            'Status' : Status,
            'Name' : Name
            }
