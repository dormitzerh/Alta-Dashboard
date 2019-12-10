import scrapy


class SnowbirdSpider(scrapy.Spider):
    name = "Road"
    start_urls = ['https://townofalta.com/road/']

    def parse(self, response):
        Alta_Areas = response.xpath('//*[@id="main"]/div/div[3]/div[1]/table/tbody/tr[2]')

        for Areas in Alta_Areas:
            Status = Areas.xpath ('normalize-space(.//td[2]/text())').extract()
        
            yield {
            'Status' : Status,
            }
