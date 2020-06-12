#open file
f = open("rosalind_gc.txt", "r")
gc_file = f.read()
#Split on line
gc_split = gc_file.split('\n')
#Genrate dictionary to store data in
all_gc = {}
#Make an index that'll be used to check the next object in the file
index = 0
for line in gc_split:
    #Detect if new ID and save ID
    #Below if statmement pulls the ID from the first FASTQ line0
    if line.startswith(">"):
        temp_id = line[1:len(line)]
        all_lines_temp = ""
        index += 1
        continue
    #Start counting and saving line data
    all_lines_temp = all_lines_temp + line
    #This first if statement was required as the way I'm looking
    #Forward in the code is with index + 1, which will break the
    #loop. This code allows me to avoid this, though its clunky.
    if index == (len(gc_split)-1):
        G_total = all_lines_temp.count("G")
        C_total = all_lines_temp.count("C")
        percent = (G_total + C_total)/len(all_lines_temp)
        all_gc[temp_id] = percent
        all_lines_temp = ""
        index += 1
        continue
    #Get the next line to test if it has ">" so if it does we
    #Can calculate the GC content
    if gc_split[index + 1].startswith(">"):
        G_total = all_lines_temp.count("G")
        C_total = all_lines_temp.count("C")
        percent = (G_total + C_total)/len(all_lines_temp)
        all_gc[temp_id] = percent
        all_lines_temp = ""
        index += 1
        continue
    index += 1
#Acquire the key associated with max value from dictionary
max_key = max(all_gc, key=all_gc.get)
#Pull all values
all_values = all_gc.values()
#Get max value and round
max_value = round(max(all_values), 8) * 100
#Print results
print(max_key)
print(max_value)
f.close()

##########Other people's work
#Gaik Tamazian
#Max empty container to hold max
max_gc_name, max_gc_content = '', 0

#Strip white and make by line
buf = f.readline().rstrip()
while buf:
    #pull first seq_name (which they can because its stripped)
    #Make empyt seq
    seq_name, seq = buf[1:], ''
    #Confused by seconde buf
    buf = f.readline().rstrip()
    #While line do not start with '>', basically allowing infinite
    #iterations until a new name comes and it breaks once it does
    while not buf.startswith('>') and buf:
        #Add up the sequence
        seq = seq + buf
        #Confused by this
        buf = f.readline().rstrip()
    #Generate the seq_gc content after done interating through an ID
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    #Either you save the id of the max GC content or you go again
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content
#Fancy print magic I don't understand
print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
f.close()



#Bleuest
#Open file and start immediatly looping it
with open('rosalind_gc.txt', mode='r', encoding='utf+8') as file:
#Split on lines and then join all the lines before splitting again on '>'
    re = ''.join(file.read().split('\n')).split('>')
    #Remove whitespace
    re.remove('')
    #New dictionary
    d = {}
    #Iterate over this list of IDs and their following GC content
    for i in re:
        #Rosalind IDs are 14 characters long, using this knowledge
        #they generate the count here by removing the IDs
        #That said the splicing is uneccessary for the x value as
        #Rosalind IDs do not include 'C's or 'G's, but whatever
        #this is a good idea to do anyways.
        x = i[13:].count('C') + i[13:].count('G')
        #Using the spliced i they generate the percent and
        # add it to the dictionary.
        d[i[:13]] = x * 100 / (len(i[13:]))
        #Prints values
print(max(d, key=d.get), max(d.values()))