import sqlite3 as sql
import sys

# dev@scidentify.info - Marcos Lopez

DB_FILE = "test.db"
create_tables = [
    "CREATE TABLE Task(id INT PRIMARY KEY ASC, name TEXT);",
    "CREATE TABLE StartEvent(id INT PRIMARY KEY ASC,task_id INT,action TEXT,date DATETIME default current_timestamp);",
    "CREATE TABLE StopEvent(id INT PRIMARY KEY ASC,task_id INT,action TEXT,date DATETIME default current_timestamp);",
]

class Database(object):
	"""
	Quick Database wrapper for sqlite3 for testing
	"""
	result = None
	connection = False

	def __init__(self, *args, **kwargs):
		"""Connect if kwargs present"""
		if kwargs:
			if kwargs.get('connect'):
				# try to connect
				self.connect(*args, **kwargs)


	def maketables(self):
		"""Create the tables for testing."""
		for i in create_tables:
			self.query(i)
			

	def connect(self, *args, **kwargs):
		"""Connect to the database api fields."""
		try:
			self.connection = sql.connect(DB_FILE)
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