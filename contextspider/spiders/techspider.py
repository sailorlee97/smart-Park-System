# -*- coding: utf-8 -*-
"""
@Time    : 2022/8/22 15:27
@Author  : zeyi li
@Site    : 
@File    : techspider.py
@Software: PyCharm
"""
import scrapy

#from scrapy import selector
from ..items import ContextspiderItem

class techSpider(scrapy.Spider):
  name = 'tech'
  allowed_domains = ['kw.nanjing.gov.cn']
  start_urls = ['http://kw.nanjing.gov.cn/']

  def parse(self, response, **kwargs):
    #sel = scrapy.selector
    url = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[1]//a/@href').extract()
    title = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[1]//a//text()').extract()
    #new_url = self.start_urls[0]+url[0][2:]
    new_url = self._get_whole_url(url)

    file = dict(zip(title,new_url))
    #print("file:",file)
    item = ContextspiderItem()
    for key in file:

      item['title'] = key
      item['url'] = file[key]
      yield item
    #print("title:",title)
    pass



  def _get_whole_url(self,list):
    new_list = []
    for item in list:
      new_list.append(self.start_urls[0]+item[2:])
    return new_list