BOT_NAME = 'MidasSpider'

SPIDER_MODULES = ['MidasSpider.spiders']
NEWSPIDER_MODULE = 'MidasSpider.spiders'


MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "stackoverflow"
MONGODB_COLLECTION = "questions"

#ITEM_PIPELINES = {'MidasSpider.pipelines.MongoDBPipeline': 1}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MidasSpider (+http://www.yourdomain.com)'
