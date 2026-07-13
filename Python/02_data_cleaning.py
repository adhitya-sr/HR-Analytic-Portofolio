"""
Project : HR Analytics Portfolio
File    : 02_data_cleaning.py
Author  : Adhitya SR

Description:
This script performs data cleaning, including duplicate removal,
missing value handling, typo correction, and data type conversion.
"""
import pandas as pd

# =================================
# LOAD DATASET
# =================================
df = pd.read_csv('hr_data_raw.csv')

# =================================
# REMOVE DUPLICATE RECORDS
# =================================
df_clean = df.drop_duplicates()
print(df_clean)

# =================================
# HANDLE MISSING VALUES
# =================================
print('\n===== MISSING PERFORMANCE SCORE =====')
performance_mean = round(df_clean['Performance Score'].mean(),2)
df_clean['Performance Score']=df_clean['Performance Score'].fillna(performance_mean)
# Missing values pada Performance Score diisi menggunakan nilai rata-rata
# untuk mempertahankan jumlah observasi dan memudahkan analisis statistik.
# Dampaknya, distribusi data dapat menunjukkan peningkatan frekuensi
# pada nilai hasil imputasi.

print('\n===== MISSING ATTENDANCE RATE (%) =====')
attendance_mean = round(df_clean['Attendance Rate (%)'].mean(),2)
df_clean['Attendance Rate (%)']=df_clean['Attendance Rate (%)'].fillna(attendance_mean)
# Missing values pada Attendance Rate diisi menggunakan nilai rata-rata
# untuk mempertahankan jumlah observasi dan memudahkan analisis statistik.
# Dampaknya, distribusi data dapat menunjukkan peningkatan frekuensi
# pada nilai hasil imputasi.

# =================================
# CORRECT INCONSISTENT VALUES
# =================================
print('\n===== INCONSISTENT VALUES =====')
df_clean['Department'] = df_clean['Department'].replace('Operatons','Operations')
df_clean['Region'] = df_clean['Region'].replace('Jakrta','Jakarta')

# =================================
# CONVERT DATA TYPES
# =================================
print('\n===== DATE TYPE =====')
df_clean['Resignation Date'] = pd.to_datetime(df_clean['Resignation Date'])
df_clean['Hire Date'] = pd.to_datetime(df_clean['Hire Date'])

# =================================
# DATA VALIDATION
# =================================
print('\n===== DATASET INFO =====')
df_clean.info()
print('============================')
print(df_clean.dtypes)

# =================================
# EXPORT CLEAN DATASET
# =================================
df_clean.to_csv('hr_data_cleaning.csv',index=False)