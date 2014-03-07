# dev@scidentify.info - Marcos Lopez

DB_FILE = "test.db"

class Database(object):
	"""
	Database class handling connection and sql queries
	"""
	def __init__(self):
		if kwargs:
			# try to connect
			try:
				con = sql.connect(DB_FILE)
			except sql.Error, e:
				sys.exit(1)