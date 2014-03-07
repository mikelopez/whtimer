import sqlite3 as sql
import sys

# dev@scidentify.info - Marcos Lopez

DB_FILE = "test.db"
create_tables = [
    "CREATE TABLE Task(task_id INT PRIMARY KEY ASC, name TEXT, user TEXT);",
    "CREATE TABLE StartEvent(id INT PRIMARY KEY ASC, task_id INT,\
    	action TEXT,date DATETIME default current_timestamp, user TEXT);",
    "CREATE TABLE StopEvent(id INT PRIMARY KEY ASC, task_id INT,\
    	action TEXT,date DATETIME default current_timestamp, user TEXT);",
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


	def query(self, query, commit=True):
		"""Run a select query."""
		cur = self.connection.cursor()
		cur.execute(query)
		self.connection.commit()
		return cur

			
	def select(self, query):
		"""Return the query result."""
		cur = self.query(query, commit=False)
		data = cur.fetchall()
		return data


	def close(self):
		"""Closes the connection."""
		if getattr(self, 'connection'):
			getattr(self, 'connection').close()
