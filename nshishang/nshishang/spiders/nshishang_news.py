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
        # 遍历资讯列表 获取每条资讯标题和链接 如果解析到列表则遍历解析
        if articles:
            for article in articles:
                # 解析资讯标题
                title = article.css('a.r-p-a::text').get()
                # 解析资讯链接
                url = article.css('a.r-p-a::attr(href)').get()
                self.log(f"[{self.name}]解析到资讯数据:{title}-{url}")
            
            # 下一页地址提取
            _next_url = response.css("a.a1:last-child::attr(href)").get()
            # 完整的下一页地址拼接
            next_url = response.urljoin(_next_url)
            self.log(f"[{self.name}]解析到下一页地址:{url}")
            yield scrapy.Request(url=next_url, callback=self.parse)
        # 未解析到列表，在所有任务请求完之后 爬虫将关闭
        else:
            self.log(f"[{self.name}]所有数据采集完成，爬虫关闭")
