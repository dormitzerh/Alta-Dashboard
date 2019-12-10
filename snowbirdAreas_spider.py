import scrapy


class SnowbirdSpider(scrapy.Spider):
    name = "SnowbirdAreas"
    start_urls = ['http://www.snowbird.com/mountain-report/']

    def parse(self, response):
    	Snowbird_Areas_Closed = response.css('div.Closed.closed.gate')
        Snowbird_Areas_Open = response.css('div.Open.open.gate')

        for Areas in Snowbird_Areas_Closed:
            Status = Areas.css('div.status::text').extract()
            Name = Areas.css('div.title::text').extract()
        
            yield {
            'Status' : Status,
            'Name' : Name
            }

    	for Areas in Snowbird_Areas_Open:
            Status = Areas.css('div.status::text').extract()
            Name = Areas.css('div.title::text').extract()
    	
            yield {
            'Status' : Status,
            'Name' : Name
            }
