"""
复制数据库中每个表的最后一条数据，到该表，即添加一条新数据（时间上要取当前的时间）
"""



import uuid
import pymysql
import time


class Add:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.1.222',
            port=3306,
            user='root',
            password='Rz@2021!',
            database='dp_ads',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
        self.add()

    # 给数据库每个表添加一条新数据（它和上一条最新数据除时间相关的字段外都相同）
    def add(self):
        # print(self.latest_data())
        for table_name in self.all_table_name():
            # 过滤不需要添加的表
            if table_name in ["ads_assets", "ads_business_license"]:
                continue

            print('table_name ' + table_name)
            keys = self.get_table_keys(table_name)
            if len(keys) == 1:
                # print('table_keys ' + keys[0])
                key = keys[0]
            elif len(keys) == 0:
                # print('这个没有主键') 没有主键就以 etl_id
                key = 'etl_id'
            else:
                # print('这个表主键不唯一')
                # print('table_keys ' + keys[0] +" " + keys[1])
                key = keys[0]

            items = self.latest_data(table_name, key)
            if items is not None:
                self.insert_into_table(table_name, items)

    # 获取数据库的所有表名
    def all_table_name(self):
        # 执行 SQL 查询语句获取所有表名
        self.cursor.execute("SHOW TABLES;")
        tables = self.cursor.fetchall()
        # 遍历表名并执行操作
        for table in tables:
            table_name = table[0]
            yield table_name
            # break

    # 获取该表的主键,通过主键得到最新的的一条数据
    def get_table_keys(self, table_name):
        self.cursor.execute(f"SHOW KEYS FROM `{table_name}` WHERE Key_name = 'PRIMARY';")
        primary_key_info = self.cursor.fetchall()
        column_name = []
        for key_info in primary_key_info:
            column_name.append(key_info[4])
        return column_name

    # 插入数据
    def insert_into_table(self, table_name, items):
        # 构建插入语句
        # columns = ', '.join(items.keys())
        columns = ', '.join(f'`{key}`' for key in items.keys())
        values = ', '.join(['%s' for _ in range(len(items))])
        query = f"REPLACE INTO `{table_name}` ({columns}) VALUES ({values})"
        # print(query)
        # 执行插入
        self.cursor.execute(query, tuple(items.values()))
        # 提交事务
        self.conn.commit()

    # 获取最新的一条数据
    def latest_data(self, table_name, key):
        # 执行查询语句
        query = "SELECT * FROM `{}` ORDER BY `{}` DESC LIMIT 1".format(table_name, key)
        self.cursor.execute(query)

        # 获取结果
        latest_row = self.cursor.fetchone()

        # 关闭连接
        # self.cursor.close()
        # self.conn.close()

        self.cursor.execute(f"SHOW COLUMNS FROM `{table_name}`")
        columns = [column[0] for column in self.cursor.fetchall()]

        items = {}

        if latest_row != None:
            # 将列名和最新一行的数据一一对应
            for column, value in zip(columns, latest_row):
                items[column] = value

            # 主键必须在下面进行处理

            items["etl_create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            items["etl_update_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            items["etl_id"] = uuid.uuid1()

            if "create_time" in items and items["create_time"] is not None:
                if ":" in str(items["create_time"]):
                    #items["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    items["create_time"] = "2023-09-17 10:03:32"
                else:
                    #current_year_month = time.strftime("%Y%m", time.localtime())
                    current_year_month = "202309"
                    items["create_time"] = current_year_month
                # 当 create_time 是主键时，每月执行一次？



            if "id" in items:
                if type(items["id"]) == int:
                    items["id"] = items["id"] + 1
                else:
                    items["id"] = time.strftime("%Y%m", time.localtime())

            if "ID" in items:
                if type(items["ID"]) == int:
                    items["ID"] = items["ID"] + 1

            if table_name == "ads_cockpit_ym":
                items["id"] = time.strftime("%Y%m", time.localtime())

            if items["etl_create_date"] is not None:
                items["etl_create_date"] = time.strftime("%Y-%m-%d", time.localtime())

            if items["etl_update_date"] is not None:
                # items["etl_update_date"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if ":" in items["etl_update_date"]:
                    # 如果包含冒号，说明是 "%Y-%m-%d %H:%M:%S" 的格式
                    items["etl_update_date"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                else:
                    # 否则，假设是 "%Y-%m-%d" 的格式
                    items["etl_update_date"] = time.strftime("%Y-%m-%d", time.localtime())

            print(items)
            return items
        else:
            return None

if __name__ == "__main__":
    test = Add()
