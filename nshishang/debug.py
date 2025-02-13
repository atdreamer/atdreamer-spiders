'''
Descripttion: 
version: 
Author: afcentry
Date: 2024-12-06 15:45:03
LastEditors: afcentry
LastEditTime: 2024-12-12 11:46:17
'''
'''
Descripttion: 
version: 
Author: afcentry
Date: 2024-12-06 15:45:03
LastEditors: afcentry
LastEditTime: 2024-12-12 11:41:23
'''
from scrapy.cmdline import execute
import sys
import os
# 获取当前脚本路径
dirpath = os.path.dirname(os.path.abspath(__file__))
#运行文件绝对路径
print(os.path.abspath(__file__))
#运行文件父路径
print(dirpath)
# 添加环境变量
sys.path.append(dirpath)
#切换工作目录
os.chdir(dirpath)
# 启动爬虫,第三个参数为爬虫name

execute(['scrapy','crawl','nshishang_news'])
