#Activate the environment created for the class excercise having the software barrnap and bedtools installed 
conda activate ex2_part1 

#make directories to save the data 
mkdir -pv ~/hw2/{ssu,cds}
cd ~/hw2/ssu

#downaloding the assembled file from the given link using wget and zip the file.
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/009/659/385/GCF_009659385.1_ASM965938v1/GCF_009659385.1_ASM965938v1_genomic.fna.gz
gunzip -k *.fna.gz

#Use barrnap for 16S rRNA (small subunit ["ssu"]) gene sequence extraction 
barrnap  GCF_009659385.1_ASM965938v1_genomic.fna  | grep "Name=16S_rRNA;product=16S ribosomal RNA"  > 16S.gff

#Use bedtools to save the extracted sequences to fastA file
#If the index file is not generated, the following command will generate it and run it again. 
bedtools getfasta  -fi GCF_009659385.1_ASM965938v1_genomic.fna  -bed 16S.gff  -fo 16S.fa

#remove the index file for cleanup purposes. 
rm *.fai
conda deactivate

#Activate the environment that has prodigal for coding sequence prediction
conda activate ex2_part2
cd ~/hw2/cds
ls -lh ~/hw2/ssu/*.fna

#Prodigal to isolate and predict genes from assembled file
prodigal  -i ~/hw2/ssu/GCF_009659385.1_ASM965938v1_genomic.fna  -c  -m  -f gbk  -o cds.gbk 2>&1 | tee log.txt

#Check the files
zmore *.gbk.gz
q
zcat log.txt.gz

