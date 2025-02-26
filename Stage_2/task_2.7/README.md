# Health Data Analysis Project

## Overview

In this project, we analyze the NHANES dataset, performing data cleaning, visualization, and statistical analysis. The dataset contains various health-related attributes, including BMI, weight, age, blood pressure, income, and lifestyle factors such as smoking and alcohol consumption. Our analysis includes generating histograms, scatter plots, and conducting statistical tests to uncover patterns and relationships in the data.

## Steps to Complete the Analysis

### 1. Load the Dataset

We load the NHANES dataset using Pandas:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Read the CSV file
data_path = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv"
df = pd.read_csv(data_path, sep=",")
```
In this code snippet, we start by importing the necessary libraries: Pandas (import pandas as pd) for data manipulation, Seaborn (import seaborn as sns) for statistical data visualization, Matplotlib's pyplot module (import matplotlib.pyplotas plt) for creating visualizations, and the stats module from SciPy (from scipy import stats) for statistical analysis. We then load the NHANES dataset from its URL using pd.read_csv(), specifying a comma as the column separator. The dataset is read into a DataFrame named df, enabling efficient data handling and analysis.

### 2. Data Preprocessing

To ensure clean data, we remove missing values:

```python
df_process = df.dropna()
```

### 3. Generate Histograms

We create histograms to visualize the distribution of BMI, weight, age, and weight in pounds.

```python
# BMI Histogram
df_BMI = df.dropna(subset=["BMI"])  # Removes rows with missing BMI values from the DataFrame
plt.figure(figsize=(10, 6))  # Sets the figure size for the histogram plot
sns.histplot(df_BMI["BMI"])  # Plots the BMI values using Seaborn's histplot
plt.title('Histogram of BMI')  # Adds a title to the plot
plt.xlabel('BMI')  # Labels the X-axis
plt.savefig('histogram_bmi.png')  # Saves the generated histogram to a PNG file
plt.show()  # Displays the histogram
```

### BMI Histogram
![BMI Histogram](figures/histogram_bmi.png)

```python
# Weight Histogram
df_Weight = df.dropna(subset=["Weight"])  # Removes rows with missing Weight values from the DataFrame
plt.figure(figsize=(10, 6))  # Sets the figure size for the histogram plot
sns.histplot(df_Weight["Weight"])  # Plots the Weight values using Seaborn's histplot
plt.title('Histogram of Weight')  # Adds a title to the plot
plt.xlabel('Weight')  # Labels the X-axis
plt.savefig('histogram_weight.png')  # Saves the generated histogram to a PNG file
plt.show()  # Displays the histogram
```

### Weight Histogram
![Weight Histogram](figures/histogram_weight.png)

```python
# Age Histogram
df_Age = df.dropna(subset=["Age"])  # Removes rows with missing Age values from the DataFrame
plt.figure(figsize=(10, 6))  # Sets the figure size for the histogram plot
sns.histplot(df_Age["Age"])  # Plots the Age values using Seaborn's histplot
plt.title('Histogram of Age')  # Adds a title to the plot
plt.xlabel('Age')  # Labels the X-axis
plt.savefig('histogram_age.png')  # Saves the generated histogram to a PNG file
plt.show()  # Displays the histogram
```

### Age Histogram
![Age Histogram](figures/histogram_age.png)

```python
# Weight in Pounds Histogram
df_Weight_in_Pounds = df.dropna(subset=["Weight"])  # Removes rows with missing Weight values from the DataFrame
df_Weight_in_Pounds = df["Weight"] * 2.2  # Converts Weight from kilograms to pounds
plt.figure(figsize=(10, 6))  # Sets the figure size for the histogram plot
sns.histplot(df_Weight_in_Pounds, bins=20)  # Plots the Weight in pounds values using Seaborn's histplot
plt.title('Histogram of Weight in Pounds')  # Adds a title to the plot
plt.xlabel('Weight in Pounds')  # Labels the X-axis
plt.savefig('histogram_weight_in_pounds.png')  # Saves the generated histogram to a PNG file
plt.show()  # Displays the histogram
```

### Weight in Pounds Histogram
![Weight in Pounds Histogram](figures/histogram_weight_in_pounds.png)

### 4. Descriptive Statistics

We calculate the mean of the Pulse column, rounding to five decimal places:

```python
mean_pulse = round(df["Pulse"].mean(), 5)
print(f"Mean Pulse (rounded to 5 decimal places): {mean_pulse}")
# Output: Mean Pulse (rounded to 5 decimal places): 73.63382
```
In this step, we calculate the mean of the 'Pulse' column in the DataFrame using the mean() method, round the mean value to five decimal places with the round() function, and print the rounded mean value.

We determine the minimum and maximum values for diastolic blood pressure:

```python
max_BPDia = df["BPDia"].max()
min_BPDia = df["BPDia"].min()
print(f"Minimum Diastolic Blood Pressure: {min_BPDia}")
# Output: Minimum Diastolic Blood Pressure: 0.0
print(f"Maximum Diastolic Blood Pressure: {max_BPDia}")
# Output: Maximum Diastolic Blood Pressure: 116.0
```

In this step, we calculate the maximum and minimum values of the 'BPDia' (Diastolic Blood Pressure) column using the max() and min() methods, and then print these values.

### 5. Standard Deviation and Variance of Income

We calculate and display the standard deviation and variance of income:

```python
describe_income = df["Income"].describe()
income_std_rounded = round(describe_income['std'], 5)
income_variance_rounded = round(df["Income"].var(), 5)

