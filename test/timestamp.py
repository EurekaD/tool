import time
import arrow
from datetime import datetime, timedelta


# 获取当前时间 前一天 的 时间戳（以秒为单位）
def get_yesterday_timestamp():
    current_date = datetime.now()
    previous_date = current_date - timedelta(days=1)
    timestamp = int(previous_date.timestamp())
    return timestamp

timestamp = 1698325258
print(datetime.fromtimestamp(timestamp))
