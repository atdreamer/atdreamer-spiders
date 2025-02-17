# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from nshishang import settings
from dbutils.pooled_db import PooledDB


class NshishangPipeline:
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,  # 使用 pymysql 作为数据库连接驱动
            maxconnections=5,  # 允许的最大连接数
            mincached=2,       # 初始化时创建的空闲连接数量
            maxcached=3,       # 连接池中最多缓存的空闲连接数量
            blocking=True,     # 达到最大连接数后是否阻塞，True 阻塞等待连接
            maxusage=None,     # 单个连接的最大重复使用次数
            setsession=[],     # 开始会话前执行的命令
            ping=1,            # ping 服务器检查连接是否可用，1 表示在每次使用连接时检查
            host=settings.MYSQL_HOST,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWORD,
            database=settings.MYSQL_DB,
            charset=settings.CHARSET,
            cursorclass=pymysql.cursors.DictCursor
        )

    def process_item(self, item, spider):
        # 插入数据到 MySQL 表
        sql = """
            INSERT INTO items (title, url) 
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(sql, (item['title'], item['url'], item['description']))
        self.conn.commit()  # 提交事务
        return item

    def close_spider(self, spider):
        # 关闭数据库连接
        self.cursor.close()
        self.conn.close()