from scrapy.spider import BaseSpider,Rule
from scrapy.selector import HtmlXPathSelector
from items import NewsItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class MySpider(BaseSpider):
        name = "gonews"
        allowed_domains = ["www.thehindu.com",
                           "www.thehindubusinessline.com",
                           "english.manoramaonline.com/"

                          ]
        start_urls = [

                      "http://www.thehindu.com/business/Economy/",
            "http://english.manoramaonline.com/news.html",
            "http://english.manoramaonline.com/sports.html",
            "http://english.manoramaonline.com/business.html",
             " http://www.thehindu.com /business/Industry/",
                "http://english.manoramaonline.com/wellness.html",
                 "http://english.manoramaonline.com/lifestyle.html",
                  "http://english.manoramaonline.com/entertainment.html",
                  "http://travel.manoramaonline.com/travel.html",
                  "http://food.manoramaonline.com/food.html",
              "http://english.manoramaonline.com/multimedia.html",
                "http://english.manoramaonline.com/women.html",
                      "http://www.thehindu.com/business/markets/",
                      "http://www.thehindu.com/business/budget/",
                          "http://www.thehindu.com/sport/cricket/",
                       "http://www.thehindu.com/sport/football/"
                       "http://www.thehindu.com/elections/",
                      "http://www.thehindubusinessline.com/economy/"

                    ]
        rules = (
            # Extract links for next pages
            Rule(SgmlLinkExtractor(allow=(),
                                   restrict_xpaths=('//div[contains(@class, "leftright")][1]//a[contains(., "Next")]')),
                 callback='parse', follow=True),
        )
        def parse(self, response):
            titles = response.selector.xpath("//p")
            items = []
            for titles in titles:
                item = NewsItem()
                item["title"] = titles.xpath("a/text()").extract()
                item["link"] = titles.xpath("a/@href").extract()
                items.append(item)
            return items
