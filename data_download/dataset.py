import pymysql

class Dataset:
    # 定义mysql连接信息
    def __init__(self, start_id, data_range):
        self.conn = pymysql.connect(
            host='rm-cn-x0r3ape70000lc5o.rwlb.rds.aliyuncs.com',
            port=3306,
            user='chenlin',
            password='Chenlin6',
            database='vidsummarize_text',
            charset='utf8'
        )

        self.data = []
        self.data_range = data_range
        self.start_id = start_id
        self.cursor = self.conn.cursor()

    def __iter__(self):
        return self.get_text()

    def __len__(self):
        pass

    def close_dataset(self):
        self.conn.close()

    def update_label(self, id, labels):
        self.data = []
        self.data.append((labels, id))
        self.write_to_db_update()

    def write_to_db_update(self):
        self.cursor.executemany(self.update_label_sql, self.data)
        self.conn.commit()

    def get_text(self):
        """
        迭代器，随机返回数据库中的一条数据
        :return:
        """
        for id in range(self.start_id, self.data_range+1):
            self.cursor.execute("SELECT content, summary FROM train_text WHERE id=%s", id)
            result = self.cursor.fetchone()
            content = result[0].split()
            summary = result[1].split()
            yield content, summary