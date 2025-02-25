# Bacterial Growth Analysis Project

## Overview

In this project, we analyze bacterial growth data, performing data visualization and statistical analysis to compare wild-type (Knock-Out) and mutant (Knock-In) strains. The dataset consists of optical density (OD600) measurements over time for different bacterial strains. Our analysis includes generating growth curves, calculating time to carrying capacity, and performing statistical comparisons.

## Steps to Complete the Analysis

### 1. Load the Dataset

We load the bacterial growth dataset using Pandas:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load dataset (tsv = tab-separated values)
url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
df = pd.read_csv(url, sep="\t")
```

In this step, we import the necessary libraries: Pandas (for data manipulation), Matplotlib and Seaborn (for data visualization), and SciPy (for statistical analysis). Then, we read the dataset from the provided URL using `pd.read_csv()` and store it in a DataFrame named `df`.

### 2. Visualizing Growth Curves

We plot the bacterial growth curves for all strains:

```python
# Extract time column
time = df["time"]
# Identify strains (all columns except 'time')
strains = df.columns[1:]

# Plot growth curves
plt.figure(figsize=(12, 6))  # Set the figure size 
for strain in strains:
    plt.plot(time, df[strain], label=strain)
plt.xlabel("Time (minutes)")  # Label the X-axis
plt.ylabel("OD600 (Bacterial Growth)")  # Label the Y-axis
plt.title("Bacterial Growth Curves")  # Add a title to the plot
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))  # Add a legend outside the plot
plt.show()  # Display the plot
```
### Growth curves
![Growth curves](figures/Bacterial%20Growth%20Curves.png)

Here, we extract the `time` column and identify the bacterial strains in the dataset. Then, we generate a line plot for each strain, showing OD600 measurements over time.

### 3. Calculating Time to Carrying Capacity

We define the time to carrying capacity as the first time point when OD600 reaches 80% of the maximum value for each strain:

```python
def time_to_carrying_capacity(strain):
    """Finds the first time point when OD600 reaches 80% of max OD600."""
    max_od = df[strain].max()
    threshold = 0.8 * max_od
    time_reach = df[df[strain] >= threshold]["time"].min()
    return time_reach

# Compute carrying capacity times for all strains
carrying_times = {strain: time_to_carrying_capacity(strain) for strain in strains}
carrying_df = pd.DataFrame(list(carrying_times.items()), columns=["Strain", "Time_to_Carrying_Capacity"])
```

In this step, we define a function to compute the time to carrying capacity for each strain. The function identifies the first time point when OD600 reaches 80% of the maximum value for that strain.

### 4. Visualizing Time to Carrying Capacity

We generate scatter and box plots to compare time to carrying capacity across strains:

```python
# Scatter plot
plt.figure(figsize=(8, 5))  # Set the figure size
sns.scatterplot(x=carrying_df["Strain"], y=carrying_df["Time_to_Carrying_Capacity"])  # Create a scatter plot
plt.xticks(rotation=90)  # Rotate x-axis labels by 90 degrees
plt.xlabel("Strain")  # Label the X-axis
plt.ylabel("Time to Carrying Capacity (minutes)")  # Label the Y-axis
plt.title("Time to Carrying Capacity for Knock-Out vs. Knock-In Strains")  # Add a title to the plot
plt.show()  # Display the plot
```
### Scatter plot
![Scatter plot](figures/Time%20to%20Carrying%20Capacity%20for%20Knock-Out%20vs.%20Knock-In%20Strains.png)

```python
# Box plot
plt.figure(figsize=(8, 5))  # Set the figure size
sns.boxplot(data=carrying_df, y="Time_to_Carrying_Capacity")  # Create a box plot
plt.ylabel("Time to Carrying Capacity")  # Label the Y-axis
plt.title("Box Plot of Time to Carrying Capacity")  # Add a title to the plot
plt.show()  # Display the plot
```
### Box plot
![Box plot](figures/Box%20Plot%20of%20Time%20to%20Carrying%20Capacity.png)


Here, we create a scatter plot and a box plot to visualize the distribution of time to carrying capacity among different bacterial strains.

### 5. Statistical Comparison of Knock-Out vs. Knock-In Strains

We perform an independent t-test to compare time to carrying capacity between Knock-Out and Knock-In strains:

```python
# Define Knock-Out (WT) and Knock-In (MUT) strains
wt_strains = ["A1", "A3", "A5", "A7", "A9", "A11", "B1", "B3", "B5", "B7", "B9", "B11", "C1", "C3", "C5", "C7", "C9", "C11"]
mut_strains = ["A2", "A4", "A6", "A8", "A10", "A12", "B2", "B4", "B6", "B8", "B10", "B12", "C2", "C4", "C6", "C8", "C10", "C12"]

# Extract times to carrying capacity
knockout_times = carrying_df[carrying_df["Strain"].isin(wt_strains)]["Time_to_Carrying_Capacity"]
knockin_times = carrying_df[carrying_df["Strain"].isin(mut_strains)]["Time_to_Carrying_Capacity"]

if not knockout_times.empty and not knockin_times.empty:
    # Perform an independent t-test
    stat, p_value = ttest_ind(knockout_times, knockin_times, equal_var=False)
    print(f"T-Test P-value: {p_value}")
    if p_value < 0.05:
        print("Significant difference between Knock-Out & Knock-In strains.")
    else:
        print("No significant difference between Knock-Out & Knock-In strains.")
else:
    print("Could not find Knock-Out (-) and Knock-In (+) strain labels in dataset.")

#Output: T-Test P-value: 0.7818650881745381
#Output: No significant difference between Knock-Out & Knock-In strains.
```

Here, we extract the time to carrying capacity values for wild-type (Knock-Out) and mutant (Knock-In) strains and perform an independent t-test to determine whether there is a statistically significant difference between the two groups.

---


