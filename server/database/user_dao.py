import psycopg2
from database.database_helper import DatabaseHelper


class UserDao(object):

    def createTable(self):
        query = '''CREATE TABLE IF NOT EXISTS t_user(
                    id                  SERIAL		PRIMARY KEY NOT NULL,
                    user_name           TEXT     	NOT NULL,
                    password            TEXT        NOT NULL,
                    token               TEXT        NOT NULL,
                    lazada_user_name    TEXT,
                    lazada_user_id      TEXT,
                    lazada_api_key      TEXT,
                    created_at          INTEGER 	NOT NULL,
                    updated_at          INTEGER     
                    );'''
        DatabaseHelper.execute(query)


    def insert(self, user):
        query = '''INSERT INTO t_user (user_name, password, token, lazada_user_name, lazada_user_id, lazada_api_key, created_at, updated_at) 
                    VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {}, 0)'''.format(
                    user['user_name'], user['password'], user['token'], user['lazada_user_name'], user['lazada_user_id'], 
                    user['lazada_api_key'], user['created_at'])
        DatabaseHelper.execute(query)


    def getUser(self, token):
        try:
            query = '''SELECT lazada_user_name, lazada_user_id, lazada_api_key FROM t_user WHERE token={}'''.format(token)
            conn = DatabaseHelper.getConnection()
            cur = conn.cursor()
            cur.execute(query)

            user = {
                "lazada_user_name": "",
                "lazada_user_id": "",
                "lazada_api_key": "",
            }
            rows = cur.fetchall()
            for row in rows:
                user['lazada_user_name'] = row[0]
                user['lazada_user_id'] = row[1]
                user['lazada_api_key'] = row[2]
            conn.close()

            return user
        except Exception as ex:
            print(ex)
            return None





