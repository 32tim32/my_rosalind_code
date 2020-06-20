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

print(*mot_found, sep =' ')
 