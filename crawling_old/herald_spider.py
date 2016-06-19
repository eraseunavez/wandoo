import scrapy

class heraldSpider(scrapy.Spider):
    name = "herald"
    allowed_domains = ["biz.heraldcorp.com"]
    start_urls = [
        "http://biz.heraldcorp.com/wealth/",
    ]

    def parse(self, response):
        for href in response.css(".lnewslist > dt > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//div[@id="articleText"]'):
            print sel.xpath('text()').extract()
            #item = DmozItem()
            #item['title'] = sel.xpath('a/text()').extract()
            #item['link'] = sel.xpath('a/@href').extract()
            #item['desc'] = sel.xpath('text()').extract()
            #yield item

