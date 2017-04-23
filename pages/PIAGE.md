# PIAGE
Record added by Jurg Ott (the original Rockefeller list)

## Full Name
Power of Indirect Association Studies of Gene-Environment Interactions

## Version
1.0 (March 2008)

## Description
The program PIAGE performs estimation of power and sample sizes required to detect genetic and environmental main, as well as gene-environment interaction (GxE) effects in indirect matched case-control studies (1:1 matching). When the hypothesis of GxE is tested, power/sample size will be estimated for the detection of GxE, as well as for the detection of genetic and environmental marginal effects. Furthermore, power estimation is implemented for the joint test of genetic marginal and GxE effects (Kraft P et al., 2007). Power and sample size estimations are based on Gauderman's (2002) asymptotic approach for power and sample size estimations in direct studies of GxE. Hardy-Weinberg equilibrium and independence of genotypes and environmental exposures in the population are assumed. The estimates are based on genotypic codes (G=1 (G=0) for individuals who carry a (non-) risk genotype), which depend on the mode of inheritance (dominant, recessive, or multiplicative). A conditional logistic regression approach is used, which employs a likelihood-ratio test with respect to a biallelic candidate SNP, a binary environmental factor (E=1 (E=0) in (un)exposed individuals), and the interaction between these components.

## Author
* Rebecca Hein (email:r.hein@dkfz-heidelberg.de)
* Lars Beckmann (email:l.beckmann@dkfz-heidelberg.de)

## URL
http://www.dkfz.de/en/epidemiologie-krebserkrankungen/software/software.html

## Language
R

## OS
MS-Windows, Linux

## Reference
* Hein, Beckmann, Chang-Claude (2008), "Sample size requirements for indirect association studies of gene-environment interactions (GxE)", Genetic Epidmiology, to appear.
* Gauderman (2002), "Sample size requirements for matched case-control studies of gene-environment interaction", Statistics in Medicine, 21:35-50.
* Kraft, Yen, Stram, Morrison, Gauderman (2007), "Exploiting gene-environment interaction to detect genetic associations", Human Heredity, 63:1141-1119.