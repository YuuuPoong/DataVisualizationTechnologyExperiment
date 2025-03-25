import matplotlib.pyplot as plt
import matplotlib

# 设置支持中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 适用于Windows
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据
quarters = ["第1季度", "第2季度", "第3季度", "第4季度"]
product_A = [2144, 4671, 7674, 6666]
product_B = [853, 1214, 2414, 4409]
product_C = [153, 183, 292, 680]

# 绘制折线图
plt.figure(figsize=(8, 6))
plt.plot(quarters, product_A, marker='o', linestyle='-', color='b', label='产品A')
plt.plot(quarters, product_B, marker='s', linestyle='--', color='g', label='产品B')
plt.plot(quarters, product_C, marker='^', linestyle=':', color='r', label='产品C')

# 添加标题和标签
plt.title("不同产品各季度销售额折线图")
plt.xlabel("季度")
plt.ylabel("销售额（万元）")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.show()