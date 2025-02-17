# Function to translate a DNA sequence into a protein sequence
def genetic_code(mRNA_sequence):
    translated_protein = ""
    
    # Genetic code dictionary
    genetic_code_dict = {
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
    'UAC': 'Y', 'UAU': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGC': 'C', 'UGU': 'C', 'UGA': 'Stop', 'UGG': 'W'
}


    # Iterate through the DNA sequence in steps of 3 (triplets)
    for i in range(0, len(mRNA_sequence), 3):
        codon = mRNA_sequence[i:i+3]  # Extract codon (three nucleotides)

        # Ensure the codon is exactly three nucleotides
        if len(codon) != 3:
            break
        
        # Stop translation if a STOP codon is encountered
        if codon in ["UAA", "UAG", "UGA"]:
            break

        # Add the corresponding amino acid to the translated protein
        translated_protein += genetic_code_dict.get(codon) 

    return translated_protein  # Return the translated protein sequence

def translate_DNA_to_mRNA(DNA_sequence):
    return DNA_sequence.upper().replace("T", "U")

# Function to find the start codon and translate from there
def translate_DNA_to_protein(DNA_sequence):
    translated_proteins_list = []
    mRNA_sequence = translate_DNA_to_mRNA(DNA_sequence)

    # Loop through the DNA sequence in triplets
    for i in range(0, len(mRNA_sequence), 3):
        codon = mRNA_sequence[i:i+3]

        # Ensure the codon is exactly three nucleotides
        if len(codon) != 3:
            break
        
        # If start codon "ATG" is found, translate from this point
        if codon == "AUG":
            protein = genetic_code(mRNA_sequence[i:])  # Translate from start codon
            translated_proteins_list.append(protein)

    return translated_proteins_list  # Return list of translated proteins
