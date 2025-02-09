# Week 3 Lab: DNA Sequence
# Description: Consider a fragment of the DNA sequence provided below. Assign it to a variable in Python and do the following:
# Reverse each 8 length sequence (excluding space),
# Count number of times - “TTACT” has occurred.
# ATGTACTC ATTCGTTTCG GAAGAGACAG GTACGTTAAT AGTTAATAGC GTACTTCTTT TTCTTGCTTT
# CGTGGTATTC TTGCTAGTTA CACTAGCCAT CCTTACTGCG CTTCGATTGT GTGCGTACTG CTGCAATATT
# GTTAACGTGA GTCTTGTAAA ACCTTCTTTT TACGTTTACT CTCGTGTTAA AAATCTGAAT TCTTCTAGAG
# TTCCTGATCT TCTGGTCTAA

import re

# DNA sequence
dna_sequence = "ATGTACTC ATTCGTTTCG GAAGAGACAG GTACGTTAAT AGTTAATAGC GTACTTCTTT TTCTTGCTTT CGTGGTATTC TTGCTAGTTA CACTAGCCAT CCTTACTGCG CTTCGATTGT GTGCGTACTG CTGCAATATT GTTAACGTGA GTCTTGTAAA ACCTTCTTTT TACGTTTACT CTCGTGTTAA AAATCTGAAT TCTTCTAGAG TTCCTGATCT TCTGGTCTAA"

# Remove spaces and join into a single sequence
dna_sequence = re.sub(r"\s+", "", dna_sequence)

# Split into chunks of 8
chunks = [dna_sequence[i:i+8] for i in range(0, len(dna_sequence), 8)]

# Reverse each chunk
reversed_chunks = [chunk[::-1] for chunk in chunks]

# Join back into a sequence with spaces
reversed_dna = " ".join(reversed_chunks)

# Count occurrences of "TTACT"
ttact_count = dna_sequence.count("TTACT")

# Output results
print(f"Reversed 8-length sequences:\n{reversed_dna}\n")
print(f"Occurrences of 'TTACT': {ttact_count}")
