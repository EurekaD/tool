from Tools.OpenccUtils import ctoswLite
import pandas as pd
import numpy as np
excel_path1 = r'C:\Users\RZ\OneDrive\桌面\台湾各地关于教育程度和年龄的人口数据表\台南市_.xlsx'

excel_file = pd.ExcelFile(excel_path1)
df1 = excel_file.parse(sheet_name='Sheet1')

edu_list = ['博士', '硕士', '大学', '高中', '专科', '国中', '初职', '国小', '自修', '不识字']


def sum_inner_lists(lists):
    # 使用列表推导式对每个最小的子列表进行加和
    result = [sum(inner_list) for inner_list in lists]
    return result


def add_nested_lists(lists):
    # 初始化结果列表
    sum_result = lists[0]
    len_lists = len(lists)

    for i in range(1, len_lists):
        add_list = lists[i]
        sum_result = [a + b for a, b in zip(sum_result, add_list)]
    return sum_result


def process_dictionary(input_dict):
    # 遍历字典的每个子字典
    for key, inner_dict in input_dict.items():
        # 获取需要相加的键的值
        values_to_sum = [inner_dict.pop('初职', 0), inner_dict.pop('国小', 0),
                         inner_dict.pop('自修', 0), inner_dict.pop('不识字', 0)]

        # 将相加的值作为新键值对放入字典
        inner_dict['其他'] = sum(values_to_sum)

    return input_dict


def edu(list_):
    list_area = []
    for area in list_:
        # print(ctoswLite(area))
        df_area = df1[df1['area'] == ctoswLite(area)]
        # print(df_area)
        list_edu_num = []
        # 选出每个学历
        for edu in edu_list:
            list_num = []
            if edu not in ['自修', '不识字']:
                for i in range(1, 6):
                    edus = edu + str(i)
                    if edus in df_area.columns:
                        list_num.append(int(df_area[edus]))
            else:
                if edu in df_area.columns:
                    list_num.append(int(df_area[edu]))
            edu_people_sum = sum(list_num)
            list_edu_num.append(edu_people_sum)

        # 计算得到此区不同年龄的每个学历人数
        # print(list_edu_num)
        list_area.append(list_edu_num)
    list_area = add_nested_lists(list_area)
    list_area = dict(list(zip(edu_list, list_area)))
    values_to_sum = [list_area.pop('初职', 0), list_area.pop('国小', 0),
                     list_area.pop('自修', 0), list_area.pop('不识字', 0)]

    # 将相加的值作为新键值对放入字典
    list_area['其他'] = sum(values_to_sum)
    result = {"全部":list_area}
    print(result)
    # 把 list_area中的几个区域的 数据 加和 得到 一个选区的数据
    return result


list_ = [['后壁区', '白河区', '北门区', '学甲区', '盐水区', '新营区', '柳营区', '东山区', '将军区', '下营区', '六甲区'],
['七股区', '佳里区', '麻豆区', '官田区', '善化区', '大内区', '玉井区', '楠西区', '西港区', '安定区', '山上区', '左镇区', '南化区'],
['安南区', '北区'],
['永康区', '新市区', '新化区'],
['安平区', '中西区', '南区', '东区'],
['仁德区', '归仁区', '关庙区', '龙崎区', '东区']]

for list1 in list_:
    print(list1)
    result = edu(list1)


