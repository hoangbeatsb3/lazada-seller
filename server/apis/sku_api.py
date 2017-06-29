import time
import simplejson as json
from flask_cors import CORS, cross_origin
from flask import Blueprint, render_template, abort, request, make_response, jsonify
from managers.sku_manager import SkuManager
from managers.user_manager import UserManager
from lazada_api.lazada_sku_api import LazadaSkuApi


SkuAPI = Blueprint('sku_api', __name__, template_folder='apis')


# ---------------------------------------------------------------------------------------
# Get All KSU
# ---------------------------------------------------------------------------------------
@SkuAPI.route('/sku/get-all', methods=['GET'])
@cross_origin()
def getAll():
	if not request.args:
		return make_response(jsonify({'error': 'Missig token parameter value'}), 404)

	skuManager = SkuManager()
	return make_response(jsonify({"data": skuManager.getAll(request.args.get('token'))}))

# ---------------------------------------------------------------------------------------
# Get By Id KSU
# ---------------------------------------------------------------------------------------
@SkuAPI.route('/sku/get-by-id', methods=['GET'])
@cross_origin()
def getById():
	if not request.args:
		return make_response(jsonify({'error': 'Missig token parameter value'}), 404)

	skuManager = SkuManager()
	return make_response(jsonify({"data": skuManager.getById(request.args.get('id'))}))

# ---------------------------------------------------------------------------------------
# Delete KSU
# ---------------------------------------------------------------------------------------
@SkuAPI.route('/sku/delete', methods=['POST'])
@cross_origin()
def delete():
	if not request.json:
		return make_response(jsonify({'error': 'Missig json parameters value'}), 404)
	if not 'id' in request.json:
		return make_response(jsonify({'error': 'Missig sku parameter'}), 404)

	sku = {
		"id": request.json['id']
	}

	skuManager = SkuManager()
	skuManager.deleteSku(sku)
	return make_response(jsonify({"success": "done"}))


# ---------------------------------------------------------------------------------------
# Insert KSU
# ---------------------------------------------------------------------------------------
@SkuAPI.route('/sku/insert', methods=['POST'])
@cross_origin()
def insert():
	if not request.json:
		return make_response(jsonify({'error': 'Missig json parameters value'}), 404)
	if not 'sku' in request.json:
		return make_response(jsonify({'error': 'Missig sku parameter'}), 404)
	if not 'min_price' in request.json:
		return make_response(jsonify({'error': 'Missig min_price parameter'}), 404)
	if not 'max_price' in request.json:
		return make_response(jsonify({'error': 'Missig max_price parameter'}), 404)
	if not 'compete_price' in request.json:
		return make_response(jsonify({'error': 'Missig compete_price parameter'}), 404)
	if not 'state' in request.json:
		return make_response(jsonify({'error': 'Missig state parameter'}), 404)
	if not 'repeat_time' in request.json:
		return make_response(jsonify({'error': 'Missig repeat_time parameter'}), 404)

	sku = {
		"id": request.json['id'],
		"sku": request.json['sku'],
		"name": "null",
		"link": "null",
		"min_price": int(request.json['min_price']),
		"max_price": int(request.json['max_price']),
		"compete_price": int(request.json['compete_price']),
		"special_price": 0,
		"state": int(request.json['state']),
		"repeat_time": int(request.json['repeat_time']),
		"created_at": int(round(time.time()))
	}

	userManager = UserManager()
	temporaryUser = userManager.getUser("token");

	lazadaSkuApi = LazadaSkuApi()
	lazadaProduct = lazadaSkuApi.getSku(sku, temporaryUser)

	if (lazadaProduct):
		sku['name'] = lazadaProduct['Attributes']['name'].encode('utf-8')
		sku['link'] = lazadaProduct['Skus'][0]['Url'].encode('utf-8')
		sku['special_price'] = lazadaProduct['Skus'][0]['special_price']
		skuManager = SkuManager()
		skuManager.insertSku(sku)
		return make_response(json.dumps(sku), 201)
	else:
		return make_response(jsonify({'error': 'Seller SKU is wrong !!!'}), 404)


# ---------------------------------------------------------------------------------------
# Update KSU
# ---------------------------------------------------------------------------------------
@SkuAPI.route('/sku/update', methods=['POST'])
@cross_origin()
def update():
	if not request.json:
		return make_response(jsonify({'error': 'Missig json parameters value'}), 404)
	if not 'id' in request.json:
		return make_response(jsonify({'error': 'Missig id parameter'}), 404)
	if not 'sku' in request.json:
		return make_response(jsonify({'error': 'Missig sku parameter'}), 404)
	if not 'min_price' in request.json:
		return make_response(jsonify({'error': 'Missig min_price parameter'}), 404)
	if not 'max_price' in request.json:
		return make_response(jsonify({'error': 'Missig max_price parameter'}), 404)
	if not 'compete_price' in request.json:
		return make_response(jsonify({'error': 'Missig compete_price parameter'}), 404)
	if not 'state' in request.json:
		return make_response(jsonify({'error': 'Missig state parameter'}), 404)
	if not 'repeat_time' in request.json:
		return make_response(jsonify({'error': 'Missig repeat_time parameter'}), 404)

	sku = {
		"id": request.json['id'],
		"sku": request.json['sku'],
		"name": "123",
		"link": "123",
		"min_price": int(request.json['min_price']),
		"max_price": int(request.json['max_price']),
		"compete_price": int(request.json['compete_price']),
		# # "special_price": 0,
		"state": int(request.json['state']),
		"repeat_time": int(request.json['repeat_time']),
		"updated_at": int(round(time.time()))
	}
	skuManager = SkuManager()
	skuManager.updateSku(sku)
	return make_response(json.dumps(sku), 201)










