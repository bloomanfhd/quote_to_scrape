# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3

class QuotesPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect("quote.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quote_table""")
        self.curr.execute("""create table quote_table(Quote text, Author text, Tags text) """)

    def process_item(self, item, spider):
        self.store_database(item)
        return item
    
    def store_database(self, item):
        self.curr.execute(""" insert into quote_table values(?,?,?)""",
                                (item['quote'],
                                item['author'],
                                item['tag'][0]))
        self.conn.commit()

    


