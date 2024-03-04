#activate the environment 
conda activate ex1

#make a directory to save fastq files and zip it 
#used fastq-dump to fetch the data
mkdir hw1/raw_data
fasterq-dump SRR20215132 -O exercise_1/raw_data --split-files --qual-defline '+' --seq-defline '@$ac_$sn/$ri' --threads 2 -v
pigz -9f hw1/raw_data/*.fastq

#make directory to save quality assessment of the sequence by fastqc
mkdir ~/hw1/raw_qa
fastqc \
 --threads 2 \
 --outdir exercise_1/raw_qa \
 hw1/raw_data/SRR20215132_1.fastq.gz \
 hw1/raw_data/SRR20215132_2.fastq.gz


#trim the sequences using trimmomatic 
trimmomatic PE -phred33 \
 hw1/raw_data/SRR15276224_1.fastq.gz \
 hw1/raw_data/SRR15276224_2.fastq.gz \
 hw1/trim/r1.paired.fq.gz \
 hw1/trim/r1_unpaired.fq.gz \
 hw1/trim/r2.paired.fq.gz \
 hw1/trim/r2_unpaired.fq.gz \
 SLIDINGWINDOW:5:30 AVGQUAL:30 MINLEN:36

#combining unpaired reads into a single file and deleting unpaired files
cat hw1/trim/r1_unpaired.fq.gz ~/hw1/trim/r2_unpaired.fq.gz > hw1/trim/singletons.fq.gz 
rm -v hw1/trim/*unpaired*
tree hw1/trim

#make directory to save the assembly file 
mkdir ~/hw1/asm 

#genome assembly using spades 
spades -1 hw1/trim/r1.paired.fq.gz -2 hw1/trim/r2.paired.fq.gz -o hw1/asm/ 
pigz -9f spades.log

#filtering contigs
mkdir ~/hw1/filter 
python3 filter.contigs.py -i /home/pushti/hw1/asm/contigs.fasta -o /home/hw1/filter/mehta_assembly.fna.gz -g -m


