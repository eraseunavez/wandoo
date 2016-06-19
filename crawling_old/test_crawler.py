import scrapy
import psycopg2

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'

    conn = psycopg2.connect("dbname=collectMeta user=postgres host=localhost")
    cur = conn.cursor()

    cur.execute("SELECT url FROM crawlingtarget WHERE no = 1 AND valid = \'Y\'")

    start_urls = cur.fetchone()
    cur.close()
    conn.close()

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract_first(),
            'votes': response.css('.question .vote-count-post::text').extract_first(),
            'body': response.css('.question .post-text').extract_first(),
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }
