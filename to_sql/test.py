import pandas as pd

from sqlalchemy import create_engine

if __name__ == '__main__':
    a = 21
    b = 32
    c = 45
    data = {"total": a, "seven_day_total": b, "today_total": c}
    pd_data_frame = pd.DataFrame(data,index=[0])

    pd_data_frame.to_sql()
    # 替换 'your_table' 为目标表的名称
    table_name = 'homepage_data_count'
    # 替换以下信息为你的数据库连接信息
    db_config = {
        'host': '192.168.1.189:3308',
        'user': 'root',
        'password': 'Dataplatform2023',
        'database': 'public_opinion'
    }
    # 创建 SQLAlchemy 引擎
    engine = create_engine(
        f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

    # 将 DataFrame 写入 MySQL 数据库
    pd_data_frame.to_sql(name=table_name, con=engine, index=False, if_exists='append')
