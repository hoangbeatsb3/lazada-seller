from database.database_helper import DatabaseHelper
from utils.string_utils import StringUtils

class SkuDao(object):

    def createTable(self):
        query = '''CREATE TABLE IF NOT EXISTS sku_management(
        			id 				SERIAL		PRIMARY KEY NOT NULL,
                    sku           	TEXT    	NOT NULL,
                    name          	TEXT     	NOT NULL,
                    link			TEXT		NOT NULL,
                    min_price     	INTEGER		NOT NULL,
                    max_price     	INTEGER    	NOT NULL,
                    compete_price 	INTEGER 	NOT NULL,
                    special_price   INTEGER     NOT NULL,
                    state			INTEGER		NOT NULL,
                    repeat_time 	INTEGER 	NOT NULL,
                    created_at 		INTEGER 	NOT NULL,
                    updated_at		INTEGER
                    );'''
        DatabaseHelper.execute(query)


    def getAll(self):
        try:
            query = '''SELECT * from sku_management ORDER BY id DESC LIMIT 100'''
            conn = DatabaseHelper.getConnection()
            cur = conn.cursor()
            cur.execute(query)

            skus = []
            rows = cur.fetchall()
            for row in rows:
                skus.append({
                    "id": row[0],
                    "sku": row[1],
                    "name": row[2],
                    "link": row[3],
                    "min_price": row[4],
                    "max_price": row[5],
                    "compete_price": row[6],
                    "special_price": row[7],
                    "state": row[8],
                    "repeat_time": row[9],
                    "created_at": row[10]
                })

            conn.close()
            return skus
        except Exception as ex:
            print(ex)
            return None

    def getById(self, id):
        try:
            query = '''SELECT * from sku_management WHERE id = '{}' '''.format(id)
            conn = DatabaseHelper.getConnection()
            cur = conn.cursor()
            cur.execute(query)

            skus = []
            rows = cur.fetchall()
            for row in rows:
                skus.append({
                    "id": row[0],
                    "sku": row[1],
                    "name": row[2],
                    "link": row[3],
                    "min_price": row[4],
                    "max_price": row[5],
                    "compete_price": row[6],
                    "special_price": row[7],
                    "state": row[8],
                    "repeat_time": row[9],
                    "created_at": row[10]
                })

            conn.close()
            return skus
        except Exception as ex:
            print(ex)
            return None


    # ---------------------------------------------------------------------------------------
    # Delete KSU
    # ---------------------------------------------------------------------------------------
    def delete(self, sku):
        query = '''DELETE from sku_management where id = '{}' '''.format(sku['id'])
        DatabaseHelper.execute(query)


    # ---------------------------------------------------------------------------------------
    # Insert KSU
    # ---------------------------------------------------------------------------------------
    def insert(self, sku):
        query = '''INSERT INTO sku_management (sku, name, link, min_price, max_price,
    				compete_price, special_price, state, repeat_time, created_at, updated_at)
    				VALUES ('{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, 0)'''.format(
    				StringUtils.toString(sku['sku']), StringUtils.toString(sku['name']), StringUtils.toString(sku['link']),
                    sku['min_price'], sku['max_price'], sku['compete_price'], sku['special_price'], sku['state'], sku['repeat_time'], sku['created_at'])
        DatabaseHelper.execute(query)


    # ---------------------------------------------------------------------------------------
    # Update KSU
    # ---------------------------------------------------------------------------------------
    def update(self, sku):
        # query = '''UPDATE sku_management set sku = '{}', name = '{}', link = '{}', min_price = {}, max_price = {},
    				# compete_price = {}, special_price = {}, state = {}, repeat_time = {}, updated_at = {}
        #             WHERE id = '{}' '''.format(
    				# sku['sku'], sku['name'], sku['link'], sku['min_price'], sku['max_price'],
    				# sku['compete_price'], sku['special_price'], sku['state'], sku['repeat_time'],
        #             sku['updated_at'], sku['id'])
        query = '''UPDATE sku_management set sku = '{}', min_price = '{}', max_price='{}', compete_price='{}', repeat_time='{}', state='{}', link='{}', name='{}', updated_at='{}'
                    WHERE id = '{}' '''.format(
                    sku['sku'], sku['min_price'], sku['max_price'], sku['compete_price'], sku['repeat_time'], sku['state'], sku['link'], sku['name'], sku['updated_at'], sku['id'])
        DatabaseHelper.execute(query)







