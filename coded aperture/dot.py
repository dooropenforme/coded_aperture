from PIL import Image
import numpy as np
from multiprocessing import Pool

# 打开文件
anticode = Image.open("1_s2.png")
image = Image.open("coded_65.png")

# 创建新对象
width, height = image.size
new_image = Image.new("L", (width, height))
value = np.zeros((width, height))

for x in range(width):
    print(f"Processing pixel at ({x})")
    for y in range(height):

        a=0
        for x1 in range(width):
            for y1 in range(height):
                x2 = x + (x1 - width // 2)
                y2 = y + (y1 - height // 2)
                if 0 <= x2 < width and 0 <= y2 < height:
                    if image.getpixel((x1, y1))>0 and anticode.getpixel((x2, y2))>0:
                        a+=1
        if a>1450:
            value[x][y] = 255
            for x1 in range(width):
                for y1 in range(height):
                    x2 = x + (x1 - width // 2)
                    y2 = y + (y1 - height // 2)
                    if 0 <= x2 < width and 0 <= y2 < height and anticode.getpixel((x2, y2)) > 0:
                        pixel_value = image.getpixel((x1, y1))
                        new_value = pixel_value - 100
                        image.putpixel((x1, y1), new_value)
            image.save(f"cut_{x}_{y}.png")
for x in range(width):
    for y in range(height):
        new_image.putpixel((x, y), int(value[x][y]))#写入计算得到的值
        new_image.save("dot.png")
