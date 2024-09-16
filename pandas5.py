import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()
