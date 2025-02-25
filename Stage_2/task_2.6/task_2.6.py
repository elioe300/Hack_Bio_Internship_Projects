# Task Code 2.6

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# URL of the dataset
url_data = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"

# Load the dataset from the URL
gene_expression_df = pd.read_csv(url_data, sep=" ")

# Calculate the -log10(p-value) for visualization
gene_expression_df['-log10_pvalue'] = -np.log10(gene_expression_df['pvalue'])

## Differential expression analysis 
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

# Color map for scatter plot
color_map = {'Up': 'red', 'Down': 'blue', 'No': 'grey'}

## Volcano plot for differential expression visualization
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

## Extraction of differentially expressed genes
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

## Identification of the most differentially expressed genes
# Sort upregulated genes by log2FoldChange in descending order
upregulated_genes_sorted = upregulated_genes_df.sort_values(by='log2FoldChange', ascending=False)
print("Top 5 upregulated genes:", upregulated_genes_sorted["Gene"].head(5).tolist())

# Sort downregulated genes by log2FoldChange in descending order
downregulated_genes_sorted = downregulated_genes_df.sort_values(by='log2FoldChange', ascending=False)
print("Top 5 downregulated genes:", downregulated_genes_sorted["Gene"].head(5).tolist())