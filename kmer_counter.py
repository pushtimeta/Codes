import sys 
kmer = {}
infile = open(sys.argv[2],'r')
k = int(sys.argv[1])
#generating kmers and saving in dictionary
for line in infile:
    if line[0] != '>':
        dna = line.strip('\n')
        kmercount = len(dna)-k+1
        for i in range(kmercount):
            a = dna[i:i+k]
            if len(a) == k:
                if a not in kmer.keys():
                    kmer[a] = 1 
                else:
                    kmer[a] += 1
#saving it into a text file                    
f = open("kmer.txt",'w')
for k, v in kmer.items():
    f.write("%s" %k + "\t" + "%d" %v)
    f.write("\n")
f.close()
infile.close()