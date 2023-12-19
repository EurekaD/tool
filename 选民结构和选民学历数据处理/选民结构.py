from Tools.OpenccUtils import ctoswLite, ctosw
import pandas as pd
import numpy as np
excel_path1 = r"C:\Users\RZ\OneDrive\桌面\台湾各地关于教育程度和年龄的人口数据表\彰化县.xlsx"
excel_path2 = r'C:\Users\RZ\OneDrive\桌面\立委专项数据\xm_voter_info.xlsx'

excel_file = pd.ExcelFile(excel_path1)
df1 = excel_file.parse(sheet_name='Sheet1')
# df1 = pd.read_excel(excel_path1)
df2 = pd.read_excel(excel_path2)

age_list_pro = ['20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65岁以上']
data_zero = [0,0,0,0,0,0,0,0,0,0]
city = '彰化县'

# print(df1['20歲'])


def age_list2(range_str):
    list_ = []
    if range_str == '65岁以上':
        return ['65-69岁', '70-74岁', '75-79岁', '80-84岁', '85-89岁', '90-94岁', '95-99岁', '100岁以上']

    list_.append(range_str + '岁')
    return list_


def age_list(range_str):
    list_ = []
    if range_str == '65岁以上':
        for i in range(65, 100):
            list_.append(str(i) + '歲')
        list_.append('100歲以上')
        return list_

    start = int(range_str[0:2])
    for i in range(start, start+5):
        list_.append(str(i)+'歲')
    return list_



def excel_class_1():
    for index, row in df2[df2['city'] == city].iterrows():
        detail_areas = str(row['detail_info']).split('，')
        print(detail_areas)

        data = dict(list(zip(age_list_pro, data_zero)))
        # 一个 市 的一个选区
        for area in detail_areas:
            # print(area)
            for age_range in age_list_pro:
                # print(age_range)
                # 一个选区下的一个区
                df_area = df1[(df1['區域別'] == ctoswLite(area)) & (df1['性別'] == '計')]
                data[age_range] = data[age_range] + df_area[age_list(age_range)].sum().values.sum()

        print(data)


def excel_class_2():
    for index, row in df2[df2['city'] == city].iterrows():
        detail_areas = str(row['detail_info']).split('，')
        print(detail_areas)

        data = dict(list(zip(age_list_pro, data_zero)))
        # 一个 市 的一个选区
        for area in detail_areas:
            # print(area)
            for age_range in age_list_pro:
                # print(age_range)
                # 一个选区下的一个区
                df_area = df1[(df1['区别'] == ctoswLite(area)) & (df1['性别'] == '总计')]
                data[age_range] = data[age_range] + df_area[age_list2(age_range)].sum().values.sum()
        print(data)

excel_class_1()

# list_ = ['七股区', '佳里区', '麻豆区', '官田区', '善化区', '大内区', '玉井区', '楠西区', '西港区', '安定区', '山上区', '左镇区', '南化区']
#
# for area in list_:
#     print(ctoswLite(area))
#     print(df1[df1['区别'] == ctoswLite(area)])