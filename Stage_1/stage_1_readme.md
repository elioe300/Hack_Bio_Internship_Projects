# DNA to Protein Translation

## Overview
This Python project provides functions to translate **DNA sequences into protein sequences** using the standard genetic code.

---

## Features
- Converts **DNA to mRNA** before translation.
- Finds the **start codon (ATG)** and translates from there.
- Handles **stop codons** correctly by terminating translation.
- Uses a **genetic code dictionary** for codon-to-amino acid mapping.
- Returns a **list of translated protein sequences**.

---

## Usage
### Translate a full DNA sequence into all possible proteins
```python
proteins = translate_DNA_to_protein("ATGCGATAGCTAGATGCGTGA")
print(proteins)
```

---

## Code Explanation
### When translate_DNA_to_protein is invoked, the following functions are also executed:
#### Functions:
1. translate_DNA_to_mRNA.

Translate a DNA sequence to mRNA
```python
mRNA = translate_DNA_to_mRNA("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(mRNA)  # Output: AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG
```

2. genetic_code.
   
Translate a mRNA sequence to a protein sequence
```python
protein = genetic_code("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
print(protein) # Output: 'MAIVMGR' and 'MGR'. If multiple protein sequences are present within the same mRNA sequence, the function will produce one output at a time. However, since it is encapsulated within a loop, it will ultimately generate all the protein sequences.  
```

3. translate_DNA_to_protein.

Translate a full DNA sequence into all possible proteins
```python
proteins = translate_DNA_to_protein("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(proteins) # Output: ['MAIVMGR', 'MGR']
```

---


# Logistic Growth Model

## Overview

This Python project simulates and generates logistic population growth curves. The logistic equation models population dynamics and is widely used in biological and ecological studies.

---

## Usage
```python
dataframe = logistic_equation(0.1, 10, 1, False, False, 5)
print(dataframe) # Output: {'DataFrame_1': [[0, 0.2689414213699951], [1, 0.289050497374996], [2, 0.31002551887238755], [3, 0.3318122278318339], [4, 0.35434369377420455], [5, 0.3775406687981454], [6, 0.401312339887548], [7, 0.425557483188341], [8, 0.45016600268752216], [9, 0.47502081252106], [10, 0.5], [11, 0.52497918747894], [12, 0.549833997312478], [13, 0.574442516811659], [14, 0.598687660112452], [15, 0.6224593312018546], [16, 0.6456563062257954], [17, 0.6681877721681662], [18, 0.6899744811276125], [19, 0.7109495026250039]]}
```

## Function
logistic_equation(growth_rate, midpoint, L=1, randomize_growth_rate=False, randomize_midpoint=False, iterations=1)

Generates logistic growth data for a specified number of iterations.

- Parameters:

  - growth_rate (float): The growth rate of the population.

  - midpoint (int): The midpoint where population growth slows.

  - L (float): The carrying capacity (default is 1).

  - randomize_growth_rate (bool): If True, assigns a random growth rate between 0.10 and 0.80.

  - randomize_midpoint (bool): If True, assigns a random midpoint between 10 and 80.

  - iterations (int): Number of different logistic growth curves to generate.

- Returns:

  - A dictionary containing logistic growth data for each iteration.


## Code Explanation
### When logistic_equation is invoked, the following functions are also executed:
#### Functions
1. logistic_function.

```python
result = logistic_function(1, 0.1, 10, 1)
print(result) #Output: 0.289050497374996
```

logistic_function(time, growth_rate, midpoint, L)

Computes the logistic function value at a given time.

- Parameters:

  - time (int): The current time step.

  - growth_rate (float): The rate of growth in the function.

  - midpoint (int): The point where the curve transitions.

  - L (float): The carrying capacity (default is 1).

- Returns:

  - The logistic function value at the given time.

2. get_80_percent_result(data_frames, index, midpoint)

```python
result = get_80_percent_result(dataframe, 1, 10)
print(result) # Output: 0.6456563062257954
````

Finds the logistic function value at 80% of the midpoint time.

- Parameters:

  - data_frames (dict): Dictionary containing generated logistic growth data.

  - index (int): Index of the desired dataset.

  - midpoint (int): Midpoint of the logistic curve.

- Returns:

  - The function value at 80% beyond the midpoint.

  
# Hamming Distance Calculator

## Overview
This Python project calculates the **Hamming distance** between two strings of equal length. The Hamming distance measures how many characters are different between two strings at the same position.

---

## Usage
### Calculate the Hamming distance between two strings
```python
result = hamming_distance("Elias", "Elioe")
print(result) # Output: ('Hamming Distance: 2', "Differences: ['a ≠ o', 's ≠ e']")
```

---

## Function

hamming_distance(term_1, term_2)

Calculates the Hamming distance between two strings of equal length.

- Parameters:

  - term_1 (str) : The first term from which you want to extract the Hamming distance.

  - term_2 (str) : The term to which you are comparing for the extraction of the Hamming distance.
  
- Returns:

  - Returns a tuple containing the Hamming distance and a list of differences.


# Requirements

- Python 3.x

- math and random libraries (built-in)

# License

- This project is open-source and available under the MIT License.
