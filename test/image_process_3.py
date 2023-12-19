import cv2
import numpy as np

def find_largest_connected_component(image_path, output_path):
    # 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 自适应阈值化
    binary_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # 反转二值化图像，确保轮廓为白色
    binary_img = 255 - binary_img

    # 连通区域分析
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_img)

    # 找到最大的连通区域
    max_label = 1  # 默认第一个连通区域
    max_area = stats[max_label, cv2.CC_STAT_AREA]

    for label in range(2, len(stats)):
        area = stats[label, cv2.CC_STAT_AREA]
        if area > max_area:
            max_label = label
            max_area = area

    # 创建一个只包含最大连通区域的掩码
    mask = np.zeros_like(binary_img)
    mask[labels == max_label] = 255

    # 在原图上绘制最大连通区域
    result = cv2.bitwise_and(img, img, mask=mask)

    # 保存结果
    cv2.imwrite(output_path, result)

# 例子：找到一张图像的最大连通区域并保存（使用自适应阈值）
find_largest_connected_component("test.png", "output_image_1.jpg")

