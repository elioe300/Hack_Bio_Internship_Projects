# Task Code 2.1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load dataset (tsv = tab-separated values)
url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
df = pd.read_csv(url, sep="\t")

# Display first few rows to understand the structure of the dataset
print(df.head())

# Extract time column
time = df["time"]

# Identify strains (all columns except 'time')
strains = df.columns[1:]

# Define WT (Knock-Out) and MUT (Knock-In) strains based on dataset structure
wt_strains = [
    "A1",
    "A3",
    "A5",
    "A7",
    "A9",
    "A11",
    "B1",
    "B3",
    "B5",
    "B7",
    "B9",
    "B11",
    "C1",
    "C3",
    "C5",
    "C7",
    "C9",
    "C11",
]
mut_strains = [
    "A2",
    "A4",
    "A6",
    "A8",
    "A10",
    "A12",
    "B2",
    "B4",
    "B6",
    "B8",
    "B10",
    "B12",
    "C2",
    "C4",
    "C6",
    "C8",
    "C10",
    "C12",
]


# 1️. Plot growth curves for all strains
# This function plots OD600 against time for each strain
# Formula used: OD600 vs Time for each strain
# Parameters:
# - time: Time in minutes (X-axis)
# - OD600: Optical Density at 600 nm (Y-axis)
def plot_growth_curves():
    plt.figure(figsize=(12, 6))
    for strain in strains:
        plt.plot(time, df[strain], label=strain)
    plt.xlabel("Time (minutes)")
    plt.ylabel("OD600 (Bacterial Growth)")
    plt.title("Bacterial Growth Curves")
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.show()


plot_growth_curves()


# 2️. Function to compute time to carrying capacity
# Formula used: OD_threshold = 0.8 * OD_max
# Time to Carrying Capacity: T_carry = min {T | OD600(T) >= OD_threshold}
# Parameters:
# - max_od: Maximum OD600 value for a strain
# - threshold: 80% of max_od, defining carrying capacity
# - time_reach: First time reaching threshold
def time_to_carrying_capacity(strain):
    """Finds the first time point when OD600 reaches 80% of max OD600."""
    max_od = df[strain].max()  # Maximum OD600 value for the strain
    threshold = 0.8 * max_od  # Define 80% threshold
    time_reach = df[df[strain] >= threshold][
        "time"
    ].min()  # Find first time reaching threshold
    return time_reach


# Compute carrying capacity times for all strains
carrying_times = {strain: time_to_carrying_capacity(strain) for strain in strains}

# Convert to DataFrame
carrying_df = pd.DataFrame(
    list(carrying_times.items()), columns=["Strain", "Time_to_Carrying_Capacity"]
)
print(carrying_df.head())


# 3. Scatter plot for carrying capacity times
# This function generates a scatter plot of the time to carrying capacity
# No specific formula; it visualizes the time to carrying capacity for different strains
def plot_scatter():
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=carrying_df["Strain"], y=carrying_df["Time_to_Carrying_Capacity"])
    plt.xticks(rotation=90)
    plt.xlabel("Strain")
    plt.ylabel("Time to Carrying Capacity (minutes)")
    plt.title("Time to Carrying Capacity for Knock-Out vs. Knock-In Strains")
    plt.show()


plot_scatter()


# 4️. Box plot for carrying capacity times
# This function generates a box plot to compare time to carrying capacity across strains
# No specific formula; it visualizes distribution of time to carrying capacity
def plot_box():
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=carrying_df, y="Time_to_Carrying_Capacity")
    plt.ylabel("Time to Carrying Capacity")
    plt.title("Box Plot of Time to Carrying Capacity")
    plt.show()


plot_box()

# 5️. Statistical test for Knock-Out (-) vs. Knock-In (+) strains
# Formula used:
# T-Test: t = (X1 - X2) / sqrt((s1^2/n1) + (s2^2/n2))
# Parameters:
# - knockout_times: Time to carrying capacity for Knock-Out (-) strains
# - knockin_times: Time to carrying capacity for Knock-In (+) strains
# - p_value: Statistical significance test result (T-Test)
# Extract times to carrying capacity for WT (Knock-Out) and MUT (Knock-In)
knockout_times = carrying_df[carrying_df["Strain"].isin(wt_strains)][
    "Time_to_Carrying_Capacity"
]
knockin_times = carrying_df[carrying_df["Strain"].isin(mut_strains)][
    "Time_to_Carrying_Capacity"
]

if not knockout_times.empty and not knockin_times.empty:
    # Perform an independent t-test to check for significant differences
    stat, p_value = ttest_ind(knockout_times, knockin_times, equal_var=False)
    print(f"T-Test P-value: {p_value}")
    if p_value < 0.05:
        print("Significant difference between Knock-Out & Knock-In strains.")
    else:
        print("No significant difference between Knock-Out & Knock-In strains.")
else:
    print("Could not find Knock-Out (-) and Knock-In (+) strain labels in dataset.")