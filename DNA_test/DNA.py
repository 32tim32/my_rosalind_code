f = open("rosalind_dna.txt", "r")
dna = f.read()

#dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
a_count = 0
g_count = 0
c_count = 0
t_count = 0


for nuc in dna:
    if nuc == "A":
        a_count += 1
    if nuc == "G":
        g_count += 1
    if nuc == "C":
        c_count += 1
    if nuc == "T":
        t_count += 1

a_count = str(a_count)    
c_count = str(c_count)   
g_count = str(g_count)   
t_count = str(t_count)   

print(a_count + " " + c_count + " " + g_count + " " + t_count)
