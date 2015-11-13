# CpG Islands prediction using Hidden Markov Model:

###Input and Output Files Format:


#####Sequence Files: 
"training.txt" is the input genomic sequence. The whole sequence
is divided in multiple lines and such format is known as multi-fasta.  Note that
the length of the complete sequence for the given training file should be 85000.
A similar test file (testing.txt) is given.

#####FILE cpg_island_training.txt format: 
A separate file denoting the cpg islands in the training sequence where:
1. Each line of this file denotes a cpg island in the above sequence.  
2. Consider the following.  347 584. It denotes that the cpg island starts
from position 347 and ends at position 584 (584 included).  

###TASK: 
To generate a similar cpg_island file for the test data using your learned model. More details about the problem can be found on this link: http://www.cse.iitd.ernet.in/~parags/teaching/col776/assignments/ass2/ass2-b.pdf

###Program description:
1. Given a training data file and the corresponding file denoting cpg islands in the sequence, it learns the HMM model.

###HOW TO RUN:
python cpg.py
