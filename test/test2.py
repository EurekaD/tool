import re

def extract_dates(text):
    year_pattern = re.compile(r'(\d{4})年')
    month_pattern = re.compile(r'(\d{1,2})月')
    day_pattern = re.compile(r'(\d{1,2})日')

    years = re.findall(year_pattern, text)
    months = re.findall(month_pattern, text)
    days = re.findall(day_pattern, text)

    # 构建日期格式
    formatted_date = ""

    # 添加年份部分
    if years:
        formatted_date += f"{years[0]}"

    # 添加月份部分
    if months:
        formatted_date += f"-{months[0]}"

    # 添加日期部分
    if days:
        formatted_date += f"-{days[0]}"

    return formatted_date

# 示例文段
text = "2022年9月11日是一个特殊的日子。明年可能有更多的进展。"

formatted_date = extract_dates(text)

print("格式化后的日期:", formatted_date)