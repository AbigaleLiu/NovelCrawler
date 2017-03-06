# _*_ coding:utf-8 _*_
from scrapy import *
from NovelCrawler.NovelItems import *


class Novel(Spider):
    name = "Novel"  # 爬虫名
    allowde_domains = ["jjwxc.net"]  # 域名
    start_urls = ["http://www.jjwxc.net/onebook.php?novelid=379995&chapterid=1"]  # 爬取地址

    def parse(self, response):
        # print(response.encoding)  # 获取网页编码格式
        # body = response.body.decode("gb18030", "ignore").encode("utf-8")  # 忽略非法字符将网页转为Unicode，再转为utf-8
        # print(body)
        item = NovelItems()  # 实例一个容器保存爬取到的信息
        title = response.xpath("/html/head/title/text()").extract()
        item["title"] = title
        text_list = response.xpath("/html/body/table[@id='oneboolt']/tr[2]/td[1]/div[@class='noveltext']/text()").extract()
        item["text"] = text_list
        yield item
        # url跟踪
        url = response.xpath("/html/body/table[@id='oneboolt']/tr[5]/td[@class='noveltitle']/span/a/@href").extract()
        if url:
            page = "http://www.jjwxc.net/" + url[0]  # 组成下一页的ＵＲＬ
            yield Request(page, callback=self.parse)