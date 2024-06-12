from PIL import Image

# 打开彩色图像
image = Image.open("2_s.png")


# 转换为灰度图像
grayscale_image = image.convert("L")

# 保存黑白图像
grayscale_image.save("2_s1.png")