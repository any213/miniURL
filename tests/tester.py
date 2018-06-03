import unittest
from models import db
from models.db_redis import redis_class
from util.short_maker import make_short


class TestminiURL(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_db(self):
        dbconf ={
                    "host": "localhost",
                    "port": 6379,
                    "pool_size":10,
                    "db":0
                  }
        db.init_db(redis_class.__module__, redis_class.__name__,dbconf)
        self.assertNotEqual(db.db,None)



    def test_short_maker(self):
        sht_url=make_short("www.kakaopay.com")
        self.assertNotEqual(sht_url,None)


    def test_redis(self):
        dbconf ={
                    "host": "localhost",
                    "port": 6379,
                    "pool_size":10,
                    "db":0
                  }
        rds = redis_class(dbconf)
        rds.set_url("www.testurl.com","happy")
        result = rds.get_org_url("happy")
        self.assertEqual(result,"www.testurl.com")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestminiURL)
    unittest.TextTestRunner(verbosity=2).run(suite)

