# dev@scidentify.info - Marcos Lopez

from base import *


class TestLogic(BaseTest):
    """
    test the main class.
    """
    def setUp(self):
        """First create 100 task tests"""
        self.create_tables(dbfile="testdb.logic.db")
        self.logw("** Adding %s Test Tasks" % MAX_ADD)
        for n in range(1, (MAX_ADD + 1)):
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


    def __check_task_exists(self, task_id, user):
        """Check if the task exists for the user so we can create or update.
        Could possibly avoid this by always adding the task event when adding a task"""
        c = self.select('select count(id) from TaskEvent where task_id=%s and user="%s"' % (task_id, user))
        try:
            if int(c[0][0]) > 0:
                return True 
            return False
        except IndexError:
            return False


    def __insert_taskevent(self, startdate=None, enddate=None):
        """Inserts a brand new task event with minutes sum hardcoded to 0."""
        self.add_task_event(420, 420, "Name 420", 0, startdate, enddate, 0)


    def __stopall(self, user):
        """Stops all the processes.
        TODO: Need to check if this takes longer than just doing a count(id) and running 
        the update only if the count returns something larger than 0
        """
        for row in self.select('select * from TaskEvent where user = "%s"' % user):
            rowd = {'is_started': row[3], 'sum_sec': int(row[6]), 'start': row[4],
                    'task_id': row[1], 'user': row[2]}
            if rowd.get('is_started') == int(1):
                if start:
                    sumsec += (datetime.now() - rowd.get('start')).seconds
                    self.__stop_task(rowd.get('start'), rowd.get('task_id'), rowd.get('user'))
                else:
                    # something is wrong here, should reupdate 
                    self.__stop_task(datetime.now(), rowd.get('task_id'), rowd.get('user'))
                    pass


    def __stop_task(self, start_date, task_id, user):
        """Stops a task for a user, and updates the minutes sum"""
        minutes_sum = (datetime.now() - start_date).seconds
        q = 'update TaskEvent set is_started=0, stop="%s", minutes_sum=(minutes_sum + %s) ' % (
            datetime.now(), minutes_sum)

        q += 'where task_id=%s and user="%s"' % (task_id, user)
        self.query(q)


    def __start_task(self, task_id, user, startdate=datetime.now()):
        """Starts the task for a user."""
        self.__stopall(user)
        self.query('update TaskEvent set is_started=1, start="%s" where task_id=%s and user="%s"' %\
                   (startdate, task_id, user));


    def __check_task_running(self, task_id, user):
        """Checks if the task is running if query result is > 0"""
        query = 'select count(id) from TaskEvent where '
        query += 'task_id=%s and user="%s" and is_started=1' % (task_id, user)
        c = self.select(query)
        try:
            if c[0][0] > 0:
                return True
            return False
        except IndexError:
            return False


    def test_logic(self):
        """
        Tests the main logic.
        Only one started task per user.
        When starting a task, stop all tasks.
        Update the minutes sum for each of the stopped tasks for a user
        Set the requested task as started.
        """
        from wh_timer import *
        wht = WHTimer()

        # check database counts and add a test task to work with (420)
        self.check_database_counts()

        # user wants to start a task after creating it
        # first check if it exists
        self.assertFalse(self.__check_task_exists(420, "Name 420"))
        self.assertFalse(self.__check_task_running(420, "Name 420"))

        # now add the tasks event as blank date since its the first add (stopped)
        self.__insert_taskevent()
        self.assertTrue(self.__check_task_exists(420, "Name 420"))

        for i in range(0, 3):
            started = (datetime.now() - timedelta(minutes=10))
            self.__start_task(420, "Name 420", startdate=started)
            self.assertTrue(self.__check_task_running(420, "Name 420"))
            # stop it now 10 min later
            self.__stop_task(started, 420, "Name 420")
            self.assertFalse(self.__check_task_running(420, "Name 420"))
  
        q = self.select('select minutes_sum from TaskEvent where user = "%s" and task_id = "%s"' % ("Name 420", 420))
        self.assertTrue(q[0][0] == int(30 * 60))
        self.__print_results()


    def __print_results(self):
        """Print an ugly table on terminal.....yeah!"""
        results = self.select('select * from TaskEvent')
        print "| ID\t| Task\t| User\t| Started\t| Start Date\t| End Date\t| Total Seconds"
        print '-----------------------------------------------------------------------------------------------------------------'
        for i in results:
            row = ""
            for col in i:
                row += "| %s\t" % col
            print row
            print "-----------------------------------------------------------------------------------------------------------------"


if __name__ == '__main__':
    unittest.main()











