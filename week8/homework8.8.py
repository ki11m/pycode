import seaborn as sns
import matplotlib.pyplot as plt

# 加载示例数据集
tips = sns.load_dataset("tips")

# 绘制散点图
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Scatter Plot of Total Bill vs Tip")
plt.show()

# 绘制直方图
sns.histplot(tips["total_bill"], bins=20, kde=True)
plt.title("Histogram of Total Bill")
plt.show()

# 绘制箱线图
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Box Plot of Total Bill by Day")
plt.show()
