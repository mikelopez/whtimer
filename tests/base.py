#dev@scidentify.info - Marcos Lopez
import unittest
import sys
import os
sys.path.append('../')
from termprint import *
from datetime import datetime, timedelta
from random import randint
from db import Database

MAX_ADD = 10

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

    def query(self, data):
        db = Database(connect=True)
        q = db.query(data)
        db.close()
        return q


    def add_task(self, id, name, user):
        """Adds a task to Task table. Requires ID, NAME, USER params"""
        db = Database(connect=True)
        #print "INSERT INTO Task VALUES(%s, '%s', '%s');" % (id, name, user)
        q = db.query("insert into Task values(%s, '%s', '%s');" % (id, name, user))
        db.close() 
        return q

    def add_task_event(self, id, task_id, user, is_started, start, stop, minutes_sum):
        """Adds a task to Task table. Requires ID, NAME, USER params"""
        db = Database(connect=True)
        values = "('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (id, task_id, user, 
                                                                 is_started, start, 
                                                                 stop, minutes_sum)
        q = db.query("insert into TaskEvent values%s;" % (values))
        db.close() 
        return q

    def select(self, query):
    	db = Database(connect=True)
    	q = db.select(query)
    	db.close()
    	return q

    def get_count(self, col, tbl):
        """Returns the count integer for a query"""
        query = self.select('select count(%s) from %s' % (col, tbl))
        try:
            return query[0][0]
        except IndexError:
            return int(0)

    def get_count_where(self, col, tbl, wherecol, whereval):
        """Returns the count integer for a query"""
        query = self.select("select count(%s) from %s where %s = '%s'" % (col, tbl, wherecol, whereval))
        try:
            return query[0][0]
        except IndexError:
            return int(0)



    def check_database_counts(self):
        """
        Checks the counts in the databases to make
        sure all test data was added with the right amounts.
        Finally, creates the official test users task/taskevent
        """
        # test select 100 tasks / taskevents from setUp()
        q = self.get_count('task_id', 'Task')
        self.assertTrue(q == MAX_ADD)
        q = self.get_count('id', 'TaskEvent')
        self.assertTrue(q == MAX_ADD)

        # checking tasks
        query = self.select('select * from Task where task_id = 10')
        self.assertTrue(len(query) == 1)

        # check all tasks are stopped
        q = self.get_count_where('id', 'TaskEvent', 'is_started', 0)
        query = self.select('select count(id) from TaskEvent where is_started = 0')
        self.assertTrue(query[0][0] == MAX_ADD)

        # check task does not exist
        query = self.select('select count(task_id) from Task where task_id = 420 and user = "Name 420"')
        self.assertTrue(query[0][0] == 0)

        # now add the task
        new_task = self.add_task(420, 'MANTASK', 'Name 420')
