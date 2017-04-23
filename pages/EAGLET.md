# EAGLET
Record added by Jurg Ott (the original Rockefeller list)

## Full Name
Efficient Analysis of Genetic Linkage: Testing and Estimation

## Version
1.1

## Description
EAGLET is a software package that provides a number of improved statistics for detecting linkage and estimating trait location. EAGLET uses multiple subsamples of dense SNP data to detect linkage with increased power, and to construct sharp 95% confidence intervals for the true trait location. Subsamples with minimal amounts of LD are repeatedly drawn from the original dense SNP data, and the linkage information across subsamples is then combined. This minimizes the false positive evidence for linkage that LD can create in classical multipoint linkage analysis due to an apparent excess in allele sharing among affecteds. Another attractive feature of EAGLET is that by using multiple subsamples, as opposed to one, EAGLET's estimate of trait location is greatly improved. EAGLET can be used to generate subsamples for custom linkage packages as well, and computes standard LD statistics via the EM algorithm.

## Author
William C.L. Stewart (email: ws2267@columbia.edu)

## URL
http://www.columbia.edu/~ws2267/SOFT/EAGLET/eaglet.html

## Language
Perl, C

## OS
Linux, MacOS

## EXE
eaglet.pl

## Reference
Stewart, Peljto, Greenberg (2009), "Multiple subsampling of dense SNP data localizes disease genes with increased precision", Human Heredity, to appear.