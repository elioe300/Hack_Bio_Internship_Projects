# Gene Expression Analysis Project

## Overview

In this project, we analyze a gene expression dataset, performing data cleaning, visualization, and differential expression analysis. The dataset contains gene expression values, p-values, and log2 fold changes, which help identify upregulated and downregulated genes. Our analysis includes generating a volcano plot and extracting differentially expressed genes based on statistical thresholds.

## Steps to Complete the Analysis

### 1. Load the Dataset

We load the gene expression dataset using Pandas:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# URL of the dataset
url_data = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"

# Load the dataset from the URL
gene_expression_df = pd.read_csv(url_data, sep=" ")
```
In this step, we import the necessary libraries: Pandas (for data manipulation), NumPy (for numerical computations), Matplotlib and Seaborn (for data visualization). Then, we read the dataset from the provided URL using `pd.read_csv()` and store it in a DataFrame named `gene_expression_df`.

### 2. Compute -log10(p-value)

To visualize the significance of gene expression changes, we compute the -log10(p-value):

```python
gene_expression_df['-log10_pvalue'] = -np.log10(gene_expression_df['pvalue'])
```
This transformation makes it easier to interpret the statistical significance of gene expression differences, as lower p-values will appear higher on the volcano plot.

### 3. Differential Expression Analysis

We classify genes as upregulated, downregulated, or not significantly changed:

```python
# Initialize the 'regulation' column with 'No'
gene_expression_df['regulation'] = 'No'

# Label upregulated genes (log2FoldChange > 1 and p-value < 0.01)
gene_expression_df.loc[
    (gene_expression_df['log2FoldChange'] > 1) & (gene_expression_df['pvalue'] < 0.01), 'regulation'
] = 'Up'

# Label downregulated genes (log2FoldChange < -1 and p-value < 0.01)
gene_expression_df.loc[
    (gene_expression_df['log2FoldChange'] < -1) & (gene_expression_df['pvalue'] < 0.01), 'regulation'
] = 'Down'
```
In this step, we initialize a new column `regulation` and set its default value to "No". We then update this column to "Up" for genes with a log2 fold change greater than 1 and a p-value below 0.01, indicating significant upregulation. Similarly, we mark genes with log2 fold change less than -1 and a p-value below 0.01 as "Down", indicating significant downregulation.

### 4. Volcano Plot Visualization

We create a volcano plot to visualize differential gene expression:

```python
# Color map for scatter plot
color_map = {'Up': 'red', 'Down': 'blue', 'No': 'grey'}

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=gene_expression_df, x='log2FoldChange', y='-log10_pvalue', hue='regulation', palette=color_map
)

# Reference lines for significance thresholds
plt.axhline(y=-np.log10(0.01), color='r', linestyle='--', label='p = 0.01')
plt.axvline(x=1, color='r', linestyle='--', label='log2FC = 1')
plt.axvline(x=-1, color='r', linestyle='--', label='log2FC = -1')

# Labels and title
plt.title('Volcano Plot')
plt.xlabel('log2(Fold Change)')
plt.ylabel('-log10(p-value)')
plt.legend(title='Gene Regulation')
plt.show()
```
Here, we create a scatter plot where each point represents a gene. The x-axis shows the log2 fold change, indicating the magnitude of change in expression, while the y-axis shows the -log10(p-value), indicating statistical significance. Genes that are significantly upregulated (red) and downregulated (blue) stand out from non-significant genes (grey). The reference lines mark commonly used significance thresholds.

### Volcano Plot
![Volcano Plot](figures/Volcano%20Plot.png)

### 5. Extracting Differentially Expressed Genes

We extract lists of upregulated and downregulated genes:

```python
# Upregulated genes
upregulated_genes_df = gene_expression_df.loc[
    (gene_expression_df['log2FoldChange'] > 1) & (gene_expression_df['pvalue'] < 0.01)
]
upregulated_genes_list = upregulated_genes_df["Gene"].tolist()

# Downregulated genes
downregulated_genes_df = gene_expression_df.loc[
    (gene_expression_df['log2FoldChange'] < -1) & (gene_expression_df['pvalue'] < 0.01)
]
downregulated_genes_list = downregulated_genes_df["Gene"].tolist()
```
In this step, we filter the dataset to extract genes classified as "Up" and "Down" based on log2 fold change and p-value criteria. We then store the gene names in separate lists for further analysis.

### 6. Identifying the Most Differentially Expressed Genes

We determine the top 5 upregulated and downregulated genes:

```python
# Sort upregulated genes by log2FoldChange in descending order
upregulated_genes_sorted = upregulated_genes_df.sort_values(by='log2FoldChange', ascending=False)
print("Top 5 upregulated genes:", upregulated_genes_sorted["Gene"].head(5).tolist())
#Output: Top 5 upregulated genes: ['DTHD1', 'EMILIN2', 'PI16', 'C4orf45', 'FAM180B']

# Sort downregulated genes by log2FoldChange in descending order
downregulated_genes_sorted = downregulated_genes_df.sort_values(by='log2FoldChange', ascending=False)
print("Top 5 downregulated genes:", downregulated_genes_sorted["Gene"].head(5).tolist())
#Output: Top 5 downregulated genes: ['FAM46B', 'HS3ST3A1', 'PMEL', 'TNFAIP6', 'COL4A2']
```
Here, we sort the upregulated and downregulated genes by their log2 fold change values to identify the most differentially expressed genes. The top 5 genes from each category are printed to highlight the most significant changes.

