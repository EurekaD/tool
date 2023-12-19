
"""
保存 接口返回的数据
"""
import pymysql
import requests
import time

class DB:
    # 定义mysql连接信息
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.1.162',
            port=3307,
            user='dataplatform',
            password='Dataplatform@2021',
            database='2024election',
            charset='utf8'
        )

        self.cursor = self.conn.cursor()
        self.sql_insert = """
        REPLACE INTO api_result (time, name, result) VALUES( %s, %s, %s)
        """

    def close_dataset(self):
        self.conn.close()

    def insert_db(self, data):
        self.cursor.executemany(self.sql_insert, data)
        self.conn.commit()



class ApiResultSave():
    def __init__(self):
        self.url = 'http://192.168.1.162:9011/election-model-api/system/data/query?'
        self.data = []
        self.db = DB()

    def api(self):
        res = requests.get(self.url, params={"type": '2'})
        res = res.json()["data"]
        return res

    def get_api_result(self):
        for i in range(4):
            res = self.api()[i]
            time_ = time.localtime()
            name = res["name"]
            result = res['result']
            self.data.append((time_, name, result))
        return self.data

    def save(self):
        self.db.insert_db(self.data)


if __name__ == '__main__':
    api_result_save = ApiResultSave()
    api_result_save.get_api_result()
    api_result_save.save()


