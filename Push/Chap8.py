# Storing paired data
dna = "AATGATCGATCGTACGCTGA"
all_counts = []
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            count = dna.count(trinucleotide)
            print("count is " + str(count) + " for " + trinucleotide)
            all_counts.append(count)
print(all_counts)
print("count for TGA is " + str(all_counts[24]))

dna = "AATGATCGATCGTACGCTGA"
all_trinucleotides = []
all_counts = []
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            count = dna.count(trinucleotide)
            all_trinucleotides.append(trinucleotide)
            all_counts.append(count)
print(all_counts)
print(all_trinucleotides)

# Creating dictionary 
enzymes = { 'EcoRI':r'GAATTC', 
           'AvaII':r'GG(A|T)CC', 
           'BisI':'GC[ATGC]GC' }
print(enzymes['BisI'])

enzymes = {}
enzymes['EcoRI'] = r'GAATTC'
enzymes['AvaII'] = r'GG(A|T)CC'
enzymes['BisI'] = r'GC[ATGC]GC'

dna = "AATGATCGATCGTACGCTGA"
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            count = dna.count(trinucleotide)
            counts[trinucleotide] = count
print(counts)

## If count is greater than zero
dna = "AATGATCGATCGTACGCTGA"
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            count = dna.count(trinucleotide)
            if count > 0:
                counts[trinucleotide] = count
print(counts)

print("count for TGA is " + str(counts.get('TGA', 0)))
print("count for AAA is " + str(counts.get('AAA', 0)))
print("count for GTA is " + str(counts.get('GTA', 0)))
print("count for TTT is " + str(counts.get('TTT', 0)))

# Iterating over keys
print(counts.keys())

for trinucleotide in counts.keys():
    if counts.get(trinucleotide) == 2:
        print(trinucleotide)
        
for trinucleotide in sorted(counts.keys()):
    if counts.get(trinucleotide) == 2:
        print(trinucleotide)
        
# Iterating over items
for trinucleotide, count in counts.items():
    if count == 2:
        print(trinucleotide)