print(f"Standard Deviation (std): {income_std_rounded}")
# Output: Standard Deviation (std): 33489.76064
print(f"Variance: {income_variance_rounded}")
# Output: Variance: 1121564067.88888
```
Here, we calculate descriptive statistics for the 'Income' column in the DataFrame by using the describe() method. We then extract the standard deviation from the descriptive statistics and calculate the variance directly from the 'Income' column. Both the standard deviation and the variance are rounded to five decimal places using the round() function, and finally, the rounded values are printed.

### 6. Scatter Plots

We create scatter plots to analyze relationships between weight, height, gender, smoking status, and diabetes.

```python
# Weight vs Height by Gender
plt.figure(figsize=(10, 6))  # Set the figure size
sns.scatterplot(data=df, x="Weight", y="Height", hue="Gender")  # Scatter plot colored by Gender
plt.title('Scatterplot of Weight vs Height (Gender)')  # Add a title to the plot
plt.xlabel('Weight')  # Label the X-axis
plt.ylabel('Height')  # Label the Y-axis
plt.savefig('scatterplot_weight_vs_height_gender.png')  # Save the plot as a PNG file
plt.show()  # Display the plot
```

### Weight vs Height by Gender
![Weight vs Height by Gender](figures/scatterplot_weight_vs_height_gender.png)

```python
# Weight vs Height by Smoking Status
plt.figure(figsize=(10, 6))  # Set the figure size
sns.scatterplot(data=df, x="Weight", y="Height", hue="SmokingStatus")  # Scatter plot colored by Smoking Status
plt.title('Scatterplot of Weight vs Height (SmokingStatus)')  # Add a title to the plot
plt.xlabel('Weight')  # Label the X-axis
plt.ylabel('Height')  # Label the Y-axis
plt.savefig('scatterplot_weight_vs_height_smokingstatus.png')  # Save the plot as a PNG file
plt.show()  # Display the plot
```

### Weight vs Height by Gender
![Weight vs Height by Gender](figures/scatterplot_weight_vs_height_smokingstatus.png)

```python
# Weight vs Height by Diabetes
plt.figure(figsize=(10, 6))  # Set the figure size
sns.scatterplot(data=df, x="Weight", y="Height", hue="Diabetes")  # Scatter plot colored by Diabetes status
plt.title('Scatterplot of Weight vs Height (Diabetes)')  # Add a title to the plot
plt.xlabel('Weight')  # Label the X-axis
plt.ylabel('Height')  # Label the Y-axis
plt.savefig('scatterplot_weight_vs_height_diabetes.png')  # Save the plot as a PNG file
plt.show()  # Display the plot
```

### Weight vs Height by Diabetes
![Weight vs Height by Diabetes](figures/scatterplot_weight_vs_height_diabetes.png)

### 7. Statistical Tests

We perform T-tests to analyze differences in age by gender, BMI by diabetes status, and alcohol consumption by marital status.

```python
# Age vs. Gender
t_stat, p_value = stats.ttest_ind(df[df['Gender'] == 'male']['Age'].dropna(),
                                  df[df['Gender'] == 'female']['Age'].dropna())
print(f"T-Test Age vs. Gender - p-value: {p_value:.5f}")
# Output: T-Test Age vs. Gender - p-value: 0.08020
```

```python
# BMI vs. Diabetes
t_stat, p_value = stats.ttest_ind(df[df['Diabetes'] == 'No']['BMI'].dropna(),
                                  df[df['Diabetes'] == 'Yes']['BMI'].dropna(),
                                  equal_var=False)
print(f"T-Test BMI vs. Diabetes - p-value: {p_value:.5f}")
# Output: T-Test Age vs. Gender - p-value: 0.08020
```

```python
# Alcohol consumption vs. Marital Status
t_stat, p_value = stats.ttest_ind(df[df['RelationshipStatus'] == 'Single']['AlcoholYear'].dropna(),
                                  df[df['RelationshipStatus'] == 'Committed']['AlcoholYear'].dropna(),
                                  equal_var=False)
print(f"T-Test Alcohol vs. Marital Status - p-value: {p_value:.5f}")
# Output: T-Test Alcohol vs. Marital Status - p-value: 0.00000
```

In this task, we conduct T-tests to compare means between different groups. We extract Age data for males and females, perform a T-test to compare ages between genders, and print the p-value of the T-test. Similarly, we extract BMI data for individuals with and without diabetes, perform a T-test to compare BMI between these groups, and print the p-value. Finally, we extract alcohol consumption data for single and committed individuals, perform a T-test to compare alcohol consumption between these groups, and print the p-value.

---
