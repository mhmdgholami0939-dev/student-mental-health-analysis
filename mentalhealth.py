import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy import stats
df=pd.read_csv("Student Mental health.csv")
print("shape of data:",df.shape)
print(df.head())
print(df.isna().sum())
print(df.dtypes)
colmap = {
    "Choose your gender": "Gender",
    "Age": "Age",
    "Do you have Depression?": "depression",
    "Do you have Anxiety?": "anxiety",
    "Do you have Panic attack?": "Panicattack", 
}
df = df.rename(columns=colmap)
data=df.copy()
binary_map={'Yes':1,'No':0}
data['Depression']=data['depression'].map(binary_map)
data['Anxiety']=data['anxiety'].map(binary_map)
data['Panic attack']=data['Panicattack'].map(binary_map)
data['Gender']=data['Gender'].map({'Male': 0, 'Female': 1})
data = data.dropna(subset=["Age", "Gender", "depression", "anxiety", "Panicattack"])
corr_age_dep=stats.pointbiserialr(data['Age'], data['Depression'])
corr_age_anx=stats.pointbiserialr(data['Age'], data['Anxiety'])
corr_age_panic=stats.pointbiserialr(data['Age'], data['Panic attack'])
print("Correlation between Age and Depression:", corr_age_dep)
print("Correlation between Age and Anxiety:", corr_age_anx)
print("Correlation between Age and Panic attack:", corr_age_panic)
for col in ['Depression', 'Anxiety', 'Panic attack']:
    contingency = pd.crosstab(data['Gender'], data[col])
    chi2, p, dof, expected = chi2_contingency(contingency)
    print(f"\ Chi-square test: Gender {col}")
    print(f"Chi2 = {chi2:.3f}, p-value = {p:.4f}")