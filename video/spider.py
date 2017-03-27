import scrapy
from scrapy.crawler import CrawlerProcess


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class VideoSpider(scrapy.Spider):
    name = "videos"
    start_urls = [
        'http://travel.youku.com/?spm=a2hww.20023042.topNav.5~5~1~3~A'
    ]

    def parse(self, response):
        for base_info in response.xpath('//div[@class="v-link"]/a'):
            yield {
                'url': base_info.xpath('@href').extract_first(),
                'name': base_info.xpath('@title').extract_first()
            }


def get_videos():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    })

    process.crawl(VideoSpider)
    process.start()
