# student-mental-health-analysis
 first Python data analysis project exploring student mental health using statistical tests.
Overview

This project explores how age and gender are related to students’ mental health — specifically depression, anxiety, and panic attacks.
The main goal was to see if younger or older students experience more mental health issues and if there are noticeable differences between male and female students.

I used this project to practice real-world data analysis with Python and to better understand how statistics can explain human behavior.

Objectives

Find out if age is related to depression, anxiety, or panic attacks.

Check whether gender makes a difference in these mental health conditions.

Learn how to perform statistical analysis using Python.

Tools & Libraries

Python

pandas, numpy – for data handling

scipy.stats – for correlation and chi-square tests

VS Code – for coding and testing

Process

Data Cleaning

Loaded the dataset and renamed some columns for easier use.

Replaced “Yes”/“No” with 1 and 0.

Encoded gender as Male = 0 and Female = 1.

Dropped rows with missing values.

Exploratory Analysis

Looked at the structure, data types, and missing values.

Checked column names and first few rows to understand the dataset.

Statistical Tests

Used Point-Biserial Correlation to see how age is related to depression, anxiety, and panic attacks.

Used Chi-Square Test to check if gender differences are statistically significant for each mental health variable.

Interpretation

Read the correlation values (r) and p-values to decide if relationships were strong or weak, significant or not.

Compared gender distributions across conditions.

Results Summary
Relationship	Interpretation
Age ↔ Depression	Negative correlation — younger students tend to report more depression
Age ↔ Anxiety	Negative correlation — younger students show slightly higher anxiety
Age ↔ Panic Attack	Negative correlation — panic attacks more common in younger students
Gender ↔ Depression	Significant difference — females report higher depression rates
Gender ↔ Anxiety	Not significant — both genders experience similar anxiety
Gender ↔ Panic Attack	Significant difference — females report more panic attacks
What I Learned

How to clean and prepare data for analysis using pandas.

How to apply basic statistical tests with scipy.stats.

How to interpret correlation and chi-square results.

How to describe results clearly without overcomplicating them.

This was my first time applying statistics to real human data, and it helped me understand how analysis can connect numbers with real emotions and experiences.
