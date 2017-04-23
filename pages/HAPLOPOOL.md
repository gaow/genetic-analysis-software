# HAPLOPOOL
Record added by Jurg Ott (the original Rockefeller list)

## Description
HaploPool is a program for estimating haplotype frequencies either from genotypes of individuals or from genotypes of pooled individuals. The genotypes must be for a block of bi-allelic SNPs (meaning that the SNPs should be in linkage disequilibrium with each other). The program assumes that it is given many genotypes of unrelated diploid individuals in Hardy-Weinberg equilibrium. If the genotypes are from pooled DNA, the program assumes that every pool contains the same number of individuals and the individuals were chosen at random when placed into the pools. For a reasonable running-time, the number of individuals in a pool needs to be between 2 and 4.

## URL
http://haplopool.icsi.berkeley.edu/haplopool/

## Language
gcc/g++, perl, MATLAB

## Reference
Kirkpatrick, Santos-Armendariz, Karp, Halperin (2007), "HaploPool: improving haplotype frequency estimation through DNA pools and phylogenetic modeling", Bioinformatics, 23(22):3048-3055.