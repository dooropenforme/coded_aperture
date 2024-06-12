from PIL import Image
import numpy as np
from multiprocessing import Pool

# 打开文件
anticode = Image.open("anticode_257.png")
image = Image.open("coded_257.png")

# 创建新对象
width, height = image.size
new_image = Image.new("L", (width, height))
value = np.zeros((width, height))
def process_row(x):
    for y in range(height):
        # 历遍每一个image中的像素点
        pixel_value = image.getpixel((x, y))
        if pixel_value > 50:
            for x1 in range(width):
                for y1 in range(height):
                    x2 = x + (x1 - width // 2)
                    y2 = y + (y1 - height // 2)
                    # 判断是否在图像内
                    if 0 <= x2 < width and 0 <= y2 < height:
                        fpixel_value = anticode.getpixel((x1, y1))
                        if pixel_value > 150:
                            value[x2][y2] += 2 * (fpixel_value / 10)
                        else:
                            value[x2][y2] += fpixel_value / 10
    return value[x]

# 使用多进程
if __name__ == '__main__':
    with Pool() as p:
        results = p.map(process_row, range(width))

    for x in range(width):
        value[x] = results[x]

    min_val = np.min(value)
    max_val = np.max(value)
    value = np.round(value - min_val) / (max_val - min_val) * 250  # 归一化

    for x in range(width):
        for y in range(height):
            new_image.putpixel((x, y), int(value[x][y]))

    new_image.save("final33_257.png")

    # 绘制三维图
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    X, Y = np.meshgrid(np.arange(len(value[0])), np.arange(len(value)))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(X, Y, value, rstride=1, cstride=1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Value')
    ax.set_title(' value ')
    plt.show()