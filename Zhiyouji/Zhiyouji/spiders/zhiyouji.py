# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Zhiyouji.items import ZhiyoujiItem

# ----符号表示将爬虫改为分布式爬虫的步骤
# ----1.导包
from scrapy_redis.spiders import RedisCrawlSpider

class ZhiyoujiSpider(RedisCrawlSpider):
# class ZhiyoujiSpider(CrawlSpider):　＃２．－－－－
    name = 'zhiyouji'
    allowed_domains = ['jobui.com']
    #start_urls = ['http://www.jobui.com/cmp']　＃　３．－－－－
    redis_key = "zhiyou:start_urls"#5.----
    # 6.----修改settings配置

    rules = (
        # 下一页
        Rule(LinkExtractor(allow=r'cmp\?n=\d+\#listInter'), follow=True),
        # 详情页
        Rule(LinkExtractor(allow=r'/company/\d+/$'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = ZhiyoujiItem()
        # 公司名称
        item['name'] = response.xpath('//*[@id="companyH1"]/a/text()').extract_first()
        # 浏览量
        item['browse'] = response.xpath('//div[@class="grade cfix sbox"]/div/text()').extract_first().split('人')[0].strip()
        # 公司信息
        try:
            item['message'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[1]/text()').extract_first()
        except:
            item['message'] = response.xpath('//*[@id="cmp-intro"]/div/div/dl/dd[1]/text()').extract_first()
        # 公司行业
        item['industry'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[2]/a/text()').extract_first()
        # 公司简称
        item['abb'] = response.xpath('//dl[@class="j-edit hasVist dlli mb10"]/dd[3]/text()').extract_first()
        # 公司概述
        item['summ'] = ''.join(response.xpath('//*[@id="textShowMore"]/text()').extract_first())
        # 好评度
        item['dop'] = response.xpath('//div[@class="swf-contA"]/div/h3/text()').extract_first()
        # 薪资
        item['pay'] = response.xpath('//div[@class="swf-contB"]/div/h3/text()').extract_first()
        # 产品列表
        data_list = []
        nond_list = response.xpath('//div[@class="jk-matter jk-box"]/div[contains(@class,"products-logo")]')
        #print(nond_list,'------------------------------')
        for nond in nond_list:
            temp = {}
            temp['name'] = nond.xpath('./div/div/a/text()').extract_first()
            temp['info'] = nond.xpath('./div/p/text()').extract_first()
            data_list.append(temp)
        item['product'] = data_list

        # 融资情况
        data_list = []
        nond_list = response.xpath('//div[@class="jk-matter jk-box fs16"]/ul/li')
        for nond in nond_list:
            temp = {}
            temp['time'] = nond.xpath('./span[1]/text()').extract_first()
            temp['state'] = nond.xpath('./h3/text()').extract_first()
            temp['money'] = nond.xpath('./span[2]/text()').extract_first()
            temp['investor'] = nond.xpath('./span[3]/text()').extract_first()
            data_list.append(temp)
        item['financing'] = data_list
        # 排名
        data_list = []
        nond_list = response.xpath('//div[@class="fs18 honor-box"]/div')
        for nond in nond_list:
            temp = {}
            key = nond.xpath('./a/text()').extract_first()
            temp[key] = nond.xpath('./span[2]/text()').extract_first()
            data_list.append(temp)
        item['ranking'] = data_list
        # 地址
        item['add'] = response.xpath('//div[@class="s-wrapper"]/dl/dd[1]/text()').extract_first()
        # 网址
        item['web'] = response.xpath('//div[@class="s-wrapper"]/dl/dd[2]/a/text()').extract_first()
        # 联系方式
        item['tel'] = response.xpath('//div[@class="j-shower1 dn"]/dd/text()').extract_first()
        # QQ
        item['qq'] = response.xpath('//div[@class="j-shower1 dn"]/dd/span/text()').extract_first()
        #print(item['qq'],response.url)

        # for k,v in item.items():
        #     print(k,v)
        #     print("--------------------")
        yield item
