import cv2
import numpy as np

def binary_contour(image_path, output_path, lower_black, upper_black):
    # 读取图片
    img = cv2.imread(image_path)

    # 将图片转换为HSV颜色空间
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 定义黑色的颜色范围
    lower_black = np.array(lower_black, dtype=np.uint8)
    upper_black = np.array(upper_black, dtype=np.uint8)

    # 创建黑色的掩码
    mask_black = cv2.inRange(hsv, lower_black, upper_black)

    # 对原始图片进行二值化处理
    _, thresh = cv2.threshold(mask_black, 1, 255, cv2.THRESH_BINARY)

    # 寻找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 在原图上绘制轮廓
    result = img.copy()
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

    # 保存结果
    cv2.imwrite(output_path, result)

# 例子：将图片的黑色和其他颜色区分开，并形成二值化的轮廓
binary_contour("test.png", "output_image.png", [0, 0, 0], [10, 10, 10])
