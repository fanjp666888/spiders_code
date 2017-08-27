# -*- coding: utf-8 -*-
import scrapy
from Yiche.items import YicheItem
import json

class YicheSpider(scrapy.Spider):
    name = 'yiche'
    allowed_domains = ['car.bitauto.com']
    start_urls = ['http://api.car.bitauto.com/CarInfo/getlefttreejson.ashx?tagtype=chexing&pagetype=masterbrand&objid=127']
    print("******************")
    def parse(self, response):

        aa = response.text.split('name:')
        temp = []

        i = 1
        while i < len(aa):
            pp = []
            pp.append(aa[i])
            #print(pp[0])
            temp.append(pp)
            i += 1
        res_1 = []

        for i in temp:
            res_2 = []
            res_2.append(i[0])
            res_1.append(res_2)

        result = []

        for i in res_1:
            result_1 = []
            result_1.append(i[0])
            result.append(result_1[0])
        #print(result)
        for i in result:
            item = YicheItem()
            # 车型
            item['series'] = i.split(',')[0]
            # 获取ｕｒｌ并拼接
            url = 'http://www.car.bitauto.com'+i.split(',')[1].split('"')[1]
            #print(url)
            yield scrapy.Request(url,callback=self.parse_next,meta={'item_1':item})
            # break用于一次测试，防止在编写代码时被反爬
            break

    def parse_next(self,response):
        print('＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝')
        item = response.meta['item_1']
        print("======================")

        # 分组　
        data_list = response.xpath('//div[@class="row block-4col-180"]/div[@class="col-xs-3"]').extract()
        for data in data_list:
            url = 'http://car.bitauto.com'+data.xpath('./div/div/a/@href').extract_first()
            yield scrapy.Request(url,callback=self.parse_min,meta={'item_2':item})

    def parse_min(self,response):
        item = response.meta['item_2']
        # 车型
        item['car'] = response.xpath('//div[@class="container"]/div[1]/h1/a[2]/text()').extract_first()
        # 参考价
        item['reference'] = response.xpath('//div[@class="lowest-price"]/h2/a[1]/text()').extract_first()
        data_list = response.xpath('//tr[contains(@id,"car_filter_id")]').extract()
        # 车辆各配置信息集合
        info = []
        for data in data_list:
            info_1 = []
            # 排量
            displacement = data.xpath('./td[1]/a/text()').extract_first()
            info_1.append(displacement)
            # 关注度
            attention = data.xpath('./td[2]/div/div/@style').extract_first().split(':')[1]
            info_1.append(attention)
            # 变速箱
            gearbox = data.xpath('./td[3]/text()').extract_first()
            info_1.append(gearbox)
            # 指导价
            guidance = data.xpath('./td[4]/span/text()').extract_first()
            info_1.append(guidance)
            # 最低价
            minimum = data.xpath('./td[5]/span/a/text()').extract_first()
            info_1.append(minimum)
            info.append(info_1)
        item['info'] = info

        # 口碑评分
        item['graded'] = response.xpath('//div[@id="circleProgress-report"]/div/p/text()').extract_first()

        yield item

