"""
Project : HR Analytics Portfolio
File    : 03_exploratory_data_analysis.py
Author  : Adhitya SR

Description:
This script performs exploratory data analysis (EDA)
to understand workforce characteristics, employee
demographics, compensation, performance,
attendance, and attrition.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =================================
# LOAD DATASET
# =================================
df = pd.read_csv('hr_data_cleaning.csv')

# =================================
# WORKFORCE OVERVIEW
# =================================
print('===== Total Employee =====')
total_employee = df['Employee ID'].count()
print(f'Total`s Employee : {total_employee}')

print('===== Employee by Department =====')
department_employee = pd.pivot_table(df,
                      values='Employee ID',
                      index='Department',
                      aggfunc='count')
print(department_employee)
sns.countplot(data=df,
              x='Department')
plt.title('Employee by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print('===== Employee by Region =====')
region_employee = pd.pivot_table(df,
                  values='Employee ID',
                  index='Region',
                  aggfunc='count')
print(region_employee)
sns.countplot(data=df,
              x='Region')
plt.title('Employee by Region')
plt.tight_layout()
plt.show()

print('===== Employee by Gender =====')
gender_employee = pd.pivot_table(df,
                  values='Employee ID',
                  index='Gender',
                  aggfunc='count')
print(gender_employee)
gender_employee.plot(kind='pie',
                     subplots=True,
                     autopct='%1.1f%%',
                     ylabel='',
                     startangle=90)
plt.title('Employee by Gender')
plt.tight_layout()
plt.show()


# =================================
# EMPLOYEE DEMOGRAPHICS
# =================================
print('===== Age Statistics =====')
print(df['Age'].describe())

print('===== Age Distribution =====')
sns.histplot(data=df,
             x='Age',
             bins=20,
             kde=True)
plt.title('Age Distribution')
plt.tight_layout()
plt.show()

print('===== Average Age by Department =====')
department_age = (df.groupby('Department')['Age']
                    .mean()
                    .sort_values(ascending=False)
                    .round(2))
print(department_age)
sns.barplot(data=df,
            x='Department',
            y='Age',
            estimator='mean')
plt.title('Average Age by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
sns.boxplot(data=df,
            y='Age')
plt.title('Range of Employee`s Age')
plt.tight_layout()
plt.show()


# =================================
# COMPENSATION ANALYSIS
# =================================
print('===== Salary Statistic =====')
print(df['Monthly Salary'].describe())

print('===== Salary Distribution =====')
sns.histplot(df,
             x='Monthly Salary',
             bins=20,
             kde=True)
plt.title('Monthly Salary Distribution')
plt.tight_layout()
plt.show()

print('===== Salary Range =====')
sns.boxplot(df,
            y='Monthly Salary')
plt.title('Range of Monthly Salary')
plt.tight_layout()
plt.show()

print('===== Average Monthly Salary =====')
average_salary = round(df['Monthly Salary'].mean(),2)
print(f'Average monthly salary : Rp{average_salary:,.2f}')

print('===== Monthly Salary by Department =====')
department_salary = (df.groupby('Department')['Monthly Salary']
                     .mean()
                     .sort_values(ascending=False)
                     .round(2))
print(department_salary)
sns.barplot(data=df,
            x='Department',
            y='Monthly Salary',
            order=department_salary.index)
plt.title('Average Monthly Salary by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print('===== Bonus Statistic =====')
print(df['Bonus'].describe())

print('===== Bonus Distribution =====')
sns.histplot(df,
             x='Bonus',
             bins=20,
             kde=True)
plt.title('Bonus Distribution')
plt.tight_layout()
plt.show()

print('===== Bonus Range =====')
sns.boxplot(df,
            y='Bonus')
plt.title('Range of Bonus')
plt.tight_layout()
plt.show()

print('===== Average Bonus =====')
average_bonus = round(df['Bonus'].mean(),2)
print(f'Average bonus : Rp{average_bonus:,.2f}')

print('===== Bonus by Department =====')
department_bonus = (df.groupby('Department')['Bonus']
                    .mean()
                    .sort_values(ascending=False)
                    .round(2))
print(department_bonus)
sns.barplot(data=df,
            x='Department',
            y='Bonus',
            order=department_bonus.index)
plt.title('Average Bonus by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =================================
# PERFORMANCE ANALYSIS
# =================================
print('===== Performance Statistics =====')
print(df['Performance Score'].describe())

print('===== Performance Distribution =====')
sns.histplot(df,
             x='Performance Score',
             bins=10,
             kde=True)
plt.title('Performance Score Distribution')
plt.tight_layout()
plt.show()

print('===== Performance Range =====')
sns.boxplot(df,
            y='Performance Score')
plt.title('Range of Performance Score')
plt.tight_layout()
plt.show()

print('===== Average Performance Score =====')
average_performance = round(df['Performance Score'].mean(),2)
print(f'Average Performance Score : {average_performance:,.2f}')

print('===== Performance Score by Department =====')
department_performance = (df.groupby('Department')['Performance Score']
                        .mean()
                        .sort_values()
                        .round(2))
print(department_performance)
sns.barplot(data=df,
            x='Department',
            y='Performance Score',
            order=department_performance.index)
plt.title('Performance Score by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =================================
# ATTENDANCE ANALYSIS
# =================================
print('===== Attendance Statistics =====')
print(df['Attendance Rate (%)'].describe())

print('===== Attendance Distribution =====')
sns.histplot(data=df,
             x='Attendance Rate (%)',
             bins=20,
             kde=True)
plt.title('Attendance Rate Distribution')
plt.tight_layout()
plt.show()

print('===== Attendance Range =====')
sns.boxplot(data=df,
            y='Attendance Rate (%)')
plt.title('Range of Attendance Rate')
plt.tight_layout()
plt.show()

print('===== Average Attendance Rate =====')
average_attendance = round(df['Attendance Rate (%)'].mean(),2)
print(f'Average Attendance Rate : {average_attendance:,.2f}%')

print('===== Average Attendance Rate by Department =====')
department_attendance = (df.groupby('Department')['Attendance Rate (%)']
                         .mean()
                         .sort_values()
                         .round(2))
print(department_attendance)
sns.barplot(data=df,
            x='Department',
            y='Attendance Rate (%)',
            order=department_attendance.index)
plt.title('Attendance Rate (%) by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =================================
# SATISFACTION ANALYSIS
# =================================
print('===== Satisfaction Statistics =====')
print(df['Job Satisfaction'].describe())

print('===== Satisfaction Distribution =====')
sns.countplot(
    data=df,
    x='Job Satisfaction')

plt.title('Job Satisfaction Distribution')
plt.xlabel('Job Satisfaction')
plt.ylabel('Employee Count')

plt.tight_layout()
plt.show()

print('===== Satisfaction Range =====')
sns.boxplot(data=df,
            y='Job Satisfaction')
plt.title('Range of Job Satisfaction')
plt.tight_layout()
plt.show()

print('===== Average Job Satisfaction =====')
average_satisfaction = df['Job Satisfaction'].mean()
print(f'Average Job Satisfaction : {average_satisfaction:,.2f}')

print('===== Average Job Satisfaction by Department =====')
department_satisfaction = (df.groupby('Department')['Job Satisfaction']
                           .mean()
                           .sort_values()
                           .round(2))
print(department_satisfaction)
sns.barplot(data=df,
            x='Department',
            y='Job Satisfaction',
            order=department_satisfaction.index)
plt.title('Job Satisfaction by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =================================
# ATTRITION ANALYSIS
# =================================
print('===== Attrition Count =====')
def attrition_calculate(df):
      df['Attrition Rate'] = round(
            df['Resigned']*100/
            (df['Resigned']+df['Active'])
            ,2)
      return df

print('===== Employment Status =====')
employee_status = (df.groupby('Employment Status')
                  ['Employee ID'].count())
print(employee_status)
employee_status.plot(kind='pie',
        y='Employment Status',
        autopct='%1.1f%%',
        startangle=90)
plt.title('Status Composition')
plt.tight_layout()
plt.show()

print('===== Attrition Rate =====')
total_employee = len(df)
resign = (df[df['Employment Status']=='Resigned']
          .shape[0])
attrition_rate = round(resign*100/total_employee,2)
print(f'Total Employee  : {total_employee}'
      f'\nResign Employee : {resign}'
      f'\nAttrition Rate  : {attrition_rate}%')

print('===== Attrition Rate by Department =====')
department_attrition = pd.pivot_table(df,
                                      values='Employee ID',
                                      index='Department',
                                      columns='Employment Status',
                                      aggfunc='count')
department_attrition = attrition_calculate(department_attrition)
print(department_attrition.sort_values(by='Attrition Rate'))
department_attrition.plot(kind='bar',
                          y='Attrition Rate')
plt.title('Attrition Rate by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print('===== Attrition Rate by Gender =====')
gender_attrition = pd.pivot_table(df,
                                  values='Employee ID',
                                  columns='Employment Status',
                                  index='Gender',
                                  aggfunc='count')
gender_attrition = attrition_calculate(gender_attrition)
print(gender_attrition.sort_values(by='Attrition Rate'))
gender_attrition.plot(kind='bar',
                      y='Attrition Rate')
plt.title('Attrition Rate by Gender')
plt.tight_layout()
plt.show()

print('===== Attrition Rate by Tenure =====')
def kategori(tenure):
      if tenure < 1:
            return '<1'
      elif tenure <3:
            return '1-3'
      elif tenure <5:
            return '3-5'
      else:
            return '>5'
df['Tenure Category'] = (df['Years at Company']
                        .apply(kategori))
tenure_attrition = pd.pivot_table(data=df,
                                  values='Employee ID',
                                  columns='Employment Status',
                                  index='Tenure Category',
                                  aggfunc='count')
tenure_attrition = attrition_calculate(tenure_attrition)
print(tenure_attrition.sort_values(by='Attrition Rate'))
tenure_attrition.plot(kind='bar',
                      y='Attrition Rate')
plt.title('Attrition Rate by Tenure')
plt.tight_layout()
plt.show()

print('===== Attrition Rate by Age =====')
def kategori(age):
      if age <30:
            return '21-29'
      elif age <40:
            return '30-39'
      elif age <50:
            return '40-49'
      else:
            return "+50"
df['Age Category'] = df['Age'].apply(kategori)
age_attrition = pd.pivot_table(data=df,
                               values='Employee ID',
                               columns='Employment Status',
                               index='Age Category',
                               aggfunc='count')
age_attrition = attrition_calculate(age_attrition)
print(age_attrition)
age_attrition.plot(kind='bar',
                   y='Attrition Rate')
plt.title('Attrition Rate by Age')
plt.tight_layout()
plt.show()

# =================================
# CORRELATION ANALYSIS
# =================================
print('===== Variable Correlation =====')
kolom = [
    'Age',
    'Monthly Salary',
    'Bonus',
    'Performance Score',
    'Overtime Hours',
    'Attendance Rate (%)',
    'Years at Company',
    'Job Satisfaction']
corr=df[kolom].corr().round(2)
sns.heatmap(corr,
            annot=True,
            cmap='coolwarm',
            vmin=-1,
            vmax=1,)
plt.title('Variable Correlation')
plt.tight_layout()
plt.show()

sns.scatterplot(data=df,
                x='Monthly Salary',
                y='Performance Score')
plt.title('Correlation of Monthly Salary and Performance Score')
plt.tight_layout()
plt.show()

sns.scatterplot(data=df,
                x='Years at Company',
                y='Monthly Salary')
plt.title('Correlation of Years at Company and Monthly Salary')
plt.tight_layout()
plt.show()

sns.scatterplot(data=df,
                x='Overtime Hours',
                y='Job Satisfaction')
plt.title('Correlation of Overtime Hours and Job Satisfaction')
plt.tight_layout()
plt.show()

print('===== Business Correlation =====')
salary_performance = round(df['Monthly Salary']
                      .corr(df['Performance Score']),2)
performance_attendance = round(df['Performance Score']
                               .corr(df['Attendance Rate (%)']),2)
performance_satisfaction = round(df['Performance Score']
                                 .corr(df['Job Satisfaction']),2)
years_salary = round(df['Years at Company']
                     .corr(df['Monthly Salary']),2)
overtime_satisfaction = round(df['Overtime Hours']
                              .corr(df['Job Satisfaction']),2)
overtime_performance = round(df['Overtime Hours']
                             .corr(df['Performance Score']),2)
business_corr = pd.DataFrame({
    "Variable 1": [
        "Monthly Salary",
        "Performance Score",
        "Performance Score",
        "Years at Company",
        "Overtime Hours",
        "Overtime Hours"
    ],
    "Variable 2": [
        "Performance Score",
        "Attendance Rate",
        "Job Satisfaction",
        "Monthly Salary",
        "Job Satisfaction",
        "Performance Score"
    ],
    "Correlation": [
        salary_performance,
        performance_attendance,
        performance_satisfaction,
        years_salary,
        overtime_satisfaction,
        overtime_performance
    ]
})

print(business_corr)