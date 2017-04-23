# PSEUDO
Record added by Jurg Ott (the original Rockefeller list)

## Version
0.3.5

## Description
Pseudo estimates genomewide empirical p-values for Kong and Cox tests of linkage using the replicate pool method, which for many data sets, improves upon the computational efficiency of conventional gene-dropping methods by several orders of magnitude. This allows Pseudo to handle data sets with large families and makes it particularly applicable to those situations where p-value estimation by standard methods is computationally prohibitive. Pseudo also estimates variance for reported p-values, produces graphical and text summaries of results, and is able to assess significance of multiple correlated outcomes. Pseudo is designed to work with the Merlin package and includes utilities for generating input files from standard Merlin output.

## Author
* Janis Wigginton (email:wiggie@umich.edu)
* Goncalo Abecasis

## URL
http://www.sph.umich.edu/csg/abecasis/pseudo/download

## Language
C,C++

## OS
Linux, UNIX, MacOS, MS-Windows

## EXE
pseudo, scan

## Reference
Wigginton, Abecasis (2006), "An evaluation of the replicate pool method: quick estimation of genome-wide linkage peak p-values", Genetic Epidemiology, 30(4):320-332.