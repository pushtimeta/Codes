import sys
file1 = open(sys.argv[1],'r')
file2 = open(sys.argv[2],'r')
file3 = open(sys.argv[3],'r')
lines1 = file1.readline()
lines2 = file2.readline()
lines = file3.readline()
temp1 = open('temp1.txt','w')
dic1 = {}
#save the gene names from Infectious disease-GeneSets text as keys in dictionary 
for lines in file3:
    dic1[lines.split('\n')[0]]= ""
#generating temporary files to save the important from the known Gene text file
for lines1 in file1: 
    temp1.write(lines1.split('\t')[0]+"\t")
    temp1.write(lines1.split('\t')[1]+"\t")
    temp1.write(lines1.split('\t')[3]+"\t")
    temp1.write(lines1.split('\t')[4]+"\t")
    temp1.write("\n")
temp1.close()
#saving important files from the kgXref text file to another temporary file
temp2 = open("temp2.txt",'w')
for lines2 in file2:
    temp2.write(lines2.split('\t')[0]+"\t")
    temp2.write(lines2.split('\t')[4]+"\t")
    temp2.write("\n")
temp2.close()
#comparing gene names to generate final file. 
temp2 = open("temp2.txt",'r')
l = temp2.readline()
emp = open("genesetcoordinates.txt",'w')
emp.write("Gene"+"\t"+"Chr"+"\t"+"Start"+"\t"+"Stop"+"\n")
for l in temp2:
    if l.split('\t')[1] in dic1.keys():
        dic1[l.split('\t')[1]] = l.split('\t')[0]
temp1 = open("temp1.txt",'r')
x = temp1.readline()
for x in temp1:
    for key,value in dic1.items():
        if x.split('\t')[0] == value:
            emp.write(key+"\t")
            emp.write(x.split('\t')[1]+"\t")
            emp.write(x.split('\t')[2]+"\t")
            emp.write(x.split('\t')[3]+"\t")
            emp.write("\n")
emp.close()

