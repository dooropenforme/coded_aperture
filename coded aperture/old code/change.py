from PIL import Image

# 打开灰度图像
image = Image.open("1_s1.png")

# 获取图像的宽度和高度
width, height = image.size

# 创建一个新的图像对象
new_image = Image.new("L", (width, height))

# 遍历每个像素,根据条件进行灰度值转换
for x in range(width):
    for y in range(height):
        pixel_value = image.getpixel((x, y))
        if pixel_value > 250:
            new_pixel_value = 200
        elif 100 <= pixel_value <= 250:
            new_pixel_value = 100
        else:
            new_pixel_value = 0
        new_image.putpixel((x, y), new_pixel_value)

# 保存转换后的图像
new_image.save("1_s2.png")