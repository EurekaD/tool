import cv2
import numpy as np




def overlay_contours_on_original(image_path, output_path):
    # 读取图片，包括透明通道
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # 检查图像是否成功读取
    if img is None:
        print(f"Error: Unable to read the image at {image_path}")
        return

    # 获取透明通道
    alpha_channel = img[:, :, 3]

    # 寻找轮廓
    contours, _ = cv2.findContours(alpha_channel, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大轮廓
    largest_contour = max(contours, key=cv2.contourArea)

    # 创建一个黑色背景，直接使用原图的形状
    transparent_background = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

    # 在黑色背景上绘制轮廓内的白色区域
    cv2.drawContours(transparent_background, [largest_contour], 0, (255), thickness=-1)


    # 将黑色背景中轮廓内的值改为255（不透明）
    img[:, :, 3] = np.where(transparent_background == 255, 255, img[:, :, 3])

    # 保存结果
    cv2.imwrite(output_path, img)

# 例子：将透明层直接覆盖到原图上并保存结果
overlay_contours_on_original("test.png", "output_result.png")
