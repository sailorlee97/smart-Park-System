# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class ContextspiderPipeline:


    def open_spider(self,spider):
        self.conn = pymysql.connect(host='rm-bp1mv8ua26rj84t32eo.mysql.rds.aliyuncs.com',
                                    database='spider',port=3306,user='runtrend',password='4rfv*UHB')
        self.cursor = self.conn.cursor()
        self.cursor.execute('truncate table context;')

    def process_item(self, item, spider):
        title = item.get('title','')
        url = item.get('url','')
        self.cursor.execute(
            'insert into context (title,url) values (%s,%s)',(title,url)
        )
        # print(item)
        return item

    def close_spider(self,spider):
        self.conn.commit()
        self.conn.close()
