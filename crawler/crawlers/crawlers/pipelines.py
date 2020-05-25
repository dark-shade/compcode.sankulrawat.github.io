# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from sqlite3 import Error
import logging

class SqlitePipeline:
    def __init__(self, sqlite_file):
        try:
            logging.info("inside sqlite pipeline init")
            self.connection = sqlite3.connect(sqlite_file)
            self.cursor = self.connection.cursor()
            if self.connection:
                logging.info("db connection open")
            else:
                logging.info("unable to open connection to db")
        except Error as e:
            logging.error(e)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file=crawler.settings.get('SQLITE_FILE')
        )

    def open_spider(self, spider):
        logging.info("creating leetcodedata table if not exists")
        self.cursor.execute('CREATE TABLE IF NOT EXISTS leetcodedata ' \
                    '(id INTEGER PRIMARY KEY, solved INTEGER, total INTEGER, date TEXT)')

    def close_spider(self, spider):
        logging.info("closing commit and connection")
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):
        logging.info("inserting data into leetcodedata table")
        self.cursor.execute('INSERT INTO leetcodedata (solved, total, date) VALUES (?, ?, ?)', (item["solved"], item["total"], item["date"]))
        return item
