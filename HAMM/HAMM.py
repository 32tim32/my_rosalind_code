#open file
f = open("rosalind_hamm.txt", "r")
#f = open("hamm_test.txt", "r")
gc_file = f.read()
#Split on line
line_1, line_2 = gc_file.split('\n')
hamm = 0
for ind in range(0, len(line_1)):
    hamm += (line_1[ind] != line_2[ind])
print(hamm)





#Tester zone
line_1 = "GAGCCTACTAACGGGAT"
line_2 = "CATCGTAATGACGGCCT"

#My tested for loop
hamm = 0
for ind in range(0, len(line_1)):
    hamm += (line_1[ind] != line_2[ind])
print(hamm)