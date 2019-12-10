import scrapy


class SnowbirdSpider(scrapy.Spider):
    name = "AltaLifts"
    start_urls = ['https://www.alta.com/conditions/daily-mountain-report/snow-report#road-status']

    def parse(self, response):
        Alta_Lifts = response.xpath('//*[@id="snow-report"]/table[5]/tbody/tr')

        for Lifts in Alta_Lifts:
            Status = Lifts.xpath ('normalize-space(.//td/p/text())').extract()
            Name = Lifts.xpath('normalize-space(.//td/text())').extract()
        
            yield {
            'Status' : Status,
            'Name' : Name
            }
