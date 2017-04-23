# HAPGEN
Record added by Jurg Ott (the original Rockefeller list)

## Version
1.3.0 (Jan 2008)

## Description
HAPGEN is a program thats simulates case control datasets at SNP markers and can output data in the FILE FORMAT used by IMPUTE, SNPTEST and GTOOL. The approach can handle markers in LD and can simulate datasets over large regions such as whole chromosomes. Hapgen simulates haplotypes by conditioning on a set of population haplotypes and an estimate of the fine-scale recombination rate across the region. The disease model is specified through the choice of a single SNP as the disease causing variant together with the relative risks of the genotypes at the disease SNP. The program is designed to work with publically available files that contain the haplotypes estimated as part of the HapMap project and the estimated fine-scale recombination map derived from that data. Hapgen is computationally tractable. On a modern desktop HAPGEN can simulate several thousand case and control data on a whole chromosome at Hapmap Phase 2 marker density within minutes. This program has been used to assess the power of several different commercially available genotyping chips, in the design stage of the 7 genome-wide association studies carried out by the Wellcome Trust Case-Control Consortium (WTCCC) and for evaluating the power of different methods for detecting association in genome-wide studies.

## Author
* Zhan Su
* Jonathan Marchini
* Peter Donnelly (Univ of Oxford, UK)

## URL
http://www.stats.ox.ac.uk/~marchini/software/gwas/hapgen.html

## Language
C++