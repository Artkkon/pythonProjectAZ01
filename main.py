import pandas as pd

data = pd.read_csv("recipe_data.csv")
df = pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.describe())

data = pd.read_csv("dz.csv")
df = pd.DataFrame(data)
group = df.groupby('City')['Salary'].mean()
print(group)