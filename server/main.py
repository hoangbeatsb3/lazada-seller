import time
from managers.sku_manager import SkuManager
from managers.user_manager import UserManager
from apis.sku_api import SkuAPI
from flask import Flask
from flask_cors import CORS, cross_origin
from time import sleep

app = Flask(__name__)
CORS(app)	# Should allow CORS only for our domain.
app.register_blueprint(SkuAPI)

if __name__ == "__main__":

  # userManager = UserManager()
  # user = {		
  # 	"user_name": "admin",        
  # 	"password": "null",        
  # 	"token": "token",        
  # 	"lazada_user_name": "lakami",        
  # 	"lazada_user_id": "info@lakami.vn",        
  # 	"lazada_api_key": "YMwE4W9gj6eSNiZ9ZVXvZBnQ0metPkDgnp952URBhCYHG5VfxAlSvcUk",        
  # 	"created_at": int(round(time.time()))	
  # }	
  # userManager.createUser(user)
  skuManager = SkuManager()
  userManager = UserManager()
  skuManager.initialize()
  userManager.initialize()

  app.run(debug=True)




