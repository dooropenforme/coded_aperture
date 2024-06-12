from PIL import Image

# 打开文件
image = Image.open("1_b.png")

# 同时翻转图像的水平和垂直方向
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)

# 保存翻转后的图像
flipped_image.save("f1_b.png")