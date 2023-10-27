import re

import pandas as pd
import pymysql

output_folder = r"E:/期刊论文和专利/期刊论文/"

conn = pymysql.connect(
            host='rm-2zeh92y201tfh5pdh.mysql.rds.aliyuncs.com',
            port=3306,
            user='ikcest-prod-new',
            password='ikcest-prod-new@ikcest.org',
            database='ikcest_dev',
            charset='utf8'
        )

last_id = 2825306

def clean_data(text):
    if isinstance(text, str):
        # 使用正则表达式删除非法字符
        cleaned_text = re.sub(r'[\000-\010]|[\013-\014]|[\016-\037]', '', text)
        return cleaned_text
    else:
        return text

def contains_illegal_chars(text):
    if isinstance(text, str):
        # 使用正则表达式检查是否包含非法字符
        return bool(re.search(r'[^\x00-\x7F]', text))
    else:
        return False  # 非字符串类型直接返回 False

# 分页导出
for page in range(15, 51):
    # 优化查询语句，offset跳过前面的行，但仍然会扫描，随着offset增大，查询速度很慢，
    # 因为 Limit 400000 Offset 20000000 要扫描2040W行前的所有行，再丢弃前2000w行
    # 而 WHERE id > {last_id} LIMIT 400000 只扫描大于last_id的行,虽然大于他的行可能更多，但是limit限制只要40w,所有只扫描40w,前提是id是自增的
    # 如果id没有断裂，使用 between and 也可优化查询

    # query = f"SELECT * FROM ikcest_patent LIMIT {page_size} OFFSET {offset}"
    query = f"SELECT * FROM ikcest_journal_article WHERE id > {last_id} LIMIT 200000"

    # 执行查询
    df = pd.read_sql_query(query, conn)

    last_id = df.iloc[-1, 0]
    print(last_id)

    columns_to_drop = ['createUser']  # 替换为实际要删除的列名
    df = df.drop(columns=columns_to_drop, axis=1)
    df = df.applymap(clean_data)
    # df = df[~df.apply(lambda row: any(row.apply(contains_illegal_chars)), axis=1)]
    # 定义保存路径
    excel_file = output_folder + "期刊论文_{}.xlsx".format(page)

    # 将数据保存为 Excel 文件
    df.to_excel(excel_file, index=False)

# 关闭数据库连接
conn.close()

print(f"表数据已成功分页导出到 '{output_folder}' 文件夹。")