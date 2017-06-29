import requests
import json
from lazada_api.lazada_api_helper import LazadaApiHelper
from config import LazadaAPI

class LazadaSkuApi(object):

	def getSku(self, sku, user):
		parameters = {
		'Action': 'GetProducts',
		'Format':'JSON',
		'Timestamp': LazadaApiHelper.getCurrentUTCTime(),
		'UserID': user['lazada_user_id'],
		'Version': '1.0',
		'SkuSellerList': '''["{}"]'''.format(sku['sku'])
		}

		parameters['Signature'] = LazadaApiHelper.generateSignature(parameters, user['lazada_api_key'])
		url = "{}/?Action={}&Format={}&Timestamp={}&UserID={}&Version={}&SkuSellerList={}&Signature={}".format(
						LazadaAPI.ENDPOINT,
		 				parameters["Action"], 
		 				parameters["Format"], 
		 				LazadaApiHelper.formatTimestamp(parameters["Timestamp"]), 
		 				parameters["UserID"], 
		 				parameters["Version"],
		 				parameters["SkuSellerList"],
		 				parameters["Signature"])

		resp = requests.get(url)
		if resp.status_code == 200:
			response = json.loads(resp.text)
			if ('ErrorResponse' in response):
				return None

			data = response['SuccessResponse']['Body']
			if (data['TotalProducts'] == 1):
				return data['Products'][0]
			
		return None


	def updateProductSpecialPrice(self, sku, user, newSpecialPrice):
		parameters = {
		'Action': 'UpdateProduct',
		'Format':'JSON',
		'Timestamp': LazadaApiHelper.getCurrentUTCTime(),
		'UserID': user['lazada_user_id'],
		'Version': '1.0'
		}

		parameters['Signature'] = LazadaApiHelper.generateSignature(parameters, user['lazada_api_key'])
		url = "{}/?Action={}&Format={}&Timestamp={}&UserID={}&Version={}&Signature={}".format(
						LazadaAPI.ENDPOINT,
		 				parameters["Action"], 
		 				parameters["Format"], 
		 				LazadaApiHelper.formatTimestamp(parameters["Timestamp"]), 
		 				parameters["UserID"], 
		 				parameters["Version"],
		 				parameters["Signature"])

		xmlBody = LazadaApiHelper.generateUpdateProductXML(sku, newSpecialPrice)

		resp = requests.post(url, data=xmlBody)
		if resp.status_code == 200:
			response = resp.json()
			if ('SuccessResponse' in response):
				return True

		return False
			







