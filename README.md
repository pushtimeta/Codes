# Codes

Hi everyone, My name is **Pushti Mehta**. I am a MS Bionformatics student at Georgia Technology. I will be graduating in May'24 and I am looking for full time opportunities. This is just a repository to store my succesful codes that were a part of my assignments and projects. I am proficient in Python, R, CLI, Linux/Unix system and Shell scripting. 

* FindOrthologs - pyhton script that helps find orthologs using blast using reciprocal hit method.

* Kmer_Counter - python script that reads in a FASTA file and a value of k and calculates the number of times each k-mer is observed within the genome. The output is printed on the standard output in two, tab-separated columns

* Vertical_Column - python script that takes in a file and a numerical value (column number) as input and creates a new file that has column extracted. 

mehta_cmds_genomeassembly - shell script that performs following task 
1. fetch SRR20215132
2. quality trim (consider additional options not used in first example)
3. assemble with SPAdes
4. use https://github.com/chrisgulvik/genomics_scripts/blob/master/filter.contigs.py (might only work in Python 2.7.11 with Biopython installed in a conda env) to evaluate how filtering parameters affect your output genome size. Decide which parameters seem reasonable to use to form a higher quality output assembly file that represents the isolate's genome. Save output FastA file as <Last Name>_assembly.fna Include your command in upload.


mehta_cmds.sh - shell script that performs following task 
1. fetch genome https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/009/659/385/GCF_009659385.1_ASM965938v1/GCF_009659385.1_ASM965938v1_genomic.fna.gz recently described as a multi-drug resistant bacterium from ground chicken meat
2. Choose 1 of 3 packages "No one tool to rule them all" manuscript
  GeneMark src manuscript
  GLIMMER src manuscript
  Prodigal src manuscript
3. Predict all coding sequences in the bacterial isolate genome, and store stderr and stdout logfile as a single plaintext ".log" file, and compressed one for submission.
4. Choose 1 of 2 packages
  RNAmmer 
  barrnap
5. Extract all 16S rRNA gene sequences from the assembly file, stored as gunzip compressed FastA format
