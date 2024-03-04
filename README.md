# Codes

Just a repository to store my succesful codes that were a part of my assignments and projects.

FindOrthologs - This program helps find orthologs using blast from reciprocal hits.

Kmer_Counter - script that reads in a FASTA file and a value of k and calculates the number of times each k-mer is observed within the genome. The output is printed on the standard output in two, tab-separated columns

mehta_cmds_genomeassembly - 
Task 
fetch SRR20215132
quality trim (consider additional options not used in first example)
assemble with SPAdes
use https://github.com/chrisgulvik/genomics_scripts/blob/master/filter.contigs.py (might only work in Python 2.7.11 with Biopython installed in a conda env) to evaluate how filtering parameters affect your output genome size. Decide which parameters seem reasonable to use to form a higher quality output assembly file that represents the isolate's genome. Save output FastA file as <Last Name>_assembly.fna Include your command in upload.
