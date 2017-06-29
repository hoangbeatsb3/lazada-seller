import psycopg2
from config import Database


class DatabaseHelper:

	@classmethod
	def getConnection(self):
		return psycopg2.connect(database = Database.DATABASE, user = Database.USER, password = Database.PASSWORD, host = Database.HOST, port = Database.PORT)

	@classmethod
	def execute(self, query):
		try:
			conn = psycopg2.connect(database = Database.DATABASE, user = Database.USER, password = Database.PASSWORD, host = Database.HOST, port = Database.PORT)
			cur = conn.cursor()
			cur.execute(query)
			conn.commit()
			conn.close()
			return True
		except Exception as ex:
			print(ex)
			return False






