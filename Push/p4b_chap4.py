# set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG" 

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
conserved_sites = [24, 56, 132]
print(apes[0])
first_site = conserved_sites[2]

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
chimp_index = apes.index("Pan troglodytes")
# chimp_index is now 1

# counting from the end of the list
last_ape = apes[-1]

ranks = ["kingdom","phylum", "class", "order", "family"]
lower_ranks = ranks[2:5]
# lower ranks are class, order and family

# add element onto the end of an existing list
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
apes.append("Pan paniscus")
print(apes)

# calculate the length of a list
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
print("There are " + str(len(apes)) + " apes")
apes.append("Pan paniscus")
print("Now there are " + str(len(apes)) + " apes")

# concatenate 2 lists 
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
monkeys = ["Papio ursinus", "Macaca mulatta"]
primates = apes + monkeys
print(str(len(apes)) + " apes")
print(str(len(monkeys)) + " monkeys")
print(str(len(primates)) + " primates")

ranks = ["kingdom","phylum", "class", "order", "family"]
print("at the start : " + str(ranks))
# reverse the order of the list
ranks.reverse()
print("after reversing : " + str(ranks))
# sort the list in aphabetical order
ranks.sort()
print("after sorting : " + str(ranks))

# Writing in a loop
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
for ape in apes:
    name_length = len(ape)
    first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters")

# Using string as a list
name = "python"
for character in name:
    print("one character is " + character)
    
# Splitting a string to make a list
names = "melanogaster,simulans,yakuba,ananassae"
species = names.split(",")
print(str(species))

# Iterating over lines in file
# print the length of each lines
file = open("C:/Users/iris/Desktop/Python for Biologist/Chapter 3/examples/dna.txt")
for line in file:
    print("The length is " + str(len(line)))
file.close()

# print the first character of each line
file = open("C:/Users/iris/Desktop/Python for Biologist/Chapter 3/examples/dna.txt")
for line in file:
    print("The first character is " + line[0])
file.close()

# using readlines()
# first store a list of lines in the file
file = open("C:/Users/iris/Desktop/Python for Biologist/Chapter 3/examples/dna.txt")
all_lines = file.readlines()
# print the length
for line in all_lines:
    print("The length is " + str(len(line)))
# print the 1st character
for line in all_lines:
    print("The first character is " + line[0])

# Looping with ranges
# 1 number
for number in range(6):
    print(number)
# 2 numbers
for number in range(3, 8):
    print(number)
# 3 numbers
for number in range(2,14,4):
    print(number)