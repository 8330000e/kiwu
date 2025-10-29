import pandas as pd
import seaborn as sns
# import matplotlib.pyplot as plt

# titanic = sns.load_dataset('titanic')
# # print(titanic.info())
# # print(titanic.tail(3))
# print(titanic.query('age >= 70'))

# sns.scatterplot(x='age', y='fare', data=titanic)
# plt.show()

df = sns.load_dataset('penguins')
# print(df.info())
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df['body_mass_g'].describe())
print(df[df['bill_length_mm'] >= 55.0])


