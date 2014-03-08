# dev@scidentify.info - Marcos Lopez

from base import *


DB_FILE = "test.timecomplex.db"
info, err, warn = "INFO", "ERROR", "WARNING"

class TestTimeComplexity(BaseTest):
	"""
	Test the time complexity of growing results
	"""
	def setUp(self):
		self.create_tables(dbfile="test.timecomplex.db")

	def tearDown(self):
		termprint(warn, "Deleting database")
		#os.system('rm %s' % DB_FILE)

	def __process_task(self, start_from=1, max=0):
		"""
		Adds a user n times
		"""
		termprint(info, "Adding %s Tasks" % max)
		start = datetime.now()
		termprint(err, "%s STARTED" % start)
		for n in range(start_from, max):
			randstr = str(randint(1111, 99999))
			self.add_task(n, "Task %s" % randstr, "Name %s" % randstr)
		end = datetime.now()
		termprint(err, '%s ENDED' % end)
		termprint(err, 'TOOK %s seconds' % (end - start).seconds)

	def test_to_1000(self):
		"""Adds a thousand users, tasks, and task events."""
		self.__process_task(start_from=1, max=10)
		self.__process_task(start_from=11, max=100)
		self.__process_task(start_from=101, max=200)
		self.__process_task(start_from=201, max=300)
		self.__process_task(start_from=301, max=500)
		




if __name__ == "__main__":
	unittest.main()
