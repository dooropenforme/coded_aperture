from PIL import Image
import numpy as np

anticode = Image.open("1_ba.png")
image=Image.open("2_b.png")

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
                    x2 = x + (x1 - 63)
                    y2 = y + (y1 - 63)
                    if 0 <= x2 < 129 and 0 <= y2 < 129:
                        fpixel_value = anticode.getpixel((x1, y1))
                        if pixel_value > 150:
                            value[x2][y2] += 2 * (fpixel_value / 10)
                        else:
                            value[x2][y2] += fpixel_value / 10
print(value)
value=value/400
for x in range(width):
    for y in range(height):
        new_image.putpixel((x, y), int(value[x][y]))
new_image.save("final.png")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 创建网格坐标
X, Y = np.meshgrid(np.arange(len(value[0])), np.arange(len(value)))

# 绘制三维图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, value, rstride=1, cstride=1)

# 设置坐标轴标签和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Value')
ax.set_title(' value ')

# 显示图表
plt.show()
