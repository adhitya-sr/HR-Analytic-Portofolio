"""
Project : HR Analytics Portfolio
File    : 01_data_understanding.py
Author  : Adhitya SR

Description:
This script performs an initial exploration of the HR dataset,
including dataset dimensions, column information, data types,
missing values, duplicate records, and descriptive statistics.
"""

import pandas as pd

# =================================
# LOAD DATASET
# =================================
df = pd.read_csv('hr_data_raw.csv')

# =================================
# DATASET OVERVIEW
# =================================
print("===== SHAPE =====")
print(df.shape)

print("\n===== COLUMNS =====")
print(df.columns)

print("\n===== HEAD =====")
print(df.head())

print("\n===== INFO =====")
df.info()

# =================================
# DATA TYPES
# =================================
print("\n===== DTYPES =====")
print(df.dtypes)

print("\n===== DESCRIBE =====")
print(df.describe(include='all'))

# =================================
# MISSING VALUES
# =================================
print("\n===== MISSING VALUE =====")
print(df.isnull().sum())

# =================================
# DUPLICATE RECORDS
# =================================
print("\n===== DUPLICATE VALUE =====")
print(df.duplicated().sum())

print("\n===== UNIQUE VALUES =====")
print(df.nunique())