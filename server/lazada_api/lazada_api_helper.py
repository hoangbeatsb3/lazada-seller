import datetime
import hmac, hashlib
from urllib.parse import urlencode, quote_plus


class LazadaApiHelper:

  @classmethod
  def getCurrentUTCTime(self):
    utcnow = datetime.datetime.utcnow().isoformat()
    return utcnow[:-7] + "+00:00"

  @classmethod
  def formatTimestamp(self, timestamp):
    return timestamp.replace(":", "%3A").replace("+","%2B")

  @classmethod
  def generateSignature(self, parameters, lazada_api_key):
    concatenated = urlencode(sorted(parameters.items()))
    key_bytes = bytes(lazada_api_key, 'utf-8')
    data_bytes = bytes(concatenated, 'utf-8')
    return hmac.new(key_bytes, data_bytes, hashlib.sha256).hexdigest()

  @classmethod
  def generateUpdateProductXML(self, sku, price):
    return '''<?xml version="1.0" encoding="UTF-8" ?>
      <Request>
          <Product>
              <Skus>
                  <Sku>
                      <SellerSku>{}</SellerSku>
                      <special_price>{}</special_price>
                  </Sku>
              </Skus>
          </Product>
      </Request>'''.format(sku['sku'], price)









