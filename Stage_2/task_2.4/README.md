# Protein Mutations Analysis Project

## Tasks Overview

In this project, we aim to combine and analyze data from the SIFT and FoldX datasets to investigate protein mutations. The SIFT dataset provides scores indicating the functional impact of amino acid substitutions, with a score below 0.05 considered deleterious. The FoldX dataset offers scores related to the structural impact, where a score greater than 2 kCal/mol is deemed deleterious.
We then identify mutations that are both functionally and structurally impactful. Furthermore, we analyze the frequency of amino acids involved in these significant mutations and visualize the data using bar plots and pie charts to better understand the patterns and impacts of these amino acid substitutions.

## Steps to Complete the Tasks

### 1. Import Datasets

Load the SIFT and FoldX datasets using pandas:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
sift_path = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv"
foldX_path = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv"
df_sift = pd.read_csv(sift_path, sep=r"\s+")
df_foldX = pd.read_csv(filepath_or_buffer=foldX_path, sep=r"\s+")
```
In this code snippet, we start by importing the necessary libraries, Pandas (`import pandas as pd`) for data manipulation and Matplotlib's `pyplot` module (`import matplotlib.pyplot as plt`) for creating visualizations. We then load the SIFT and FoldX datasets from their respective URLs using `pd.read_csv()`, specifying that the columns in the files are separated by whitespace characters. The datasets are read into DataFrames `df_sift` and `df_foldX`, enabling efficient data handling and analysis.

### 2. Create Unique Identifier

In this step, we create a unique identifier column called  `specific_Protein_aa` by concatenating the `Protein` and  `Amino_Acid` columns in both datasets. This unique identifier helps in matching records between the two datasets:


```python
df_sift['specific_Protein_aa'] = df_sift['Protein'].str.cat(df_sift['Amino_Acid'], sep='_')
df_foldX['specific_Protein_aa'] = df_foldX['Protein'].str.cat(df_foldX['Amino_Acid'], sep='_')
```

### 3. Merge Datasets

Here, we merge the SIFT and FoldX datasets based on the `specific_Protein_aa` column. This merged dataset combines information from both datasets into a single dataframe, allowing for comprehensive analysis:
```python
merged_df = pd.merge(df_sift[["Protein", "Amino_Acid", 'specific_Protein_aa', 'sift_Score']],
                     df_foldX[['specific_Protein_aa', 'foldX_Score']],
                     on='specific_Protein_aa')
```

### 4. Identify Deleterious Mutations

In this step, we filter the merged dataset to identify deleterious mutations. Mutations are considered deleterious if the SIFT score is below 0.05 and the FoldX score is above 2. This filtering helps in pinpointing mutations that significantly affect both function and structure:

```python
mutations_deleterious_df = merged_df.loc[(merged_df["sift_Score"] < 0.05) & (merged_df["foldX_Score"] > 2)]
```

### 5. Analyze Amino Acid Substitution

In this step, we generate a frequency table for the first amino acid in the `Amino_Acid` column. The code iterates through the `Amino_Acid` column of the `mutations_deleterious_df` dataframe, extracts the first amino acid of each mutation, and counts the occurrences of each amino acid.

```python
frequency_table = {}
for row in mutations_deleterious_df["Amino_Acid"]:
    first_aa = row[0]
    if first_aa not in frequency_table:
        frequency_table[first_aa] = 1
    else:
        frequency_table[first_aa] += 1

# Display frequency table
print(frequency_table)
```

### 6. Generate Frequency Table

Here, we convert the frequency table into two separate lists: one for the amino acids (keys) and one for their frequencies (values). These lists will be used to create visualizations in the next step.

```python
keys = list(frequency_table.keys())
values = list(frequency_table.values())
```

### 7. Visualize Data

In this step, we create visual representations of the amino acid frequencies using bar plots and pie charts. This helps in understanding the distribution and impact of different amino acids in the deleterious mutations.

```python
# Bar plot for amino acid frequencies
plt.figure(figsize=(10, 6))
plt.bar(keys, values, color='skyblue')
plt.xlabel('Amino Acid')
plt.ylabel('Frequency')
plt.title('Frequency of Amino Acids')
plt.savefig('Bar_plot_of_Frequency_of_Amino_Acids.png')
plt.show()
```

### Bar Plot
![Bar Plot of Frequency of Amino Acids](figures/Bar%20plot%20of%20Frequency%20of%20Amino%20Acids.png)

```python
# Pie chart for amino acid frequencies
plt.figure(figsize=(8, 8))
plt.pie(values, labels=keys, autopct='%1.1f%%', startangle=140)
plt.title('Frequency of Amino Acids')
plt.axis('equal')
plt.savefig('Pie_chart_of_Frequency_of_Amino_Acids.png')
plt.show()
```

### Pie Chart
![Pie Chart of Frequency of Amino Acids](figures/Pie%20chart%20of%20Frequency%20of%20Amino%20Acids.png)



