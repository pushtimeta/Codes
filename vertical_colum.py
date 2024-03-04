import sys
#opening the input file
infile = open(sys.argv[2],'r')
#saving the column number as integer
n = int(sys.argv[1])
lines = infile.readline()
result = []
f = open("column.txt",'w')
for lines in infile: 
    f.write(lines.split('\t')[n])
    f.write("\n")
f.close()