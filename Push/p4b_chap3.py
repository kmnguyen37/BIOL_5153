my_file = open("dna.txt")

my_string = 'abcdefg'
print(my_string)
my_number = 42
print(my_number+1)

my_file = open("dna.txt")
file_contents = my_file.read()
print(file_contents)

my_file_name = "dna.txt"
my_file = open(my_file_name)
my_file_contents = my_file.read()

# open the file
my_file = open("dna.txt")
# read the contents
my_dna = my_file.read()
# calculate the length
dna_length = len(my_dna)
# print the output
print("sequence is " + my_dna + " and length is " + str(dna_length))

my_file = open("dna.txt")
my_file_contents = my_file.read()
# remove the newline from the end of the file contents
my_dna = my_file_contents.rstrip("\n")
dna_length = len(my_dna)
print("sequence is " + my_dna + " and length is " + str(dna_length))

my_file = open("out.txt", "w")
my_file.write("Hello world")

# write "abcdef"
my_file.write("abc" + "def")
# write "8"
my_file.write(str(len('AGTGCTAG')))
# write "TTGC"
my_file.write("ATGC".replace('A', 'T'))
# write "atgc"
my_file.write("ATGC".lower())
# write contents of my_variable
#my_file.write(my_variable)

