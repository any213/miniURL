from const.const import const_value as c
import logging
import os

db = None
cache = None
cacheonoff = False

class miniURL_db:
    global db, cache
    def set_url(self, org_url, sht_url):
        return db.set_url(org_url,sht_url)

    def get_org_url(self, sht_url):
        return db.get_org_url(sht_url)

    def get_sht_url(self,org_url):
        return db.get_sht_url(org_url)

    def set_cache(self, org_url, sht_url):
        if cacheonoff is False :
            return ""
        return cache.set_cache(org_url, sht_url)

    def get_cache(self,sht_url):
        if cacheonoff is False :
            return ""
        return cache.get_cache(sht_url)

def init_db(db_module,db_class,dbconf):
    global db
    logging.debug(os.getcwd())
    mod = __import__(db_module, fromlist=[db_module])
    db = getattr(mod, db_class)(dbconf)
    return

def set_cache_onoff(onoff,cachedb):
    global cacheonoff, cache
    cacheonoff = onoff
    cache = cachedb("pass")
    return


if __name__ == '__main__':
    init_db("models.db_redis","db_redis")
    d = miniURL_db()
    d.set_org_url()
