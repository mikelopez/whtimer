# dev@scidentify.info - Marcos Lopez

from base import *

class TestLogic(BaseTest):
    """
    test the main class.
    """
    def setUp(self):
        # create the tables and add some tasks
        self.create_tables()
        self.add_task('Take a poop')
        self.add_task('Play Guitar')
        self.add_task('Eat some food')



    def tearDown(self):
        #self.destroy_tables()
        termprint("WARNING", "Exiting....Deleting Database")
        os.system('rm test.db')
        pass


    def test_whtimer(self):
        """Test the whtimer class"""
        from wh_timer import *
        wht = WHTimer()

    def test_select(self):
        """Test the select functionality"""
        termprint("INFO", "Tasks %s" % str(self.select('SELECT * from Task')))


    def test_logic(self):
        pass




if __name__ == '__main__':
    unittest.main()
