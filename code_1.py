import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r'C:/Users/GSS\Desktop/Extra stuff/Task 1/income.csv')

Income = df.iloc[ 1:100, 1]
Age = df.iloc[ 1:100, 2]

plt.bar(Age, Income, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Graph of Income over Age')

plt.show()

plt.hist(Income, bins=40, color='skyblue', edgecolor='black')
plt.show()