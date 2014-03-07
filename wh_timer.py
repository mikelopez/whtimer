# dev@scidentify.info - Marcos Lopez

DB_FILE = "test.db"

class Database(object):
	"""
	Quick Database wrapper for sqlite3 for testing
	"""
	result = None
	connection = False

	def __init__(self):
		"""Connect if kwargs present"""
		if kwargs:
			# try to connect
			self.connect(*args, **kwargs)
			

	def connect(self, *args, **kwargs):
		"""Connect to the database api fields."""
		try:
			connection = sql.connect(DB_FILE)
			
		except sql.Error, e:
			raise Exception("Error connecting: %s" % e)
			sys.exit(1)

			
	def query(self, query):
		"""Return the query result."""
		cur = self.connection.cursor()
		cur.execute(query)
		data = cur.fetchone()
		return data


	def close(self):
		"""Closes the connection."""
		if getattr(self, 'con'):
			getattr(self, 'con').close()