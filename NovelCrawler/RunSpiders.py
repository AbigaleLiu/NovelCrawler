# _*_ coding:utf-8 _*_
import os
class RunSpiders:
    def RunCommand(self, spider):
        os.system("scrapy crawl %s" % spider)

if __name__ == '__main__':
    _run = RunSpiders()
    _run.RunCommand('Novel')