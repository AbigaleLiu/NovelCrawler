# _*_ coding:utf-8 _*_
class NovelPipelines(object):
    def __init__(self):
        self.file = open(r"F:\NovelCrawler\SCI谜案集.txt", "a", encoding="utf-8")

    def process_item(self, item, spider):
        title = item["title"]
        text = item["text"]
        self.file.write(title[0]+"\n\n")
        for line in text:
            if "\r\n" not in line:
                self.file.write(line+"\n")
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()