def clean_seq(input_seq):
    clean = input_seq.upper()
    clean = clean.replace('N', '')
    return (clean)

def nuc_seq(sequence, base, sig_digs=2):
    # Calulate the length of the sequnce
    length = len(sequence)
    # Count the number of this nucleotide
    count_of_base = sequence.count(base)
    #Frequency of base
    freq_of_base = round(count_of_base/length, 2)
    # Return the frequency and the length
    return(length, freq_of_base)


# Read FASTA file
data1 = open('watermelon.fsa', 'r')

# Variable that will hold the genome sequence
gen = ''

# Initialize a line counter
line_num = 0

# Read in the genome file
for line in data1:
    line = line.rstrip('\n')

    if line_num > 0:
        gen = gen + line

    # increment line_number
    line_num += 1

# Close the genome file
data1.close()

# Read GFF file
data2 = open('watermelon.gff', 'r')

# Variables for all the feature types 
CDS     = ''
tRNA    = ''
rRNA    = ''
IN      = ''
MF      = ''
RR      = ''

# read in the GFF file
for line in data2:

    # remove newline's - could also use strip
    line = line.rstrip('\n')

    types = line.split('; type ')
    other_type = types[len(types)-1]
    # print(other_type)
    
    cols = line.split('\t')
    type  = cols[2]
    start = int(cols[3])
    end   = int(cols[4])
    
    # print(type, "\t", start, "\t", end)

    # extract this feature from the genome
    fragment = gen[start-1:end]
    fragment = clean_seq(fragment) 
    
    if type == 'CDS':
        CDS += fragment

    if type == 'intron':
        IN += fragment

    if type == 'misc_feature':
        MF += fragment

    if type == 'repeat_region':
        RR += fragment

    if type == 'rRNA':
        rRNA += fragment

    if type == 'tRNA':
        tRNA += fragment

list_FT = [CDS, IN, tRNA, rRNA, MF, RR]
for FT in list_FT:
    for nucleotide in ['A', 'T', 'G', 'C']:
        (Fl, Fc) = nuc_seq(FT, nucleotide, sig_digs=2)
        print(str(type) +'\t' + str(Fl) + str(Fc) +'%\t' + nucleotide)


# close the GFF file
data2.close()