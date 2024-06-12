from PIL import Image
#这是进行图像处理的整合版，适用于得到的像图像
# 打开一张图片
img = Image.open('2.png')

# 对图像进行处理，比如调整大小
resized_img = img.resize((1024, 1024))
img = resized_img.convert("L")
width, height = img.size

# 创建一个新的图像对象
new_image = Image.new("L", (width, height))

# 遍历每个像素,根据条件进行灰度值转换
for x in range(width):
    for y in range(height):
        pixel_value = img.getpixel((x, y))
        if pixel_value > 200:
            new_pixel_value = 200
        elif 100 <= pixel_value <= 200:
            new_pixel_value = 100
        else:
            new_pixel_value = 0
        new_image.putpixel((x, y), new_pixel_value)
# 保存处理后的图像
new_image.save('2_b.png')