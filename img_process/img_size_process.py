from PIL import Image
import cv2

def resize_image(input_path, output_path, new_size):
    original_image = cv2.imread(input_path, 1)
    # cv2.imshow('original', original_image)
    width, height = original_image.size

    print(f"{width}:{height}")

    # 计算新的尺寸，保持纵横比
    ratio = min(new_size / width, new_size / height)
    new_width = int(width * ratio)
    new_height = int(height * ratio)

    print(f"{new_width}:{new_height}")

    img_resize = cv2.resize(original_image, (new_height, new_width), interpolation=cv2.INTER_AREA)

    cv2.imshow('test', img_resize)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 例子
input_image_path = "彰化县第四选举区_v2.png"
output_image_path = "output.jpg"
new_size = 300

resize_image(input_image_path, output_image_path, new_size)
