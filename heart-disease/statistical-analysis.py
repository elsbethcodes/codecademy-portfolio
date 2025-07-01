# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind # two sample T-test for independent groups
from scipy.stats import f_oneway # ANOVA test a.k.a. analysis of variance
from statsmodels.stats.multicomp import pairwise_tukeyhsd # pairwise Tukey test
from scipy.stats import chi2_contingency # Chi-square test

# load data & observe first rows
heart = pd.read_csv('heart_disease.csv')
print(heart.head())
# find column names
print(heart.columns)

# boxplot for visual comparison of data groups
sns.boxplot(x='heart_disease', y='thalach', data=heart)
plt.ylabel('maximum heart rate achieved during exercise')
plt.title('Maximum Heart Rate vs Presence of Heart Disease')
plt.show()
plt.clf()
# Conclusion: those with heart disease have a lower maximum heart rate on average than those without heart disease.

# create subgroups
thalach_hd = heart['thalach'][heart['heart_disease']=='presence']
thalach_no_hd = heart['thalach'][heart['heart_disease']=='absence']

# comparison of averages
mean_diff = np.mean(thalach_no_hd) - np.mean(thalach_hd)
median_diff = np.median(thalach_no_hd) - np.median(thalach_hd)
print(mean_diff)
print(median_diff)

# Two sample t-test to test the following hypotheses:
# Null: The average thalach for a person with heart disease is equal to the average thalach for a person without heart disease.
# Alternative: The average thalach for a person with heart disease is NOT equal to the average thalach for a person without heart disease.
tval, pval = ttest_ind(thalach_hd, thalach_no_hd)
print(pval)
if pval < 0.05:
  print('There is significant evidence that the average thalach for a person with heart disease is not equal to the average thalach for a person with heart disease.')
else:
  print('There is insignificant evidence that the average thalach for a person with heart disease is not equal to the average thalach for a person with heart disease.')

# boxplot for visual comparison of data groups
sns.boxplot(x='heart_disease', y='age', data=heart)
plt.title('Age vs Presence of Heart Disease')
plt.show()
plt.clf()
# Conclusion: Those with heart disease have a higher age on average than those who do not.

# create subgroups
age_hd = heart['age'][heart['heart_disease']=='presence']
age_no_hd = heart['age'][heart['heart_disease']=='absence']

# comparison of averages
mean_diff = np.mean(age_no_hd) - np.mean(age_hd)
median_diff = np.median(age_no_hd) - np.median(age_hd)
print(mean_diff)
print(median_diff)

# Two sample t-test to test the following hypotheses:
# Null Hypothesis: The average age for a person with heart disease is equal to the average age for a person without heart disease.
# Alternative Hypothesis: The average age for a person with heart disease is NOT equal to the average age for a person without heart disease.
tval, pval = ttest_ind(age_hd, age_no_hd)
print(pval)
if pval < 0.05:
  print('There is significant evidence that the average age for a person with heart disease is not equal to the average age for a person with heart disease.')
else:
  print('There is insignificant evidence that the average age for a person with heart disease is not equal to the average age for a person with heart disease.')

sns.boxplot(x='cp', y='thalach', data=heart)
plt.title('Maximum Heart Rate vs Chest Pain Symptoms')
plt.xlabel('chest pain type')
plt.ylabel('maximum heart rate achieved during exercise')
plt.show()
plt.clf()
# conclusion: people with the asymptomatic case of heart disease have a lower maximum heart rate on average.

# create subgroups
thalach_typical = heart['thalach'][heart['cp']=='typical angina']
thalach_asymptom = heart['thalach'][heart['cp']=='asymptomatic']
thalach_nonangin = heart['thalach'][heart['cp']=='non-anginal pain']
thalach_atypical = heart['thalach'][heart['cp']=='atypical angina']

# ANOVA test to compare two or more means (type 1 error limited to 5%)
# Null Hypothesis: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people all have the same average thalach.
# Alternative Hypothesis: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people do not all have the same average thalach.
fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print(pval)
if pval < 0.05:
  print('There is at least one pair of chest pain categories for which people have statistically significant different maximum heart rates.')
else:
  print('No pair of chest pain categories has statistically significant different maximum heart rates.')

# Tukey-test - which pairs are significantly different
result = pairwise_tukeyhsd(endog = heart['thalach'], groups = heart['cp'], alpha=0.05)
print(result)

# prepare contingency table for chi-square test
Xtab = pd.crosstab(heart['cp'], heart['heart_disease']) 
print(Xtab)

# chi-square can compare two categorical variables, given a contingency table
chi2, pval, dof, exp = chi2_contingency(Xtab)
print(pval)
if pval < 0.05:
  print('There is statistically significant evidence that there is an association between chest pain type and whether or not someone is diagnosed with heart disease.')
else:
  print('There is not statistically significant evidence that there is an association between chest pain type and whether or not someone is diagnosed with heart disease.')
