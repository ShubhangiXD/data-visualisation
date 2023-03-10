import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
 
 
# reading the database
data = pd.read_csv("src/tips.csv")
 
sns.histplot(x='total_bill', data=data, kde=True, hue='sex')
 
plt.show()