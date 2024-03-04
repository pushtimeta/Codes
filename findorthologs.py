#!/usr/bin/env python3 
#This program helps find orthologs using blast from reciprocal hits.
#This python code runs on command line and has requires three necessary input - 2 fasta files with sequences and n/p flag which helps program decide protein blast or nucleotide blast 
import sys
import os
import subprocess
import glob


#This will run blast on the command line
if sys.argv[3] == 'n':
    subprocess.call(["/home/bin/ncbi-blast-2.13.0+/bin/makeblastdb -in %s  -dbtype nucl -out db1 -parse_seqids"%sys.argv[1]], shell=True)
    subprocess.call(["/home/bin/ncbi-blast-2.13.0+/bin/makeblastdb -in %s  -dbtype nucl -out db2 -parse_seqids"%sys.argv[2]], shell=True)
    subprocess.call(["/home/bin/ncbi-blast-2.13.0+/bin/blastn -db db2 -query %s -out /home/python/result1.out -outfmt 6 -max_target_seq 1 "%sys.argv[1]], shell=True)
    subprocess.call(["/home/bin/ncbi-blast-2.13.0+/bin/blastn -db db1 -query %s -out /home/python/result2.out -outfmt 6 -max_target_seq 1"%sys.argv[2]], shell=True)

if sys.argv[3] == 'p':
    subprocess.call(["/home/bin/ncbi-blast-2.13.0+/bin/makeblastdb -in %s  -dbtype prot -out db1 -parse_seqids"%sys.argv[1]], shell=True)
    subprocess.call(["/home/bin/ncbi-blast-2.13.0+/bin/makeblastdb -in %s  -dbtype prot -out db2 -parse_seqids"%sys.argv[2]], shell=True)
    subprocess.call(["/home/bin/ncbi-blast-2.13.0+/bin/blastp -db db2 -query %s -out /home/python/result1.out -outfmt 6 -max_target_seq 1"%sys.argv[1]], shell=True)
    subprocess.call(["/home/bin/ncbi-blast-2.13.0+/bin/blastp -db db1 -query %s -out /home/python/result2.out -outfmt 6 -max_target_seq 1"%sys.argv[2]], shell=True)


#Checks the reciprocals 
file1 = open("/home/python/result1.out",'r')
file2 = open("/home/python/result2.out",'r')
file3 = open("/home/python/output.txt",'w')
d1 = {}
d2 = {}
for l1 in file1:
    d1[l1.split("\t")[0].strip("lcl|")] = l1.split("\t")[1]
for l2 in file2:
    d2[l2.split("\t")[1]] = l2.split("\t")[0].strip("lcl|")
        

for k1,v1 in d1.items():
    for k2,v2 in d2.items():
        if (k1 == k2):
            if (v1 == v2):
                file3.write(k1)
                file3.write("\t")
                file3.write(v2)
                file3.write("\n")


# deletes the files not required by the user 
if sys.argv[3] == 'n':
    for f in glob.glob("db1.*"):
        os.remove(f)

if sys.argv[3] == 'p':
    for f in glob.glob("db2.*"):
        os.remove(f)    

os.remove("result1.out")
os.remove("result2.out")