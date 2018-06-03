from models import db
from const.const import const_value as c
import redis
import logging

rds = None
cache = None
org_pre = "org-"
sht_pre = "sht-"

class redis_class(db.miniURL_db):
    def __init__(self,dbconfig):
        global rds
        if dbconfig != "pass":
            pool = redis.ConnectionPool(host=dbconfig[c.HOST], port=dbconfig[c.PORT], db=dbconfig[c.DB])
            rds = redis.Redis(connection_pool=pool, max_connections=dbconfig[c.POOLSIZE], charset="utf-8",
                              decode_responses=True)
            logging.debug("redis init OK")
        return


    def set_url(self, org_url, sht_url):
        org_key = make_org_url_key(org_url)
        sht_key = make_sht_url_key(sht_url)
        rds.hset(org_key, org_url, sht_url)
        rds.hset(sht_key, sht_url, org_url)
        return

    def get_org_url(self, sht_url):
        sht_key = make_sht_url_key(sht_url)
        org_url=rds.hget(sht_key,sht_url)
        if org_url is not None:
            return str(org_url, encoding='utf-8')
        else:
            return None


    def get_sht_url(self, org_url):
        org_key = make_org_url_key(org_url)
        sht_url = rds.hget(org_key, org_url)
        if sht_url is not None:
            return str(sht_url, encoding='utf-8')
        else:
            return None

    def set_cache(self, org_url, sht_url):
        sht_key = make_sht_url_key(sht_url)
        rds.hset(sht_key, sht_url, org_url)
        return

    def get_cache(self,sht_url):
        org_url = rds.get(sht_url)
        if org_url is not None:
            return str(org_url, encoding='utf-8')
        else:
            return None

def make_org_url_key(org_url):
    kwdlist = org_url.split("/",4)
    if len(kwdlist)>3:
        rsplist=org_url.rsplit("/",len(kwdlist)-3)
        item=rsplist[0]
    else:
        item=org_url
    result = org_pre + item
    return result

def make_sht_url_key(sht_url):
    if len(sht_url) <5:
        result = sht_pre+sht_url
    else :
        result = sht_pre + sht_url[:4]
    return result


def init_cache(dbconfig):
    global cache
    pool = redis.ConnectionPool(host=dbconfig[c.HOST], port=dbconfig[c.PORT], db=dbconfig[c.DB])
    cache = redis.Redis(connection_pool=pool, max_connections=dbconfig[c.POOLSIZE], charset="utf-8",
                      decode_responses=True)
    logging.debug("cache init OK")


def get_instance(cacheconf):
    redis_class(cacheconf)
    return rds

if __name__ == "__main__":
    print(make_org_url_key("http://www.naver.com/"))
    print(make_sht_url_key("asfjiej"))