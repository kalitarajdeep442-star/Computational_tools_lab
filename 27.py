
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Mathematics': [78,85,67,90,73,81,69,94,76,88],
    'Physics': [72,88,70,92,75,79,68,90,74,85],
    'Chemistry': [75,82,65,88,78,83,72,92,79,86],
    'English': [80,84,72,91,76,80,70,95,77,89]
}

df = pd.DataFrame(data)
 
df.hist(figsize=(10,6), bins=5)
plt.tight_layout()
plt.show()
 
sns.pairplot(df)
plt.show() 

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Subject Correlation Heatmap")
plt.show()