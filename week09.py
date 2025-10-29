import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
# print(titanic.info())
# print(titanic.tail(3))
print(titanic.query('age >= 70'))

sns.scatterplot(x='age', y='fare', data=titanic)
plt.show()
