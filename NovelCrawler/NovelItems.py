# _*_ coding:utf-8 _*_
from scrapy import *
class NovelItems(Item):
    title = Field()  # 保存小说名称
    text = Field()  # 小说内容