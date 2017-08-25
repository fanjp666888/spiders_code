# -*- coding: utf-8 -*-
import scrapy
from Zhilian.items import ZhilianItem
import json

# 抓取智联招聘天津的python招聘信息
class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%A4%A9%E6%B4%A5&kw=python']

    def parse(self, response):
        # 获取招聘信息列表节点
        url_list = response.xpath('//*[@id="newlist_list_content_table"]/table')
        for temp in url_list:
            # 创建item对象
            item = ZhilianItem()
            # 发布时间
            item['time'] = temp.xpath('//*[@id="newlist_list_content_table"]/table[3]/tr[1]/td[6]/span/text()').extract_first()
            # xpath里不能有table
            url = temp.xpath('//div[@class="newlist_list_content"]/table[2]/tr[1]/td[1]/div/a/@href').extract_first()
            # 转到详情页
            yield scrapy.Request(url,callback=self.parse_url,meta={"item_1":item})
        # 下一页
        next_url = response.xpath('//div[@class="pagesDown"]/ul/li[9]/a/@href').extract_first()
        if next_url is None:
            return 0
        #print(next_url,"************************")
        # 翻页
        yield scrapy.Request(next_url,callback=self.parse)

    def parse_url(self,response):
        # 获取传递过来的item对象
        item = response.meta['item_1']
        # 招聘名称
        item['name'] = response.xpath('//div[@class="fixed-inner-box"]/div[1]/h1/text()').extract_first()
        # 招聘单位
        item['company'] = response.xpath('//div[@class="fixed-inner-box"]/div[1]/h2/a/text()').extract_first()

        # 薪资
        item['pay'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()').extract_first()
        # 工作地点
        item['rddress'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[2]/strong/a/text()').extract_first()
        # 工作经验
        item['experience'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[5]/strong/text()').extract_first()
        # 学历要求
        item['degree'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[6]/strong/text()').extract_first()
        # 招聘人数
        item['number'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[7]/strong/text()').extract_first()
        # 职位类别
        item['sort'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[8]/strong/a/text()').extract_first()
        # 职位描述
        item['describe'] = response.xpath('//div[@class="tab-inner-cont"]/p/text()').extract()
        # 公司介绍
        #item['introduce'] = ''.join(response.xpath('//div[@class="tab-inner-cont"]/p[1]/text()').extract_first())
        # 工作地点
        item['work_rdd'] = ''.join(response.xpath('//div[@class="tab-inner-cont"]/h2/text()').extract_first()).strip()

        #print(item['work_rdd'])
        yield item

