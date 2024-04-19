import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api-colombia.com/api/v1/Department"

response = requests.get(url)

if response.status_code != 200:
    print("Error obteniendo los datos", response)

data = response.json()
print(data)

colombia_df = pd.DataFrame(data)

print(colombia_df)
print(colombia_df.head()) # obtiene los primeros departamentos
print(colombia_df.shape)
print(colombia_df.columns)
print(colombia_df.describe())
print(colombia_df.info())

max_population = colombia_df.loc[colombia_df["population"].idxmax()]
print(max_population)

min_population = colombia_df.loc[colombia_df["population"].idxmin()]
print(min_population)

print(colombia_df.isna().any())

df_without_country = colombia_df.drop(columns="country", axis=1)
print(df_without_country)

df = colombia_df.sort_values(by=['surface'])
categories = colombia_df["name"]
values = df["surface"]

plt.barh(categories, values, color="skyblue")
plt.xlabel("Superficie")
plt.ylabel("Departamento")
plt.title("Superficies por Departamento")
plt.show()
