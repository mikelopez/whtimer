#dev@scidentify.info - Marcos Lopez
import unittest
import sys
import os
sys.path.append('../')
from termprint import *
from datetime import datetime, timedelta
from random import randint
from db import Database

class BaseTest(unittest.TestCase):

    def logi(self, data):
        termprint("INFO", data)
    def logw(self, data):
        termprint("WARNING", data)
    def loge(self, data):
        termprint("ERROR", data)

    def create_tables(self, dbfile=None):
        """Create Tables"""
        termprint("INFO", "Creating tables...")
        # remove test.db file from rel directoruy
        if os.path.exists("test.db"):
            os.system('rm test.db')

        # make the tables
        db = Database(connect=True)
        if dbfile:
            db.dbfile = dbfile
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
        """Adds a task to Task table. Requires ID, NAME, USER params"""
        db = Database(connect=True)
        #print "INSERT INTO Task VALUES(%s, '%s', '%s');" % (id, name, user)
        q = db.query("INSERT INTO Task VALUES(%s, '%s', '%s');" % (id, name, user))
        db.close() 
        return q

    def add_task_event(self, id, task_id, user, is_started, start, stop, minutes_sum):
        """Adds a task to Task table. Requires ID, NAME, USER params"""
        db = Database(connect=True)
        values = "('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (id, task_id, user, 
                                                                 is_started, start, 
                                                                 stop, minutes_sum)
        q = db.query("INSERT INTO TaskEvent VALUES%s;" % (values))
        db.close() 
        return q

    def select(self, query):
    	db = Database(connect=True)
    	q = db.select(query)
    	db.close()
    	return q
