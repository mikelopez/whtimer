# dev@scidentify.info - Marcos Lopez

from base import *

MAX_ADD = 50

class TestLogic(BaseTest):
    """
    test the main class.
    """
    def setUp(self):
        """First create 100 task tests"""
        self.create_tables(dbfile="testdb.logic.db")
        self.logw("** Adding 50 Test Tasks")
        for n in range(1, (MAX_ADD+1)):
            randstr = str(randint(111, 999))
            self.add_task(n, "Task %s" % randstr, "Name %s" % randstr)
            started = (datetime.now() - timedelta(hours=3))
            ended = (datetime.now() - timedelta(hours=2))
            diff = (ended - started).seconds
            self.add_task_event(n, n, "Name %s" % randstr, 0, 
                                started, ended, diff)
                                
        
        
    def tearDown(self):
        termprint("WARNING", "Exiting....Deleting Database")
        #os.system('rm test.db')


    def __check_database_counts(self):
        """
        Checks the counts in teh databases to make
        sure all test data was added with the right amounts.
        Finally, creates the official test users task/taskevent
        """
        # test select 100 tasks / taskevents from setUp()
        query = self.select('select count(task_id) from Task')
        self.loge("Returned %s" % len(query))
        self.assertTrue(len(query) == MAX_ADD)
        query = self.select('select count(id) from TaskEvent')
        self.assertTrue(len(query) == MAX_ADD)

        # checking tasks
        query = self.select('select * from Task where task_id = 10')
        self.assertTrue(len(query) == 1)

        # check all tasks are stopped
        query = self.select('select count(id) from TaskEvent where stopped = 0')
        self.assertTrue(len(query) == MAX_ADD)

        # check task does not exist
        c = self.select('select count(task_id) from Task where task_id = 420 and user = "Name 420"')
        self.assertTrue(len(c) == 0)

        # now add the task
        new_task = self.add_task(420, 'MANTASK', 'Name 420')



    def __check_task_exists(self):
        """Check if the task exists for the user so we can create or update.
        Could possibly avoid this by always adding the task event when adding a task"""
        c = self.select('select count(id) from TaskEvent where task_id = 420 and user = "Name 420"')
        if len(c) > 0:
            return True 
        return False

    def __insert_taskevent(self):
        """Inserts a brand new task event with minutes sum hardcoded to 0."""
        self.add_task_event(420, 420, "Name 420", 0, datetime.now(), None, 0)


    def __check_task_running(self):
        """Checks if the task is running if query result is > 0"""
        c = self.select('select count(id) from TaskEvent where task_id = 420 and user = "Name 420" and is_started = 1')
        if len(c) > 0:
            return True
        return True


    def test_logic(self):
        # check the class
        from wh_timer import *
        wht = WHTimer()

        # check database counts
        self.__check_database_counts()

        # user wants to start a task after creating it
        # first check if it exists
        self.assertFalse(self.__check_task_exists())
        self.assertFalse(self.__check_task_running())
        # now add the tasks event
        self.insert_taskevent()
        self.assertTrue(self.__check_task_exists())



        

        pass




if __name__ == '__main__':
    unittest.main()











