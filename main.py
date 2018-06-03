from models import db as model
from models import db_redis
from models import db_redis as cache_module
from models.db_redis import redis_class as redis_module

from controllers import route
import sys

from const import const as const_module
import json
import logging
import optparse

class miniURL_app:
    def __init__(self):
        CONFIG_PATH = "setup/config.json"
        self.const = const_module.const_value()

        config_file = open(CONFIG_PATH, 'r')
        self.app_config = json.loads(config_file.read())

    def init_db(self):
        dbtype=self.app_config[self.const.DBTYPE]

        #db 인스턴스 생성 by dbtype
        if dbtype == "redis":
            db_module = redis_module.__module__
            db_class = redis_module.__name__
            conf = self.app_config[self.const.REDIS]
        else :
            sys.exit('db init fail')

        logging.debug(db_module+db_class)
        model.init_db(db_module, db_class,self.app_config[dbtype])

        if self.app_config[self.const.CACHE][self.const.ONOFF] == "on":
            cache_module.init_cache(self.app_config[self.const.CACHE])
            model.set_cache_onoff(True,redis_module)


    def init_logging(self):
        LOGGING_LEVELS = {'critical': logging.CRITICAL,
                          'error': logging.ERROR,
                          'warning': logging.WARNING,
                          'info': logging.INFO,
                          'debug': logging.DEBUG
                          }
        parser = optparse.OptionParser()
        parser.add_option('-l', '--logging-level', help='Logging level')
        parser.add_option('-f', '--logging-file', help='Logging file name')
        (options, args) = parser.parse_args()
        logging_level = LOGGING_LEVELS.get(options.logging_level, logging.NOTSET)
        logging.basicConfig(level=logging_level, filename=self.app_config[self.const.LOG][self.const.PATH],
                            format='%(asctime)s %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')



if __name__ == '__main__':
    miniurl=miniURL_app()
    miniurl.init_logging()
    miniurl.init_db()
    route.flask_app.run(host='0.0.0.0', port=miniurl.app_config[miniurl.const.APP][miniurl.const.PORT])
