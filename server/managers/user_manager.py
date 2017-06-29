import time
from database.user_dao import UserDao


class UserManager(object):

	def initialize(self):
		userDao = UserDao()
		userDao.createTable()


	def createUser(self, user):
		userDao = UserDao()
		return userDao.insert(user)


	def getUser(self, token):
		userDao = UserDao()
		return userDao.getUser(token)

