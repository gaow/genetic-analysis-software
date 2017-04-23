# POLYMUTT
Record added by Jurg Ott (the original Rockefeller list)

## Full Name
POLYmorphism and de novo MUTaTion call in families with sequencing data

## Description
The program polymutt implemented a likelihood-based framework for calling single nucleotide variants and detecting de novo point mutation events in families for next-generation sequencing data. The program takes as input genotype likelihood format (GLF) files which can be generated following the Creation of GLF files instruction and outputs the result in the [VCF] format. The variant calling and de novo mutation detection are modelled jointly within families and can handle both nuclear and extended pedigrees without consanguinity loops. The input is a set of GLF files for each of family members and the relationships are specified through the .ped file.

## Author
* B Li
* G Abecasis (Univ Michigan)

## URL
http://genome.sph.umich.edu/wiki/Polymutt:_a_tool_for_calling_polymorphism_and_de_novo_mutations_in_families_for_sequencing_data