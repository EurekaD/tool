from Tools.OpenccUtils import ctoswLite
import pandas as pd
import numpy as np
excel_path1 = r'C:\Users\RZ\OneDrive\桌面\台湾各地关于教育程度和年龄的人口数据表\彰化县.xlsx'
excel_path2 = r'C:\Users\RZ\OneDrive\桌面\立委专项数据\xm_voter_info.xlsx'

excel_file = pd.ExcelFile(excel_path1)
df1 = excel_file.parse(sheet_name='Sheet2')

df2 = pd.read_excel(excel_path2)

age_list_pro = ['20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65岁以上']
edu_list = ['博士', '硕士', '大学', '高中', '专科', '国中', '初职', '国小', '自修', '不识字']


# age_list = ['20 ~ 24 歲', '25 ~ 29 歲', '30 ~ 34 歲', '35 ~ 39 歲', '40 ~ 44 歲', '45 ~ 49 歲', '50 ~ 54 歲', '55 ~ 59 歲', '60 ~ 64 歲', '65 歲以上']
# age_list = ['20～24', '25～29', '30～34', '35～39', '40～44', '45～49', '50～54', '55～59', '60～64', '65歲以上']
age_list = ['20～24歲', '25～29歲', '30～34歲', '35～39歲', '40～44歲', '45～49歲', '50～54歲', '55～59歲', '60～64歲', '65歲以上']

# for index, row in df2.iterrows():
#     detail_info = str(row['detail_info']).split('，')


def edu(list_):
    list_area = []
    for area in list_:
        # print(area)
        df_area = df1[df1['area'] == ctoswLite(area)]
        list_age = []
        # print(df_area)
        # 选出此区的不同年龄
        for age in age_list:
            # print(age)
            df_age = df_area[(df_area['age'] == age) & (df_area['gender'] == '計')]

            list_edu_num = []
            # 选出每个学历
            for edu in edu_list:
                list_num = []
                if edu not in ['自修', '不识字']:
                    for i in range(1, 6):
                        edus = edu + str(i)
                        if edus in df_age.columns:
                            list_num.append(int(df_age[edus]))
                else:
                    if edu in df_age.columns:
                        list_num.append(int(df_age[edu]))
                edu_people_sum = sum(list_num)
                list_edu_num.append(edu_people_sum)
                # print(edu_people_sum)

            # 计算得到此区不同年龄的每个学历人数
            education_level_age = list_edu_num
            list_age.append(education_level_age)

        list_area.append(list_age)
    # print(list_area)
    # 把 list_area中的几个区域的 数据 加和 得到 一个选区的数据
    return list_area


def add_nested_lists(lists):
    # 初始化结果列表
    result = lists[0]
    len_lists = len(lists)

    for i in range(1, len_lists):
        for j, inner_list in enumerate(lists[i]):
            result[j] = [a + b for a, b in zip(result[j], inner_list)]
    return result


def sum_inner_lists(lists):
    # 使用列表推导式对每个最小的子列表进行加和
    result = [sum(inner_list) for inner_list in lists]
    return result


def process_dictionary(input_dict):
    # 遍历字典的每个子字典
    for key, inner_dict in input_dict.items():
        # 获取需要相加的键的值
        values_to_sum = [inner_dict.pop('初职', 0), inner_dict.pop('国小', 0),
                         inner_dict.pop('自修', 0), inner_dict.pop('不识字', 0)]

        # 将相加的值作为新键值对放入字典
        inner_dict['其他'] = sum(values_to_sum)

    return input_dict

# 台北市
# list_ = [['北投区', '士林区'],
# ['大同区', '士林区'],
# ['中山区', '松山区'],
# ['内湖区', '南港区'],
# ['万华区', '中正区'],
# ['大安区'],
# ['信义区', '松山区'],
# ['文山区', '中正区']]

# 台中市

# list_ = [['大甲区', '大安区', '外埔区', '清水区', '梧栖区'],
# ['沙鹿区', '龙井区', '大肚区', '乌日区', '雾峰区'],
# ['后里区', '神冈区', '大雅区', '潭子区'],
# ['西屯区', '南屯区'],
# ['北屯区', '北区'],
# ['中区', '西区', '东区', '南区'],
# ['太平区', '大里区'],
# ['丰原区', '石冈区', '新社区', '东势区', '和平区']]

# 基隆市
# list_ = [['桃源区', '那玛夏区', '甲仙区', '六龟区', '杉林区', '内门区', '旗山区', '美浓区', '茂林区', '阿莲区', '田寮区', '燕巢区', '大社区', '大树区'],
# ['茄萣区', '湖内区', '路竹区', '永安区', '冈山区', '弥陀区', '梓官区', '桥头区'],
# ['楠梓区', '左营区'],
# ['仁武区', '鸟松区', '大寮区', '林园区'],
# ['三民区', '苓雅区'],
# ['鼓山区', '盐埕区', '前金区', '新兴区'],
# ['凤山区'],
# ['旗津区', '前镇区', '小港区']]


# 彰化县
list_ = [['伸港乡', '线西乡', '和美镇', '鹿港镇', '福兴乡', '秀水乡'],
['彰化市', '花坛乡', '芬园乡'],
['芳苑乡', '二林镇', '埔盐乡', '溪湖镇', '埔心乡', '大城乡', '竹塘乡', '埤头乡', '北斗镇', '溪州乡'],
['大村乡', '员林市', '永靖乡', '社头乡', '田尾乡', '田中镇', '二水乡']]

for list1 in list_:
    print(list1)
    result = edu(list1)

    result2 = add_nested_lists(result)
    # print(result2)
    result2_process = []
    for list_ in result2:
        list_ = dict(list(zip(edu_list, list_)))
        result2_process.append(list_)
    result2_process = dict(list(zip(age_list_pro, result2_process)))

    print(process_dictionary(result2_process))

