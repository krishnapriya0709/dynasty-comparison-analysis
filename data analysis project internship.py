import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/krishnapriya/Documents/Internship Project/Chola_Pandya_Chera_Kingdoms_Data.csv")

print("First 5 rows of the dataset:")
print(df.head())

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary (Numerical Columns):")
print(df.describe())

print("\nNumber of Records per Kingdom:")
print(df['Kingdom'].value_counts())

print("\nTop 10 Most Frequent Rulers:")
print(df['Ruler'].value_counts().head(10))

print("\nFrequency of Capitals:")
print(df['Capital'].value_counts())

kingdom_group = df.groupby('Kingdom')[['Temples Built', 'Inscriptions Found', 'Trade Reach Score', 'Military Campaigns']].mean()
print("\nAverage Values by Kingdom:")
print(kingdom_group)

kingdom_group.plot(kind='bar', figsize=(10, 6))
plt.title('Comparison of Kingdoms')
plt.ylabel('Average Value')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

correlation = df[['Temples Built', 'Inscriptions Found', 'Trade Reach Score', 'Military Campaigns']].corr()
print("\nCorrelation Between Numerical Features:")
print(correlation)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Between Variables')
plt.tight_layout()
plt.show()

df.to_csv("/Users/krishnapriya/Documents/Internship Project/cleaned_data.csv", index=False)
kingdom_group.to_csv("/Users/krishnapriya/Documents/Internship Project/kingdom_comparison.csv")

print("\nCleaned data and comparison results saved successfully in 'Internship Project' folder.")
