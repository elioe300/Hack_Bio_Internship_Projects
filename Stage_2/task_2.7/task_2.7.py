# Task Code 2.4

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Read the CSV file
data_path = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv"
df = pd.read_csv(data_path, sep=",")

## Task number 1
# Process all NA
df_process = df.dropna()


## Task number 2
# Create and save the first histogram of BMI
df_BMI = df.dropna(subset=["BMI"])
plt.figure(figsize=(10, 6))
sns.histplot(df_BMI["BMI"])
plt.title('Histogram of BMI')
plt.xlabel('BMI')  # Label the X-axis
plt.savefig('histogram_bmi.png')  # Save the plot to a file
plt.show()

# Create and save the second histogram of Weight
df_Weight = df.dropna(subset=["Weight"])
plt.figure(figsize=(10, 6))
sns.histplot(df_Weight["Weight"])
plt.title('Histogram of Weight')
plt.xlabel('Weight')  # Label the X-axis
plt.savefig('histogram_weight.png')  # Save the plot to a file
plt.show()

# Create and save the third histogram of Age
df_Age = df.dropna(subset=["Age"])
plt.figure(figsize=(10, 6))
sns.histplot(df_Age["Age"])
plt.title('Histogram of Age')
plt.xlabel('Age')  # Label the X-axis
plt.savefig('histogram_age.png')  # Save the plot to a file
plt.show()

# Create and save the fourth histogram of Weight in pounds
df_Weight_in_Pounds = df.dropna(subset=["Weight"])
df_Weight_in_Pounds = df["Weight"] * 2.2
plt.figure(figsize=(10, 6))
sns.histplot(df_Weight_in_Pounds, bins=20)
plt.title('Histogram of Weight in Pounds')
plt.xlabel('Weight in Pounds')  # Label the X-axis
plt.savefig('histogram_weight_in_pounds.png')
plt.show()

## Task number 3

# Calculate the mean of the 'Pulse' column
mean_pulse = df["Pulse"].mean()

# Round the mean value to five decimal places
mean_pulse_rounded = round(mean_pulse, 5)

# Print the rounded mean value
print(f"Mean Pulse (rounded to 5 decimal places): {mean_pulse_rounded}")

## Exercise number 3

# Calculate the maximum value of the 'BPDia' column
max_BPDia = df["BPDia"].max()

# Calculate the minimum value of the 'BPDia' column
min_BPDia = df["BPDia"].min()

# Print the minimum and maximum values
print(f"Minimum Diastolic Blood Pressure: {min_BPDia}")
print(f"Maximum Diastolic Blood Pressure: {max_BPDia}")

## Task number 4

# Calculate descriptive statistics for the 'Income' column
describe_income = df["Income"].describe()

# Extract the standard deviation (std) from the descriptive statistics
income_std = describe_income['std']

# Calculate the variance directly from the 'Income' column
income_variance = df["Income"].var()

# Round the standard deviation to five decimal places
income_std_rounded = round(income_std, 5)

# Round the variance to five decimal places
income_variance_rounded = round(income_variance, 5)

# Print the rounded standard deviation and variance
print(f"Standard Deviation (std): {income_std_rounded}")
print(f"Variance: {income_variance_rounded}")

## Task number 5
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Weight", y="Height", hue="Gender")
plt.title('Scatterplot of Weight vs Height (Gender)')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.savefig('scatterplot_weight_vs_height_gender.png')
plt.show()

# Scatterplot 2: Weight vs Height colored by SmokingStatus
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Weight", y="Height", hue="SmokingStatus")
plt.title('Scatterplot of Weight vs Height (SmokingStatus)')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.savefig('scatterplot_weight_vs_height_smokingstatus.png')
plt.show()

# Scatterplot 3: Weight vs Height colored by Diabetes
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Weight", y="Height", hue="Diabetes")
plt.title('Scatterplot of Weight vs Height (Diabetes)')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.savefig('scatterplot_weight_vs_height_diabetes.png')
plt.show()

## Task number 6
# Age vs. Gender
male_age = df[df['Gender'] == 'male']['Age']
female_age = df[df['Gender'] == 'female']['Age']
t_stat, p_value = stats.ttest_ind(male_age.dropna(), female_age.dropna())
print(f"T-Test Age vs. Gender - p-value: {p_value:.5f}")

# BMI vs. Diabetes
bmi_no_diabetes = df[df['Diabetes'] == 'No']['BMI']
bmi_diabetes = df[df['Diabetes'] == 'Yes']['BMI']
t_stat, p_value = stats.ttest_ind(bmi_no_diabetes.dropna(), bmi_diabetes.dropna(), equal_var=False)
print(f"T-Test BMI vs. Diabetes - p-value: {p_value:.5f}")

# Alcohol per year vs. Marital Status
alcohol_single = df[df['RelationshipStatus'] == 'Single']["AlcoholYear"]
alcohol_committed = df[df['RelationshipStatus'] == 'Committed']["AlcoholYear"]
t_stat, p_value = stats.ttest_ind(alcohol_single.dropna(), alcohol_committed.dropna(), equal_var=False)
print(f"T-Test Alcohol vs. Marital Status - p-value: {p_value:.5f}")
