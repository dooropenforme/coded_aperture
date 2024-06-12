from PIL import Image

# 读取PNG图像
image = Image.open("1_b.png")

# 上下和左右同时反转图像
flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT)

# 保存反转后的图像
flipped_image.save("1_ba.png")