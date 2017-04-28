# Conditions, True and False
print(3 == 5)
print(3 > 5)
print(3 <=5)
print(len("ATGC") > 5)
print("GAATTC".count("T") > 1)
print("ATGCTT".startswith("ATG"))
print("ATGCTT".endswith("TTT"))
print("ATGCTT".isupper())
print("ATGCTT".islower())
print("V" in ["V", "W", "L"])

# If statements
expression_level = 125
if expression_level > 100:
    print("gene is highly expressed")
    
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
            print(accession)
            
# Else Statement
expression_level = 125
if expression_level > 100:
    print("gene is highly expressed")
else:
    print("gene is lowly expressed")
    
file1 = open("examples/one.txt", "w")
file2 = open("examples/two.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    else:
        file2.write(accession + "\n")
        
# Elif statement
file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    elif accession.startswith('b'):
        file2.write(accession + "\n")
    else:
        file3.write(accession + "\n")
        
# Wile loops
count = 0
while count<10:
    print(count)
    count = count + 1
    
# Building up complex conditions
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a') and accession.endswith('3'):
        print(accession)
        
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if (acc.startswith('a') or acc.startswith('b')) and acc.endswith('4'):
        print(acc)
        
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if acc.startswith('a') and not acc.endswith('6'):
        print(acc)
        
# Writing true/false function
def is_at_rich(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    if at_content > 0.65:
        return True
    else:
        return False

print(is_at_rich("ATTATCTACTA"))
print(is_at_rich("CGGCAGCGCT"))