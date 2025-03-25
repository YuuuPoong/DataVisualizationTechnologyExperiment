import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置支持中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 适用于Windows
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 生成数据
x = np.linspace(-np.pi, np.pi, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(x, sin_y, color='b', linewidth=1.0, label='正弦')
plt.plot(x, cos_y, color='r', linewidth=1.0, alpha=0.5, label='余弦')

# 设置刻度
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ['-π', '-π/2', '0', 'π/2', 'π'])
plt.yticks([-1, -0.5, 0, 0.5, 1])

# 添加图例和标题
plt.legend()
plt.title("正余弦图像")

# 添加注释
plt.annotate('最小值', xy=(-np.pi/2, np.sin(-np.pi/2)), xytext=(-2, -0.75),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.text(3.1, 0.1, 'y=sin(x)', bbox=dict(facecolor='lightgray', alpha=0.5))

# 显示网格
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图像
plt.show()