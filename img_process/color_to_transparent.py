import os

"""
获取图片左上角的像素点的rgb值
根据这个rgb来吧图片中同一颜色的区域全部设置为透明
"""

from PIL import Image

def get_pixel_color(image_path, x, y):
    # 打开图片
    img = Image.open(image_path)

    # 获取图片的像素数据
    data = img.getdata()

    # 获取指定像素点的颜色值
    pixel_color = img.getpixel((x, y))

    return pixel_color

# 例子：获取图片中左上角像素点的颜色值
# image_path = "彰化县第四选举区.png"
# x_coordinate = 0
# y_coordinate = 0
#
# color_value = get_pixel_color(image_path, x_coordinate, y_coordinate)
# print(color_value)

def add_alpha_mask(image_path, output_path, target_color):
    # 打开图片
    img = Image.open(image_path)

    # 将图片转为RGBA模式，以便添加透明度
    img = img.convert("RGBA")

    # 获取图片的像素数据
    data = img.getdata()

    # 新建一个列表，用于存储修改后的像素数据
    new_data = []

    # 定义目标颜色和透明度
    target_red, target_green, target_blue = target_color
    target_alpha = 0  # 0表示完全透明

    # 遍历每个像素
    for item in data:
        # 如果像素的RGB值与目标颜色相同，则将其改为目标颜色和透明度
        if item[0] == target_red and item[1] == target_green and item[2] == target_blue:
            new_data.append((target_red, target_green, target_blue, target_alpha))
        else:
            new_data.append(item)

    # 更新图片的像素数据
    img.putdata(new_data)

    # 保存修改后的图片
    img.save(output_path, "PNG")


add_alpha_mask("彰化县第四选举区.png", "彰化县第四选举区_v2.png", (255, 255, 255))
path1 = r"C:/Users/RZ/Pictures/立法委选举区域地图/big_area/"
path2 = r"C:/Users/RZ/Pictures/立法委选举区域地图/big_area_process/"
# 遍历输入文件夹中的所有文件
# for filename in os.listdir(path1):
#     # 检查文件是否为图片文件
#     if filename.endswith((".png", ".jpg", ".jpeg")):
#         # 构建输入和输出文件的完整路径
#         input_path = os.path.join(path1, filename)
#         output_path = os.path.join(path2, filename)
#
#         # 例子：将红色（255, 0, 0）变为透明
#         add_alpha_mask(input_path, output_path, (175, 221, 233))
