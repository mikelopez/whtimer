# dev@scidentify.info - Marcos Lopez

from base import *

class TestMakeTables(unittest.TestCase):
	"""
	Create the tables that will be used 
	for the testing.
	"""
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_create_tables(self):
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
				self.assertTrue("Not creating duplicates....")
		termprint("INFO", "DONE")



if __name__ == '__main__':
	unittest.main()