import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Naman  Maheshwari\OneDrive\Desktop\Unicorn_Companies.csv")

#Converting Billions and Millions to dollar for simpiler use
def convert_to_billion(x):
    x = str(x).replace('$', '')
    if 'B' in x:
        return float(x.replace('B', ''))
    elif 'M' in x:
        return float(x.replace('M', '')) / 1000
    else:
        return None

df['Valuation ($B)'] = df['Valuation'].apply(convert_to_billion)
df['Funding ($B)'] = df['Funding'].apply(convert_to_billion)
df['Date Joined'] = pd.to_datetime(df['Date Joined'], errors='coerce')

#Basic Overview
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("Missing Values:\n", df.isnull().sum())
print("\nFirst 5 rows:\n", df.head())

#Summary Statistics
print("\nValuation Stats ($B):\n", df['Valuation ($B)'].describe())
print("\nFunding Stats ($B):\n", df['Funding ($B)'].describe())
print("\nIndustry Distribution:\n", df['Industry'].value_counts())
print("\nCountry Distribution:\n", df['Country'].value_counts())
print("\nContinent Distribution:\n", df['Continent'].value_counts())



#Top 10 Companies by Valuation 
plt.figure(figsize=(12, 6))
top_valuation = df.sort_values(by='Valuation ($B)', ascending=False).head(10)
sns.barplot(data=top_valuation, x='Valuation ($B)', y='Company', hue='Company', palette='coolwarm', legend=False)
plt.title('Top 10 Unicorns by Valuation')
plt.xlabel('Valuation ($B)')
plt.ylabel('Company')
plt.tight_layout()
plt.show()

#Top 10 Industries by Total Funding
plt.figure(figsize=(12, 6))
industry_funding = df.groupby('Industry')['Funding ($B)'].sum().sort_values(ascending=False).head(10).reset_index()
sns.barplot(data=industry_funding, x='Funding ($B)', y='Industry', hue='Industry', palette='magma', legend=False)
plt.title('Top 10 Industries by Total Funding')
plt.xlabel('Total Funding ($B)')
plt.ylabel('Industry')
plt.tight_layout()
plt.show()

#Companies by Continent
plt.figure(figsize=(8, 5))
sns.countplot(x='Continent', data=df)
plt.title("Companies by Continent")
plt.xlabel("Continent")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

#Valuation vs Year Founded 
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Year Founded', y='Valuation ($B)', hue='Continent')
plt.title("Valuation by Year Founded")
plt.xlabel("Year Founded")
plt.ylabel("Valuation ($B)")
plt.tight_layout()
plt.show()
