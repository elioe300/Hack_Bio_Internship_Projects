# Functions Galore!

## Task Overview
This task involves writing multiple functions related to bioinformatics and population modeling. Follow the instructions below to complete each part of **Task 1**.

---

## 1. Translate DNA to Protein
- Write a function that takes a **DNA sequence** as input and returns the **corresponding protein sequence**.
- Use the standard genetic code to map codons to amino acids.
- Ensure your function considers start/stop codons.

[Please refer to the README document for a comprehensive explanation.](https://github.com/elioe300/Hack_Bio_Internship_Projects/blob/main/Stage_1/stage_1_readme.md#dna-to-protein-translation)]

---

## 2. Simulate Logistic Population Growth
- Write a function that **simulates a logistic population growth curve**.
- The function should:
  - Include **two extra parameters** that randomize the length of the **lag phase** and **exponential phase**.
  - Allow for different representations of population growth, such as:
    - **Population Size vs. Time**
    - **Cell Density vs. Time**
    - **Optical Density (OD) vs. Time**
    - **Colony Forming Units (CFU) vs. Time**

[[See population growth curve reference here](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fsrep15159/MediaObjects/41598_2015_Article_BFsrep15159_Fig1_HTML.jpg)]

[Please refer to the README document for a comprehensive explanation.](https://github.com/elioe300/Hack_Bio_Internship_Projects/blob/main/Stage_1/stage_1_readme.md#logistic-growth-model)]

---

## 3. Generate 100 Growth Curves
- Using your logistic growth function, generate a **dataframe** with **100 different growth curves**.
- Ensure that each curve varies by introducing randomness in the lag and exponential phases.
- Store the data in a structured format for easy analysis.

---

## 4. Determine Time to 80% Maximum Growth
- Write a function that calculates the **time required to reach 80% of the carrying capacity**.
- This is an important metric in population studies.
- The function should take in a growth curve dataset and return the corresponding time point.

---

## 5. Calculate Hamming Distance
- Write a function to compute the **Hamming distance** between:
  - Your **Slack username**
  - Your **Twitter/X handle**.
- Return the distance as an integer and explain any transformations made.
  
[Please refer to the README document for a comprehensive explanation.](https://github.com/elioe300/Hack_Bio_Internship_Projects/blob/main/Stage_1/stage_1_readme.md#hamming-distance-calculator)]

---

## Submission Guidelines
- Write **clean and well-documented** code.
- Ensure functions are modular and reusable.
- Include **error handling** where necessary.
