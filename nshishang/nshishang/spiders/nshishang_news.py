import scrapy


class NshishangNewsSpider(scrapy.Spider):
    name = "nshishang_news"
    allowed_domains = ["nshishang.com"]
    start_urls = ["https://www.nshishang.com/life/consume/"]

    def parse(self, response):
        """数据解析

        Args:
            response (_type_): _description_
        """
        # 解析获取页面的所有资讯列表
        articles = response.css("div.clist-l-inner ul li")
        # 遍历资讯列表 获取每条资讯标题和链接
        for article in articles:
            # 解析资讯标题
            title = article.css('a.r-p-a::text').get()
            # 解析资讯链接
            url = article.css('a.r-p-a::attr(href)').get()
            self.log(f"[{self.name}]解析到资讯数据:{title}-{url}")
