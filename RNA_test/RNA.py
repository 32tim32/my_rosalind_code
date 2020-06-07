f = open("rosalind_rna.txt", "r")
#Test file below real fil above
#f = open("test.txt", "r")
rna = f.read()
#rna = "GATGGAACTTGACTACGTAAATT"

#Behold, the single line of code that does it
rna_switch = (rna.replace('T', 'U'))

#Writing out to a file because I need to practice that
outf = open("rna_out.text", "w")
outf.write(rna_switch)
outf.close()