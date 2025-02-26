# [Bacterial Growth Analysis Project](./task_2.1/)

## Dataset Information
- [Look at this dataset here](https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv)
- [This is the description of the dataset.](https://github.com/HackBio-Internship/2025_project_collection/blob/main/Python/Dataset/mcgc_METADATA.txt)

## Tasks Overview
This project involves analyzing microbiology data to understand the growth patterns of different strains and to compare the knock out (-) and knock in (+) strains. Below are the tasks to be completed:

### 1. Plot Growth Curves
- Plot all the growth curves of OD600 vs. Time for the different strains.
- For each strain, plot the growth curve of the knock out (-) and knock in (+) strains overlaid on top of each other.

### 2. Determine Time to Reach Carrying Capacity
- Using your function from the previous stage, determine the time it takes to reach the carrying capacity for each strain/mutant.

### 3. Generate Scatter Plot
- Create a scatter plot of the time it takes to reach carrying capacity for the knock out and knock in strains.

### 4. Generate Box Plot
- Create a box plot of the time it takes to reach carrying capacity for the knock out and knock in strains.

### 5. Statistical Analysis
- Determine if there is a statistical difference in the time it takes for the knock out strains to reach their maximum carrying capacity compared to the knock in strains.
- Explain your observations as comments in your code.
  
---

# [Protein Mutations Analysis Project](./task_2.4/)

## Dataset Information
- [SIFT Dataset](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv)
- [FoldX Dataset](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv)

## Tasks Overview
This project involves combining and analyzing data from the SIFT and FoldX datasets to investigate protein mutations. Below are the tasks to be completed:

### 1. Import and Process Datasets
- Import both SIFT and FoldX datasets.
- In both datasets, create a column `specific_Protein_aa` which concatenates the `Protein` and `Amino_acid` columns. For example, if you have Protein A5A607 and Amino_acid E63D, you get `specific_Protein_aa` as A5A607_E63D.

### 2. Merge Datasets
- Using the `specific_Protein_aa` column, merge the SIFT and FoldX datasets into one final dataframe.

### 3. Identify Deleterious Mutations
- According to the authors:
  - A SIFT Score below 0.05 is deleterious.
  - A FoldX score greater than 2 kCal/mol is deleterious.
- Using the criteria above, find all mutations that have a SIFT score below 0.05 and a FoldX score above 2. These mutations affect both structure and function.

### 4. Study Amino Acid Substitution
- Study the amino acid substitution nomenclature.
- Investigate which amino acid has the most functional and structural impact.

### 5. Generate Frequency Table
- Generate a frequency table for all the amino acids.

### 6. Visualize Data
- Using the amino acid frequency table, generate a barplot and pie chart to represent the frequency of the amino acids.

### 7. Analyze Amino Acid Impact
- Briefly describe the amino acid with the highest impact on protein structure and function.
- Discuss the structural and functional properties of amino acids with more than 100 occurrences.

---

# [Gene Expression Analysis Project](./task_2.6/)

## Dataset Information
- [Access Dataset Here](https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt)

## Tasks Overview
This project involves analyzing gene expression data to identify significant changes in gene regulation and understand the functions of key genes. Below are the tasks to be completed:

### 1. Generate a Volcano Plot
- Create a volcano plot to visualize the relationship between the magnitude of change (log2 fold change) and statistical significance (p-value) of gene expression data.

### 2. Identify Upregulated Genes
- Determine the upregulated genes in the dataset.
  - **Criteria**: Genes with Log2FC > 1 and p-value < 0.01.

### 3. Identify Downregulated Genes
- Determine the downregulated genes in the dataset.
  - **Criteria**: Genes with Log2FC < -1 and p-value < 0.01.

### 4. Analyze Gene Functions
- Investigate the functions of the top 5 upregulated genes and the top 5 downregulated genes using GeneCards.

---

# [Health Data Analysis Project](./task_2.7/)

## Dataset Information
- [Dataset here](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv)
- [Data Dictionary](https://github.com/HackBio-Internship/public_datasets/blob/main/R/nhanes_dd.csv)

## Tasks Overview
This project involves processing and analyzing health data to extract meaningful insights and visualize relationships between different variables. Below are the tasks to be completed:

### 1. Process Missing Values
- Process all NA values either by deleting them or converting them to zero. 

### 2. Visualize Distributions
- Create histograms to visualize the distribution of the following variables:
  - BMI
  - Weight
  - Weight in pounds (Weight * 2.2)
  - Age

### 3. Calculate Statistical Measures
- Calculate the mean 60-second pulse rate for all participants in the data. 

### 4. Determine Range of Diastolic Blood Pressure
- Find the range of values for diastolic blood pressure among all participants.
  
### 5. Compute Variance and Standard Deviation for Income
- Calculate the variance and standard deviation for income among all participants.

### 6. Visualize Relationships
- Visualize the relationship between weight and height using scatter plots. Color the points by the following categories:
  - Gender
  - Diabetes
  - Smoking Status

### 7. Conduct T-Tests
- Perform t-tests between the following variables and draw conclusions based on the p-value:
  - Age and Gender
  - BMI and Diabetes
  - Alcohol Year and Relationship Status

---
