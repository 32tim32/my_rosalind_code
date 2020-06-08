f = open("rosalind_revc.txt", "r")
revc = f.read()
#revc = "AAAACCCGGT"
#Set to lower so I can easily change letters
low_rev = revc.lower()
#Replace letters, not sure if there is a faster way to do this
revc_a = low_rev.replace('t', 'A')
revc_t = revc_a.replace('a', 'T')
revc_c = revc_t.replace('g', 'C')
revc_g = revc_c.replace('c', 'G')
#Flip the output
revc_out = revc_g[::-1]
#Final output
print(revc_out)

outf = open("revc_out.text", "w")
outf.write(revc_out)
outf.close()