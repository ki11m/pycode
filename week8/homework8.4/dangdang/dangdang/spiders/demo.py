import scrapy
from urllib.parse import urljoin
from scrapy.http import Request


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.49.01.00.00.00.html"]

    def parse(self, response):
        for i in range(1, 61):
            lab = "line" + str(i)
            lab1 = "li." + lab
            for eachbook in response.css(lab1):
                title = eachbook.xpath('./a/@title').extract_first()
                author = eachbook.xpath('./p[@class = "search_book_author"]/span/a/@title').extract_first()
                price = eachbook.xpath('./p[@class = "price"]/span[@class = "search_now_price"]/text()').extract_first()
                yield {
                    "title":title,
                    "author":author,
                    "price":price,
                }
        #pass

        next_url = response.css('div.paging li.next a::attr(href)').extract_first()
        print(next_url)
        if next_url:
            url = response.urljoin(next_url)
            yield Request(url, callback=self.parse())
