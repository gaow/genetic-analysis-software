# KBAC
Record added by Jurg Ott (the original Rockefeller list)

## Full Name
Kernal Based Association for Rare Variants

## Description
This program implements the KBAC statistic in Liu and Leal (2010). It carries out case-control association testing for rare variants for whole exome association studies. Briefly, consider a gene of length N which harbors M rare variants. Genotype on the M variant sites & the disease status (case/control) are known for each individual. The program takes as input the M-site genotype and disease status (case/control) data files, and computes a p value indicating the significance of association. In order to speed up permutation testing we use an “adaptive” approach to obtain p values.

## Year
2010

## Author
Gao Wang (email: gaow@uchicago.edu)

## URL
http://tigerwang.org/software/kbac

## Language
C++,R

## OS
Linux, MacOS

## Reference
Dajiang J. Liu and Suzanne M. Leal (2010). A Novel Adaptive Method for the Analysis of Next-Generation Sequencing Data to Detect Complex Trait Associations with Rare Variants Due to Gene Main Effects and Interactions. PLoS Genetics

## Tag
Association testing, rare variants