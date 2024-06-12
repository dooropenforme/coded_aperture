from PIL import Image

# 打开灰度图像
image = Image.open("1_b.png")

# 反转灰度图像
inverted_image = Image.eval(image, lambda x: 255 - x)

# 保存反转后的灰度图像
inverted_image.save("1_b1.png")