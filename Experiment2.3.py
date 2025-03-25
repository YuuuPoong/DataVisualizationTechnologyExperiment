import matplotlib.pyplot as plt
import matplotlib

# 设置支持中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 适用于Windows
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 比赛名称
matches = ['1-G1', '1-G2', '1-G3', '1-G4', '1-G5',
           '2-G1', '2-G2', '2-G3', '2-G4', '2-G5',
           '3-G1', '3-G2', '3-G3', '3-G4', '3-G5',
           '总决赛-G1', '总决赛-G2', '总决赛-G3', '总决赛-G4', '总决赛-G5', '总决赛-G6']

# 比赛得分
scores = [23, 10, 38, 30, 36, 20, 28, 36, 16, 29, 15, 26, 30, 26, 38, 34, 33, 25, 28, 40, 28]

# 绘制折线图
plt.figure(figsize=(12, 6))
plt.plot(matches, scores, marker='o', linestyle='-', color='b')

# 添加数据标签
for i, score in enumerate(scores):
    plt.text(i, score + 1, str(score), ha='center', fontsize=10)

# 设置标题和标签
plt.title("比赛得分图")
plt.xlabel("比赛")
plt.ylabel("得分")
plt.xticks(rotation=45)  # 旋转x轴刻度以防重叠
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.show()