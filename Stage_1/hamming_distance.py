def hamming_distance(term_1, term_2):
    """
    Calculates the Hamming distance between two strings of equal length.
    Returns a tuple containing the Hamming distance and a list of differences.
    """
    
    # Check if both terms have the same length
    if len(term_1) != len(term_2):
        return ("Error: Strings must have the same length to calculate Hamming distance.", [])
    
    hamming_distance = 0  # Counter for differing characters
    different_letters = []  # List to store differences
    
    # Iterate through the characters of both strings
    for index in range(len(term_1)):
        if term_1[index] != term_2[index]:
            hamming_distance += 1  # Increment distance for each difference
            statement = f"{term_1[index]} ≠ {term_2[index]}"  # Format the difference
            different_letters.append(statement)
    
    return (f"Hamming Distance: {hamming_distance}", f"Differences: {different_letters}")