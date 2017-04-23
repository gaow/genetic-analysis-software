# MEGASNPHUNTER
Record added by Jurg Ott (the original Rockefeller list)

## Description
MegaSNPHunter takes case-control genotype data as input and produces a ranked list of multi-SNP interactions. In particular, the whole genome is first partitioned into multiple short subgenomes and a boosting tree classifier is built for each subgenomes based on multi-SNP interactions and then used to measure the importance of SNPs. The method keeps relatively more important SNPs from all subgenomes and let them compete with each other in the same way at the next level. The competition terminates when the number of selected SNPs is less than the size of a subgenome.

## URL
http://bioinformatics.ust.hk/MegaSNPHunter.html

## Reference
Wan, Yang, Yang, Xue, Tang, Yu (2009), "MegaSNPHunter: a learning approach to detect disease predisposition SNPs and high level interactions from whole genome data", BMC Bioinformatics, 10:13.