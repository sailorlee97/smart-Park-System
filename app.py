# -*- coding: utf-8 -*-
"""
@Time    : 2022/8/25 17:26
@Author  : zeyi li
@Site    : 
@File    : app.py
@Software: PyCharm
"""
from flask import Flask, make_response, jsonify
import json
import requests
import os
import pymysql
from pandas import DataFrame
import subprocess
from scrapy import Selector

app = Flask(__name__)

conn = pymysql.connect(
    host='rm-bp1mv8ua26rj84t32eo.mysql.rds.aliyuncs.com',
    user='runtrend',
    password='4rfv*UHB',
    db='spider',
    port=3306
)


@app.route('/json')
def json_request():
  r = requests.get('http://10.22.244.19:8999/accessRecord/temp/currentRecord')

  data = r.content.decode()
  dict_json = json.loads(data)
  enter_exit_data = dict_json['data']

  enter_exit_data = DataFrame(enter_exit_data)

  total_persons = len(enter_exit_data)
  teacher_person = len(enter_exit_data[enter_exit_data['personType'] == '教工'])
  other_person = len(enter_exit_data[enter_exit_data['personType'] == '其他'])
  student_person = len(enter_exit_data[enter_exit_data['personType'] == '学生'])
  teac_percent = '{:.0%}'.format(teacher_person / total_persons)
  oth_percent = '{:.0%}'.format(other_person / total_persons)
  stu_percent = '{:.0%}'.format(student_person / total_persons)

  payload = {'Teacher': teac_percent,'Staff':oth_percent,'Student':stu_percent}

  return jsonify(payload)

@app.route('/asin',methods = ["GET"])
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
    print(payload)

    return jsonify(payload)

def obtainIndustryInformation():
    url = "http://jxw.nanjing.gov.cn/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    rsp = requests.get(url,headers = headers)

    if rsp.status_code != 200:
        raise Exception("anti reptile!")
    sel = Selector(text=rsp.text)
    urls = sel.xpath('/html/body/div[5]/div[1]/div[2]/div[4]/ul//a/@href').extract()
    titles = sel.xpath('/html/body/div[5]/div[1]/div[2]/div[4]/ul//a//text()').extract()
    encode_titles = []
    for i in titles:
        encode_titles.append(i.encode('iso-8859-1').decode('utf-8'))
        # print(i)
    # for index, c_node  in enumerate(c_nodes):
    new_url = _get_whole_url(urls, url)
    payload = []
    for i in range(len(new_url)):
        content = {'title': encode_titles[i].rstrip().lstrip(), 'url': new_url[i]}
        payload.append(content)
    print(payload)

    return jsonify(payload)

def obtainProvincetech():
  url = "http://kxjst.jiangsu.gov.cn/"
  headers = {
    #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #"Accept-Encoding": "gzip, deflate",
    #"Accept-Language": "zh-CN,zh;q=0.9",
    #"Cookie": "JSESSIONID=97F070A8C64A24BB0EC1C97D2E8A9D11; __jsluid_h=0a8c17b9085327cccceb729c45946a1f",
    #"Host": "www.jiangsu.gov.cn",
    #"Proxy-Connection": "keep-alive",
    #"Referer": "http://kxjst.jiangsu.gov.cn/",
    #"Upgrade-Insecure-Requests": "1",
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

  return jsonify(payload)

def _get_whole_url(list,start_urls):
    new_list = []
    for item in list:
      new_list.append(start_urls+item[2:])
    return new_list

@app.route('/')
def hello_world():  # put application's code here
  return 'Hello World!'


if __name__ == '__main__':
  app.run(debug=True)