from PIL import Image


def count_pixels_above_50(image_path):
    """
    统计图像中灰度值大于 50 的像素点数量。

    参数:
    image_path (str): 图像文件路径

    返回:
    int: 灰度值大于 50 的像素点数量
    """
    image = Image.open(image_path)
    width, height = image.size

    count = 0
    for x in range(width):
        for y in range(height):
            pixel_value = image.getpixel((x, y))
            if pixel_value > 50:
                count += 1

    return count


# 示例使用
image_path = "1_s2.png"
num_pixels_above_50 = count_pixels_above_50(image_path)
print(f"图像中灰度值大于 50 的像素点数量: {num_pixels_above_50}")