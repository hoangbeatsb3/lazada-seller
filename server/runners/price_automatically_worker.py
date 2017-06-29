import time
import operator
import requests
from time import sleep
from lxml import html
from database.sku_dao import SkuDao
from database.user_dao import UserDao
from lazada_api.lazada_sku_api import LazadaSkuApi


class PriceAutomaticallyWorker(object):

	def execute(self):
		print("*********** Price Automatically is executed ***********")
		skudao = SkuDao()
		skus = skudao.getAll()
		if (skus == None):
			return

		userDao = UserDao()
		user = userDao.getUser("token");
		for sku in skus:
			enemies = self.getEnemies(sku['link'])
			self.priceAlgorithm(enemies, user, sku)


	def priceAlgorithm(self, enemies, user, sku):
		newSpecialPrice = sku['special_price']
		if (enemies == None or len(enemies) < 1):
			return

		# Get enemy have lowest price
		enemies = self.sortEnemies(enemies)
		lowestPriceEnemy = enemies[0]
		lowSecondPriceEnemy = enemies[1]

		# Our product price will be lower then enemy compete_price unit
		newSpecialPrice = lowestPriceEnemy['price'] - sku['compete_price']
		if (user['lazada_user_name'].lower() == lowestPriceEnemy['name'].lower()):
			newSpecialPrice = lowSecondPriceEnemy['price'] - sku['compete_price']

		# But this is not lower then min_price and higher then max_price
		if (newSpecialPrice < sku['min_price']):
			newSpecialPrice = sku['min_price']
		if (newSpecialPrice > sku['max_price']):
			newSpecialPrice = sku['max_price']

		if (sku['special_price'] == newSpecialPrice):
			return

		print ("new special price: ", newSpecialPrice)
		self.doUpdatePrice(sku, newSpecialPrice)


	def doUpdatePrice(self, sku, newSpecialPrice):
		sku['updated_at'] = int(round(time.time()))
		sku['special_price'] = newSpecialPrice
		# Update internal database
		skuDao = SkuDao()
		skuDao.update(sku)
		# Update external database
		userDao = UserDao()
		temporaryUser = userDao.getUser("token");
		lazadaSkuApi = LazadaSkuApi()
		lazadaProduct = lazadaSkuApi.updateProductSpecialPrice(sku, temporaryUser, newSpecialPrice)
		print("*********** Price Automatically do updated price ***********")
		print("Sku: ", sku['sku'], "/nnew special price: ", newSpecialPrice)


	def getEnemies(self, pageUrl):
		enemiesJson = []
		page = requests.get(pageUrl)
		tree = html.fromstring(page.content)

		# Top enemy, will be this user if the user is on the top
		topEnemyPrice = tree.xpath('//*[@id="special_price_box"]/text()')
		topEnemyName = tree.xpath('//*[@id="prod_content_wrapper"]/div[2]/div[2]/div[1]/div[1]/a/text()')
		topEnemyJson = {
			"name": topEnemyName[0],
			"price": int(topEnemyPrice[0].replace('VND', '').replace('.', '').replace(',', ''))
		}
		enemiesJson.append(topEnemyJson)

		# List others enemy
		enemies = tree.xpath('//*[@id="multisource"]/div[2]/table/tr[2]/td[1]/div/div/a/span/text()')
		enemyPrices = tree.xpath('//*[@id="multisource"]/div[2]/table/tr[2]/td[4]/span/text()')
		for index, enemy in enumerate(enemies):
			enemiesJson.append({
				"name": enemy,
				"price": int(enemyPrices[index].replace('VND', '').replace('.', ''))
				})

		print(enemiesJson)
		return enemiesJson


	def sortEnemies(self, enemies):
		return sorted(enemies, key=operator.itemgetter('price'))




