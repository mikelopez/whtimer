# dev@scidentify.info - Marcos Lopez

from base import *
from wh_timer import *

class TestWHTimer(unittest.TestCase):
	"""
	test the main class.
	"""
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_whtimer(self):
		"""Test the whtimer class"""
		wht = WHTimer()



if __name__ == '__main__':
	unittest.main()