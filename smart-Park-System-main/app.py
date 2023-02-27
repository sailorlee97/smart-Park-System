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

from readcsv import getxlsxtojson, getxlsxtojson2
from techspider import obtain,obtainIndustryInformation

app = Flask(__name__)

# conn = pymysql.connect(
#     host='rm-bp1mv8ua26rj84t32eo.mysql.rds.aliyuncs.com',
#     user='runtrend',
#     password='4rfv*UHB',
#     db='spider',
#     port=3306
# )


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
  # teac_percent = '{:.0%}'.format(teacher_person / total_persons)
  # oth_percent = '{:.0%}'.format(other_person / total_persons)
  # stu_percent = '{:.0%}'.format(student_person / total_persons)
  # payload = {'Teacher':  20,'Staff':10,'Student':16}
  # payload = [{"value": 10, "name": 'Teacher'}, {"value": 20, "name": 'Staff'},
  #            {"value": 30, "name": 'Student'}]
  payload =[{ "value": teacher_person,"name": 'Teacher'},{ "value": other_person, "name": 'Staff'},{"value": student_person, "name": 'Student'}]
  # payload = {'Teacher': teac_percent,'Staff':oth_percent,'Student':stu_percent}
  # payload = {'Teacher': '50%','Staff':"0%",'Student':"50%"}

  return  jsonify(payload)


@app.route('/company1')
def company1():  # put application's code here
  return jsonify(getxlsxtojson())

@app.route('/company2')
def company2():  # put application's code here
  return jsonify(getxlsxtojson2())


@app.route('/')
def hello_world():  # put application's code here
  return 'Hello World!'

@app.route('/asin',methods = ["GET"])
def get_topeight():
    IndustryInformation = obtainIndustryInformation()
    a1 = IndustryInformation[0:8]
    # tech = obtain()
    # a2 = tech[0:4]
    content = a1
    print(content)
    return jsonify(content)

if __name__ == '__main__':
  app.run(debug=True)