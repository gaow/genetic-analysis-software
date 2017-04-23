# SSAHASNP
Record added by Jurg Ott (the original Rockefeller list)

## Full Name
Sequence Search and Alignment by Hashing Algorithm for SNP detection

## Description
ssahaSNP is a polymorphism detection tool. It detects homozygous SNPs and indels by aligning shotgun reads to the finished genome sequence. Highly repetitive elements are filtered out by ignoring those kmer words with high occurrence numbers. For those less repetitive or non-repetitive reads, we place them uniquely on the reference genome sequence and find the best alignment according to the pair-wise alignment score if there are multiple seeded regions. From the best alignment, SNP candidates are screened, taking into account the quality value of the bases with variation as well as the quality values in the neighbouring bases, using neighbourhood quality standard (NQS). For insertions/deletions, we check if the same indel is mapped by more than one read, ensuring the detected indel with high confidence.

## Author
* Adam Spargo
* Zemin Ning (Wellcome Trust Sanger Institute)

## URL
http://www.sanger.ac.uk/resources/software/ssahasnp/