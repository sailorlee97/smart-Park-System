"""
@Time    : 2022/10/8 16:32
-------------------------------------------------
@Author  : sailorlee(lizeyi)
@email   : sailorlee31@gmail.com
-------------------------------------------------
@FileName: techspider.py
@Software: PyCharm
"""
from scrapy import Selector
import requests

def obtain():
    url = "http://kw.nanjing.gov.cn/"
    # headers = {
    #    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    # }

    rsp = requests.get(url)

    if rsp.status_code != 200:
        raise Exception("anti reptile!")

    # rsp = rsp.text.encode('iso-8859-1').decode('utf-8')
    # demo1 > li:nth-child(1) > a
    sel = Selector(text=rsp.text)
    urls = sel.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[1]//a/@href').extract()
    titles = sel.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[1]//a//text()').extract()

    encode_titles = []
    for i in titles:
        encode_titles.append(i.encode('iso-8859-1').decode('utf-8'))
        # print(i)
    # for index, c_node  in enumerate(c_nodes):
    new_url = _get_whole_url(urls, url)
    payload = []
    for i in range(len(new_url)):
        content = {'title': encode_titles[i], 'url': new_url[i]}
        payload.append(content)

    return payload

def obtainIndustryInformation():
    url = "http://jxw.nanjing.gov.cn/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    rsp = requests.get(url,headers = headers)

    if rsp.status_code != 200:
        raise Exception("anti reptile!")
    sel = Selector(text=rsp.text)
    urls = sel.xpath('/html/body/div[5]/div[1]/div[2]/div[4]/ul//a/@href').extract()
    titles = sel.xpath('/html/body/div[5]/div[1]/div[2]/div[4]/ul//a//@title').extract()
    encode_titles = []
    for i in titles:
        encode_titles.append(i.encode('iso-8859-1').decode('utf-8'))
        # print(i)
    # for index, c_node  in enumerate(c_nodes):
    new_url = _get_whole_url(urls, url)
    payload = []
    for i in range(len(new_url)):
        content = {'title': encode_titles[i], 'url': new_url[i]}
        payload.append(content)

    return payload

def obtainProvincetech():
  url = "http://kxjst.jiangsu.gov.cn/"
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
   }

  rsp = requests.get(url,headers = headers)

  if rsp.status_code != 200:
    raise Exception("anti reptile!")

  # rsp = rsp.text.encode('iso-8859-1').decode('utf-8')
  # demo1 > li:nth-child(1) > a
  sel = Selector(text=rsp.text)
  urls = sel.xpath('//*[@id="nav_1"]/div[4]/div[2]/div[1]/div[2]/ul//a/@href').extract()
  titles = sel.xpath('//*[@id="nav_1"]/div[4]/div[2]/div[1]/div[2]/ul//a//text()').extract()

  encode_titles = []
  for i in titles:
    encode_titles.append(i.encode('iso-8859-1').decode('utf-8'))
    # print(i)
  # for index, c_node  in enumerate(c_nodes):
  new_url = _get_whole_url(urls, url)
  payload = []
  for i in range(len(new_url)):
    content = {'title': encode_titles[i], 'url': new_url[i]}
    payload.append(content)
  print(payload)

  return payload

def _get_whole_url(list,start_urls):
    new_list = []
    for item in list:
      new_list.append(start_urls+item[2:])
    return new_list