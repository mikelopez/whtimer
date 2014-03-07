#dev@scidentify.info - Marcos Lopez
import unittest
import sys
import os
sys.path.append('../')
from termprint import *
from db import Database

class BaseTest(unittest.TestCase):

    def create_tables(self):
        """Create Tables"""
        termprint("INFO", "Creating tables...")
        # remove test.db file from rel directoruy
        if os.path.exists("test.db"):
            os.system('rm test.db')

        # make the tables
        db = Database(connect=True)
        db.maketables()

        # now check they exist
        try:
            db.maketables()
        except Exception, e:
            if "already exists" in str(e):
                pass
            else:
                raise Exception(e)
        termprint("INFO", "DONE")
        db.close()


    def add_task(self, id, name, user):
        """Adds a task to test timer functionality"""
        db = Database(connect=True)
        q = db.query("INSERT INTO Task VALUES(%s, '%s', '%s');" % (id, name, user))
        db.close() 
        return q

    def select(self, query):
    	db = Database(connect=True)
    	q = db.select(query)
    	db.close()
    	return q
