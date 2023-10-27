import csv
import os
import pymysql

output_folder = r"D:/ikcest/ikcest_journal_article"

conn = pymysql.connect(
            host='rm-2zeh92y201tfh5pdh.mysql.rds.aliyuncs.com',
            port=3306,
            user='ikcest-prod-new',
            password='ikcest-prod-new@ikcest.org',
            database='ikcest_dev',
            charset='utf8'
        )
cursor = conn.cursor()

# 导出2000万行，分为50个excel文件，每个文件40万行
page_size = 400000

# 分页导出
for page in range(1, 51):
    offset = (page - 1) * page_size
    query = f"SELECT * FROM ikcest_journal_article LIMIT {page_size} OFFSET {offset}"
    cursor.execute(query)
    data = cursor.fetchall()

    # 获取列名
    column_names = [column[0] for column in cursor.description]

    # 构建文件名
    csv_file = os.path.join(output_folder, f'ikcest_journal_article_page_{page}.csv')

    # 写入CSV文件
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)

        # 写入列名
        csv_writer.writerow(column_names)

        # 写入数据
        csv_writer.writerows(data)

# 关闭数据库连接
conn.close()

print(f"表数据已成功分页导出到 '{output_folder}' 文件夹。")