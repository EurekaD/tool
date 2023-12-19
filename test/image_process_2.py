import cv2
import numpy as np

def apply_contour_to_image(image_path, output_path):
    # 读取图像
    img = cv2.imread(image_path)

    # 自适应阈值化，确保轮廓为白色
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
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

    # 创建一个具有透明通道的图像
    result = np.zeros_like(img, dtype=np.uint8)
    result[:, :, :3] = img
    result[:, :, 3] = mask

    # 保存结果
    cv2.imwrite(output_path, result)

# 例子：将轮廓应用于原图并将轮廓以外的部分设置为透明
apply_contour_to_image("test.png", "output_image_with_transparency.png")
