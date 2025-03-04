import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 设置支持中文的字体 Setting the fonts that support Chinese
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows 系统使用 "SimHei"（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 加载数据 Load data
data = pd.read_csv('heart_disease_risk_dataset_earlymed.csv')

# 计算相关性矩阵 Calculate the correlation matrix
correlation_matrix = data.corr()

# 绘制热力图 Heat mapping
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('症状与心脏病风险因素的相关性热力图 Heat map of correlation between symptoms and risk factors for heart disease')
plt.show()