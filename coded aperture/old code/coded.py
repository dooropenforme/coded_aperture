from PIL import Image
import numpy as np

anticode = Image.open("1_s2.png")
image=Image.open("outpu22t.png")

width, height = image.size
new_image = Image.new("L", (width, height))
value=np.zeros((width, height))
for x in range(width):
    for y in range(height):
        #历遍每一个image中的像素点
        pixel_value = image.getpixel((x, y))#判断是否存在值
        if pixel_value > 50:
            for x1 in range(width):
                for y1 in range(height):
                    x2 = x + (x1 - 35)
                    y2 = y + (y1 - 35)
                    if 0 <= x2 < 65 and 0 <= y2 < 65:
                        fpixel_value = anticode.getpixel((x1, y1))
                        if pixel_value > 150:
                            value[x2][y2] += 2 * (fpixel_value)
                        else:
                            value[x2][y2] += fpixel_value
    print(f"Processing pixel at ({x})")
print(value)
value=value
for x in range(width):
    for y in range(height):
        new_image.putpixel((x, y), int(value[x][y]))
new_image.save("final22.png")