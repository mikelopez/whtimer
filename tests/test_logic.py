# dev@scidentify.info - Marcos Lopez

from base import *

class TestLogic(BaseTest):
    """
    test the main class.
    """
    def setUp(self):
        # create the tables and add some tasks
        self.create_tables()
        self.add_task(1, 'Hack the planet', "Mike")
        self.add_task(2, 'Play with Mason & eat', "Mike")
        self.add_task(3, 'Put Mason to Bed', "Mike")

        self.add_task(4, 'Wake up', "Mason")
        self.add_task(5, 'Play, Eat, Poop', "Mason")
        self.add_task(6, 'Eat some food', "Mason")

        self.add_task(7, 'Feeds Mason', "Mike")
        self.add_task(8, 'Play with Mason', "Mike")
        self.add_task(9, 'Put Mason to Bed', "Mike")


    def tearDown(self):
        #self.destroy_tables()
        termprint("WARNING", "Exiting....Deleting Database")
        #os.system('rm test.db')
        pass


    def test_whtimer(self):
        """Test the whtimer class"""
        from wh_timer import *
        wht = WHTimer()


    def test_select(self):
        """Test the select functionality"""
        termprint("INFO", "Tasks %s" % str(self.select('SELECT id, name from Task')))


    def test_logic(self):
        # test starting a task
        mike, mason, jade = "Mike", "Mason", "Jade"

        # Start the task
        self.start_task(mike, 1)
        self.start_task(mason, 4)
        self.start_task(jade, 7)

        self.user_has_task_running()
        pass




if __name__ == '__main__':
    unittest.main()
