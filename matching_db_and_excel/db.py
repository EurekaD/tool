import pymysql

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
        self.sql_matching = '''SELECT organization, volume FROM `vote_opinion_survey`
WHERE name_candidate= %s AND approval_rating= %s AND (no_know= %s OR undetermined_rating= %s )
        '''

    def close_dataset(self):
        self.conn.close()

    def matching_db(self, matching_data):
        self.cursor.executemany(self.sql_matching, matching_data)
        return self.cursor.fetchone()

