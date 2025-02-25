# Task Code 2.4

import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
sift_path = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv"
foldX_path = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv"

# Read datasets with appropriate separators
df_sift = pd.read_csv(sift_path, sep=r"\s+")
df_foldX = pd.read_csv(filepath_or_buffer=foldX_path, sep=r"\s+")

# Create unique identifier for proteins and amino acids
df_sift['specific_Protein_aa'] = df_sift['Protein'].str.cat(df_sift['Amino_Acid'], sep='_')
df_foldX['specific_Protein_aa'] = df_foldX['Protein'].str.cat(df_foldX['Amino_Acid'], sep='_')

# Merge datasets on the unique identifier
merged_df = pd.merge(df_sift[["Protein", "Amino_Acid", 'specific_Protein_aa', 'sift_Score']],
                     df_foldX[['specific_Protein_aa', 'foldX_Score']],
                     on='specific_Protein_aa')

# Filter deleterious mutations (SIFT score < 0.05 and FoldX score > 2)
mutations_deleterious_df = merged_df.loc[(merged_df["sift_Score"] < 0.05) & (merged_df["foldX_Score"] > 2)]

# Generate frequency table of amino acids
frequency_table = {}
for row in mutations_deleterious_df["Amino_Acid"]:
    first_aa = row[0]
    if first_aa not in frequency_table:
        frequency_table[first_aa] = 1
    else:
        frequency_table[first_aa] += 1

# Display frequency table in console
print(frequency_table)

# Lists for amino acids and their frequencies
keys = list(frequency_table.keys())
values = list(frequency_table.values())

# Bar plot for amino acid frequencies
plt.figure(figsize=(10, 6))
plt.bar(keys, values, color='skyblue')
plt.xlabel('Amino Acid')
plt.ylabel('Frequency')
plt.title('Frequency of Amino Acids')
plt.savefig('Bar plot of Frequency of Amino Acids.png')
plt.show()

# Pie chart for amino acid frequencies
plt.figure(figsize=(8, 8))
plt.pie(values, labels=keys, autopct='%1.1f%%', startangle=140)
plt.title('Frequency of Amino Acids')
plt.axis('equal')
plt.savefig('Pie chart of Frequency of Amino Acids.png')
plt.show()
