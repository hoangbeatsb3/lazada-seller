from database.sku_dao import SkuDao


class SkuManager(object):

	def initialize(self):
		skudao = SkuDao()
		skudao.createTable()


	def insertSku(self, sku):
		skudao = SkuDao()
		skudao.insert(sku)


	def deleteSku(self, sku):
		skudao = SkuDao()
		skudao.delete(sku)


	def getAll(self, token):
		skudao = SkuDao()
		return skudao.getAll()

	def getById(self, id):
		skudao = SkuDao()
		return skudao.getById(id)

	def updateSku(self, sku):
		skudao = SkuDao()
		return skudao.update(sku)
