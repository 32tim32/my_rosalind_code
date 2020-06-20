f = open("rosalind_subs.txt", "r")
subs = f.read()
subs_split = subs.split("\n")
dna = subs_split[0]
motif = subs_split[1]
#dna = 'GATATATGCATATACTT'
#motif = 'ATAT'
mot_len = len(motif)
indx = 0
mot_found = []
for nuc in dna:
    if nuc == motif[0]:
        if motif == dna[indx:(indx+mot_len)]:
            mot_found.append(indx + 1)
            
    indx += 1
    continue
#The * is used to unpack and make the call iterate 
print(*mot_found, sep =' ')

#Example from Rosalind by Leandro Lima
#Turned my lines 1-5 into one line
s1,s2 = open('rosalind_subs.txt').read().split('\r\n')
#For index that spans the length of the entire question
for i in range(len(s1)):
    #If this index startswith the motif then print the index + 1
    if s1[i:].startswith(s2):
        print(i+1,)
 